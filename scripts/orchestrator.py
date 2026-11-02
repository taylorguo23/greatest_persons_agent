#!/usr/bin/env python3
"""
Single-entrypoint CLI orchestrator for `greatest-persons`.
Searches config/registry.json across all 200 textbook figures and loads playbooks
for Council Mode (multi-agent critique) or Worker Mode (direct execution).
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = ROOT / "config" / "registry.json"

SENSITIVE_BLOCKLIST = {
    "mao", "mao_zedong", "mao-contradiction-strategy",
    "stalin", "hitler", "lenin", "pol_pot", "chiang_kai_shek"
}


def load_registry() -> dict:
    if not REGISTRY_PATH.exists():
        sys.exit("Error: config/registry.json not found. Run `python3 scripts/build_200_personas.py` first.")
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def normalize(name: str) -> str:
    return name.strip().lower().replace("-", "_").replace(" ", "_")


def is_safe(slug: str) -> bool:
    slug = normalize(slug)
    return slug not in SENSITIVE_BLOCKLIST and not any(b in slug for b in SENSITIVE_BLOCKLIST)


def select_council(registry: dict, task: str, top_k: int = 3) -> list[str]:
    tokens = set(normalize(task).replace(",", " ").split())
    scored = []
    for slug, info in registry.items():
        if not is_safe(slug):
            continue
        haystack = " ".join(info["tags"] + [info["summary"].lower(), info["domain"].lower(), info["archetype"].lower()])
        score = sum(2 for t in info["tags"] if t in task.lower())
        score += sum(1 for tok in tokens if len(tok) > 3 and tok in haystack)
        scored.append((score, info["domain"], slug))

    scored.sort(key=lambda x: x[0], reverse=True)

    # Pick top matches across distinct domains for diverse council perspectives
    selected, used_domains = [], set()
    for score, domain, slug in scored:
        if score > 0 and domain not in used_domains:
            selected.append(slug)
            used_domains.add(domain)
            if len(selected) == top_k:
                break

    defaults = ["richard_feynman", "claude_shannon", "zhuge_liang", "zhang_heng"]
    for d in defaults:
        if len(selected) < top_k and d in registry and d not in selected:
            selected.append(d)

    return selected[:top_k]


def read_playbook(registry: dict, slug: str) -> str:
    slug = normalize(slug)
    if not is_safe(slug):
        sys.exit(f"Error: Persona '{slug}' is blocked by the safety filter.")
    if slug not in registry:
        # Try partial match
        matches = [k for k in registry if slug in k and is_safe(k)]
        if not matches:
            sys.exit(f"Error: Persona '{slug}' not found in the 200-person registry.")
        slug = matches[0]

    md_path = ROOT / registry[slug]["path"]
    return md_path.read_text(encoding="utf-8")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Greatest Persons (200 Textbook Minds) Orchestrator")
    parser.add_argument("--mode", choices=["list", "search", "council", "worker"], default="list")
    parser.add_argument("--persona", help="Persona slug for worker mode (e.g. richard_feynman)")
    parser.add_argument("--task", default="", help="Task or search query")
    parser.add_argument("--top-k", type=int, default=3, help="Number of council members to convene")
    args = parser.parse_args()

    registry = load_registry()

    if args.mode == "list":
        print(f"Total Registered Textbook Personas: {len(registry)}\n")
        for slug, info in registry.items():
            print(f"- {slug:22s} | {info['name']:28s} | {info['domain']} | {info['archetype']}")
        return

    if args.mode == "search":
        q = args.task.lower()
        for slug, info in registry.items():
            if q in slug or q in info["name"].lower() or q in info["summary"].lower() or any(q in t for t in info["tags"]):
                print(f"- {slug}: {info['name']} ({info['archetype']}) — {info['summary']}")
        return

    if args.mode == "worker":
        if not args.persona:
            sys.exit("Error: --persona <slug> is required for worker mode.")
        print(read_playbook(registry, args.persona))
        return

    if args.mode == "council":
        members = select_council(registry, args.task, args.top_k)
        print(f"=== CONVENING GREATEST PERSONS COUNCIL: {', '.join(members)} ===\n")
        for m in members:
            print(read_playbook(registry, m))
            print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
