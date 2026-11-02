# Greatest Persons (`greatest-persons`)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Personas: 200](https://img.shields.io/badge/Textbook_Personas-200-success.svg)](config/registry.json)
[![Domains: 10](https://img.shields.io/badge/Domains-10-purple.svg)](#the-10-domains-200-personas)
[![Install: Single Skill](https://img.shields.io/badge/Gateway-Single_Skill_Install-orange.svg)](SKILL.md)

**200 of history's greatest textbook minds—acting as an advisory council and active worker agents through a single, one-time skill installation.**

Unlike persona repositories that pollute your agent workspace with dozens of separate skill folders or roleplay modern tech executives, **Greatest Persons** installs as **one unified gateway skill** (`greatest-persons`) and dynamically loads first-principles playbooks derived from 200 canonical textbook figures across physics, mathematics, computer science, engineering, chemistry, medicine, philosophy, strategy, economics, and design.

---

## Why `greatest-persons`?

- **One-Time, Single-Skill Installation:** Exposes just **1** gateway skill (`greatest-persons`) to your AI coding assistant (Antigravity, Claude Code, Cursor, Gemini CLI, Codex, or custom harnesses) while indexing all 200 figures in [`config/registry.json`](config/registry.json). Zero context bloat until invoked.
- **Council + Worker Dual Execution:**
  - **Council Mode (Comment & Suggest):** Convene 3–4 cross-disciplinary minds in parallel (e.g., *Richard Feynman + Zhang Heng + Zhuge Liang*) to critique an architecture, experimental setup, debugging plan, or strategic roadmap.
  - **Worker Mode (Execute for Host):** Hand the keyboard to a single persona (e.g., *Claude Shannon*, *Qian Xuesen*, or *Kelly Johnson*) to directly write code, build a minimal verification script, design a closed-loop controller, or draft technical documentation.
- **200 Textbook Canon Figures:** Focused strictly on time-tested scientific, mathematical, engineering, diagnostic, and classical strategic methodologies—no buzzwords, no cargo-cult templates.

---

## The 10 Domains (200 Personas)

| # | Domain Directory | Count | Canonical Textbook Figures & Methodologies |
| :--- | :--- | :---: | :--- |
| **01** | `01_physics_cosmology` | 20 | **Newton**, **Einstein**, **Maxwell**, **Faraday**, **Galileo**, **Feynman** (*FirstPrinciples*), **Bohr**, **Planck**, **Curie**, **Schrödinger**, **Heisenberg**, **Dirac**, **Fermi**, **Boltzmann**, **Huygens**, **Kepler**, **Copernicus**, **Rutherford**, **Chandrasekhar**, **Chien-Shiung Wu** |
| **02** | `02_mathematics_logic` | 20 | **Euclid**, **Archimedes**, **Gauss**, **Euler**, **Turing**, **Gödel**, **Noether**, **Riemann**, **Fermat**, **Pascal**, **Leibniz**, **Descartes**, **Ramanujan**, **Hilbert**, **Poincaré**, **Al-Khwarizmi**, **Zu Chongzhi**, **Liu Hui**, **Ada Lovelace**, **George Boole** |
| **03** | `03_computer_info_systems` | 20 | **Shannon** (*InformationEntropy*), **von Neumann**, **Knuth**, **Dijkstra**, **Grace Hopper**, **Wiener**, **Qian Xuesen** (*EngineeringCybernetics*), **Ritchie**, **Thompson**, **Torvalds**, **Berners-Lee**, **Vint Cerf**, **Barbara Liskov**, **Lamport**, **McCarthy**, **Minsky**, **Judea Pearl**, **Lotfi Zadeh**, **Hamming**, **Ivan Sutherland** |
| **04** | `04_engineering_inventors` | 20 | **Da Vinci**, **Tesla**, **James Watt**, **Zhang Heng** (*InstrumentTheInvisible*), **Kelly Johnson** (*SkunkWorksLean*), **Edison**, **Wright Brothers**, **Marconi**, **Bell**, **Brunel**, **Eiffel**, **Bi Sheng**, **Cai Lun**, **Li Bing**, **Ma Jun**, **Lu Ban**, **Babbage**, **Karl Benz**, **Robert Goddard**, **Morris Chang** |
| **05** | `05_chemistry_materials` | 20 | **Lavoisier**, **Mendeleev**, **Pauling**, **Boyle**, **Berzelius**, **Wöhler**, **Liebig**, **Arrhenius**, **Gibbs**, **Haber**, **Dorothy Hodgkin**, **G.N. Lewis**, **Humphry Davy**, **Michael Polanyi**, **Seaborg**, **Ahmed Zewail**, **Dalton**, **Avogadro**, **Nobel**, **Hou Debang** |
| **06** | `06_biology_medicine` | 20 | **Hippocrates**, **Zhang Zhongjing** (*PatternDifferentiation*), **Darwin**, **Pasteur**, **Mendel**, **Claude Bernard**, **William Harvey**, **Vesalius**, **Ibn Sina**, **Li Shizhen**, **Hua Tuo**, **Sun Simiao**, **Robert Koch**, **Fleming**, **Rosalind Franklin**, **Barbara McClintock**, **Tu Youyou**, **Ramón y Cajal**, **Jenner**, **Jonas Salk** |
| **07** | `07_classical_philosophy` | 20 | **Socrates**, **Plato**, **Aristotle**, **Confucius**, **Mencius**, **Laozi**, **Zhuangzi** (*FreeWandering*), **Mozi**, **Xunzi**, **Wang Yangming**, **Kant**, **Spinoza**, **Hume**, **Locke**, **Francis Bacon**, **Karl Popper**, **Thomas Kuhn**, **Epictetus**, **Seneca**, **Nagarjuna** |
| **08** | `08_strategy_statecraft` | 20 | **Sun Tzu**, **Zhuge Liang** (*LongzhongPreparation*), **Marcus Aurelius**, **Pericles**, **Cicero**, **Benjamin Franklin**, **Washington**, **Lincoln**, **Li Shimin**, **Fan Zhongyan**, **Wang Anshi**, **Su Qin**, **Kautilya**, **Scipio Africanus**, **Clausewitz**, **Hugo Grotius**, **Montesquieu**, **Alexander Hamilton**, **Florence Nightingale**, **Taiichi Ohno** |
| **09** | `09_economics_sociology` | 20 | **Adam Smith**, **Keynes**, **Ibn Khaldun**, **Herbert Simon**, **Schumpeter**, **Ricardo**, **Walras**, **Pareto**, **Ronald Coase**, **Elinor Ostrom**, **Kenneth Arrow**, **Kahneman**, **Tversky**, **Max Weber**, **Guan Zhong**, **Sima Qian**, **Luca Pacioli**, **Fernand Braudel**, **W. Edwards Deming**, **Peter Drucker** |
| **10** | `10_literature_arts_design` | 20 | **Homer**, **Shakespeare**, **Dante**, **Goethe**, **Su Shi**, **Li Bai**, **Du Fu**, **Sima Guang**, **Cao Xueqin**, **Lu Xun**, **Tolstoy**, **Dostoevsky**, **Cervantes**, **Tagore**, **Murasaki Shikibu**, **Walter Gropius**, **Buckminster Fuller**, **Vitruvius**, **Song Yingxing**, **Shen Kuo** |

---

## Quickstart (One-Time Install)

### macOS / Linux / Git Bash
```bash
git clone https://github.com/taylorguo23/greatest_persons_agent.git
cd greatest_persons_agent
chmod +x scripts/install.sh
./scripts/install.sh
```

### Windows (PowerShell)
```powershell
git clone https://github.com/taylorguo23/greatest_persons_agent.git
cd greatest_persons_agent
python scripts/build_200_personas.py
cmd /c mklink /J "$HOME\.claude\skills\greatest-persons" "$PWD"
cmd /c mklink /J "$HOME\.gemini\config\skills\greatest-persons" "$PWD"
```

---

## Usage (Agent Prompts & CLI)

### 1. In Your AI Agent Chat
Once installed as a skill, trigger **Council Mode** or **Worker Mode** directly in natural language:

- **Council Mode (Multi-Perspective Critique & Synthesis):**
  > `council: review our distributed sensor pipeline for silent data drops and feedback instability`
- **Worker Mode (Direct Execution by a Specific Figure):**
  > `worker richard_feynman: write a minimal 30-line toy model script to falsify our retry-loop race condition hypothesis`
  > `worker claude_shannon: strip this bloated event schema down to its minimum entropy representation`
  > `worker qian_xuesen: design a closed-loop disturbance-rejection controller for this noisy actuator`

### 2. Via the CLI Orchestrator (`scripts/orchestrator.py`)
```bash
# List all 200 registered textbook personas
python3 scripts/orchestrator.py --mode list

# Search personas by keyword, tag, or domain
python3 scripts/orchestrator.py --mode search --task "sensor"

# Convene a 3-person cross-domain Council for a complex engineering problem
python3 scripts/orchestrator.py --mode council --task "verify sensor calibration and reduce system complexity" --top-k 3

# Load a single persona playbook for Worker Mode execution
python3 scripts/orchestrator.py --mode worker --persona richard_feynman
```

---

## Repository Structure

```text
greatest-persons/
├── README.md                  # Documentation & usage guide
├── LICENSE                    # MIT License
├── skill.yaml                 # Skill metadata manifest
├── SKILL.md                   # Single-gateway skill instructions for AI agents
├── config/
│   └── registry.json          # Unified index of all 200 personas, tags, and paths
├── personas/
│   ├── 01_physics_cosmology/
│   ├── 02_mathematics_logic/
│   ├── 03_computer_info_systems/
│   ├── 04_engineering_inventors/
│   ├── 05_chemistry_materials/
│   ├── 06_biology_medicine/
│   ├── 07_classical_philosophy/
│   ├── 08_strategy_statecraft/
│   ├── 09_economics_sociology/
│   └── 10_literature_arts_design/
└── scripts/
    ├── build_200_personas.py  # Generates all 200 playbooks & config/registry.json
    ├── orchestrator.py        # Runtime CLI for list, search, council, and worker modes
    └── install.sh             # One-time single-skill installer
```

---

## License

Released under the [MIT License](LICENSE).
