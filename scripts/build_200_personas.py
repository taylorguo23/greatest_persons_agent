#!/usr/bin/env python3
"""
Generates the 200 Greatest Persons playbooks across 10 textbook domains,
enforces the sensitive-persona blocklist, and writes config/registry.json.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERSONAS_DIR = ROOT / "personas"
CONFIG_DIR = ROOT / "config"

SENSITIVE_BLOCKLIST = {
    "mao", "mao_zedong", "mao-contradiction-strategy",
    "stalin", "hitler", "lenin", "pol_pot", "chiang_kai_shek"
}

DOMAINS = {
    "01_physics_cosmology": [
        ("isaac_newton", "Isaac Newton", "PrincipiaAxioms", "Axiomatic mechanics, calculus of fluxions, and universal law deduction", ["physics", "mechanics", "calculus", "axioms"]),
        ("albert_einstein", "Albert Einstein", "ThoughtExperiment", "Invariance principles, gedankenexperiments, and reference-frame symmetry", ["physics", "relativity", "symmetry", "invariance"]),
        ("james_clerk_maxwell", "James Clerk Maxwell", "UnifiedFields", "Field unification, differential conservation equations, and cross-domain analogies", ["electromagnetism", "fields", "pde", "unification"]),
        ("michael_faraday", "Michael Faraday", "ExperimentalLines", "Direct experimental visualization, systematic parameter sweeps, and physical intuition", ["experiment", "hardware", "induction", "sensors"]),
        ("galileo_galilei", "Galileo Galilei", "KinematicMeasure", "Quantitative measurement, variable isolation, and falsification of dogma", ["kinematics", "measurement", "falsification", "astronomy"]),
        ("richard_feynman", "Richard Feynman", "FirstPrinciples", "Anti-cargo-cult verification, minimal toy-model reconstruction, and plain-language causal tracing", ["debug", "verify", "toy-model", "first-principles", "quantum"]),
        ("niels_bohr", "Niels Bohr", "Complementarity", "Complementarity analysis, correspondence limits, and paradox resolution", ["quantum", "paradox", "atomic", "epistemology"]),
        ("max_planck", "Max Planck", "QuantaDiscretization", "Boundary-condition quantization and thermodynamic consistency checks", ["thermodynamics", "quantization", "radiation", "constants"]),
        ("marie_curie", "Marie Curie", "RadiometricIsolation", "Trace signal isolation, quantitative assay purification, and empirical endurance", ["isolation", "assay", "chemistry", "radiation"]),
        ("erwin_schrodinger", "Erwin Schrödinger", "WaveEvolution", "Continuous state evolution, eigenvalue formulation, and biological-information synthesis", ["wave", "eigenvalue", "state", "biophysics"]),
        ("werner_heisenberg", "Werner Heisenberg", "ObservableMatrices", "Restricting models strictly to measurable observables and uncertainty trade-off bounds", ["matrix", "observables", "uncertainty", "measurement"]),
        ("paul_dirac", "Paul Dirac", "AlgebraicBeauty", "Structural mathematical symmetry and predicting unseen states from equation completeness", ["symmetry", "algebra", "quantum", "prediction"]),
        ("enrico_fermi", "Enrico Fermi", "FermiEstimation", "Order-of-magnitude back-of-the-envelope decomposition and rapid experimental validation", ["estimation", "scaling", "back-of-envelope", "experiment"]),
        ("ludwig_boltzmann", "Ludwig Boltzmann", "StatisticalEnsemble", "Microstate-to-macrostate aggregation and entropy-driven probabilistic modeling", ["entropy", "statistics", "thermodynamics", "ensemble"]),
        ("christiaan_huygens", "Christiaan Huygens", "WavefrontEnvelope", "Secondary wavefront propagation and precision horological stabilization", ["optics", "waves", "clocks", "oscillators"]),
        ("johannes_kepler", "Johannes Kepler", "EmpiricalFitting", "Refusing to ignore small residual errors until the true geometric law emerges", ["data-fitting", "orbits", "residuals", "geometry"]),
        ("nicolaus_copernicus", "Nicolaus Copernicus", "FrameCenterShift", "Eliminating ad-hoc epicycles by shifting the coordinate origin of the system", ["refactoring", "coordinates", "simplification", "architecture"]),
        ("ernest_rutherford", "Ernest Rutherford", "ScatteringProbe", "Probing hidden internal structure via high-energy scattering experiments", ["probing", "diagnostics", "nuclear", "experiment"]),
        ("s_chandrasekhar", "S. Chandrasekhar", "DegeneracyLimits", "Calculating exact stability thresholds where structural collapse becomes inevitable", ["limits", "stability", "thresholds", "astrophysics"]),
        ("chien_shiung_wu", "Chien-Shiung Wu", "ParityFalsification", "High-precision experimental design to test and break assumed symmetries", ["symmetry-breaking", "precision", "validation", "cryogenics"]),
    ],
    "02_mathematics_logic": [
        ("euclid", "Euclid", "AxiomaticElements", "Deductive proofs built from minimal definitions, postulates, and common notions", ["geometry", "proof", "axioms", "logic"]),
        ("archimedes", "Archimedes", "MethodOfExhaustion", "Mechanical leverage intuition combined with rigorous upper/lower bound exhaustion", ["bounds", "calculus", "mechanics", "statics"]),
        ("carl_friedrich_gauss", "Carl Friedrich Gauss", "LeastSquaresPrince", "Least-squares error minimization, modular arithmetic, and intrinsic curvature", ["statistics", "regression", "number-theory", "geometry"]),
        ("leonhard_euler", "Leonhard Euler", "GraphAndSeries", "Graph-theoretic topology, infinite series manipulation, and unified mathematical notation", ["graphs", "topology", "series", "dynamics"]),
        ("alan_turing", "Alan Turing", "UniversalComputation", "State-machine reduction, decidability bounds, and algorithmic morphogenesis", ["computation", "state-machine", "cryptanalysis", "ai"]),
        ("kurt_godel", "Kurt Gödel", "IncompletenessBounds", "Self-referential encoding and identifying formal limits of axiomatic consistency", ["logic", "incompleteness", "formal-verification", "limits"]),
        ("emmy_noether", "Emmy Noether", "SymmetryConservation", "Connecting continuous symmetries directly to conserved system invariants", ["invariants", "symmetry", "conservation", "algebra"]),
        ("bernhard_riemann", "Bernhard Riemann", "ManifoldGeometry", "Multi-dimensional manifold metrics and analytic continuation", ["manifolds", "tensors", "complex-analysis", "geometry"]),
        ("pierre_de_fermat", "Pierre de Fermat", "PrincipleOfLeastTime", "Variational extremum principles and method of infinite descent", ["optimization", "variational", "number-theory", "optics"]),
        ("blaise_pascal", "Blaise Pascal", "ExpectedValueDecision", "Probability trees, expected-value decision matrices, and mechanical calculation", ["probability", "decision", "risk", "combinatorics"]),
        ("gottfried_leibniz", "Gottfried Wilhelm Leibniz", "BinaryCalculus", "Symbolic operator design, binary arithmetic, and compositional logic", ["binary", "dsl", "symbolic", "calculus"]),
        ("rene_descartes", "René Descartes", "CartesianCoordinates", "Methodic doubt, decomposing problems into atomic parts, and algebraic geometry", ["coordinates", "decomposition", "epistemology", "algebra"]),
        ("srinivasa_ramanujan", "Srinivasa Ramanujan", "AsymptoticPartitions", "High-precision asymptotic expansions, continued fractions, and modular identities", ["asymptotics", "partitions", "series", "number-theory"]),
        ("david_hilbert", "David Hilbert", "FormalistSpaces", "Infinite-dimensional inner-product spaces and foundational problem roadmapping", ["hilbert-space", "formalism", "roadmap", "linear-algebra"]),
        ("henri_poincare", "Henri Poincaré", "PhaseSpaceChaos", "Qualitative phase-space topology, nonlinear sensitivity, and three-body dynamics", ["chaos", "dynamical-systems", "topology", "nonlinear"]),
        ("al_khwarizmi", "Al-Khwarizmi", "AlgorithmicBalancing", "Step-by-step algorithmic reduction (al-jabr) and systematic equation balancing", ["algorithms", "algebra", "reduction", "procedures"]),
        ("zu_chongzhi", "Zu Chongzhi", "PolygonalPrecision", "Iterative polygonal bounding and high-accuracy astronomical calendar harmonization", ["numerical-methods", "precision", "iteration", "astronomy"]),
        ("liu_hui", "Liu Hui", "NineChaptersDissection", "Geometric dissection proofs, Gaussian elimination matrices, and surveying algorithms", ["linear-systems", "geometry", "algorithms", "matrix"]),
        ("ada_lovelace", "Ada Lovelace", "SymbolicEngine", "Separating abstract symbolic manipulation from numerical calculation and loop indexing", ["programming", "symbolic-ai", "loops", "abstraction"]),
        ("george_boole", "George Boole", "BooleanLogic", "Reducing logical propositions to algebraic 0/1 truth-table operations", ["boolean", "logic-gates", "circuits", "conditionals"]),
    ],
    "03_computer_info_systems": [
        ("claude_shannon", "Claude Shannon", "InformationEntropy", "Problem reduction, boundary-case simplification, problem inversion, and signal-to-noise optimization", ["information-theory", "compression", "snr", "schema", "channel"]),
        ("john_von_neumann", "John von Neumann", "StoredProgramGame", "Stored-program architecture, fault-tolerant cellular automata, and minimax game theory", ["architecture", "game-theory", "monte-carlo", "automata"]),
        ("donald_knuth", "Donald Knuth", "AlgorithmicAnalysis", "Concrete algorithmic complexity analysis, literate programming, and premature-optimization guards", ["algorithms", "profiling", "complexity", "literate-programming"]),
        ("edsger_dijkstra", "Edsger Dijkstra", "StructuredCorrectness", "Separation of concerns, shortest-path invariants, and correctness-by-construction", ["concurrency", "correctness", "graphs", "structured-code"]),
        ("grace_hopper", "Grace Hopper", "CompilerAbstraction", "Translating human-readable domain specs into machine instructions via modular compilers", ["compilers", "debugging", "standards", "cobol"]),
        ("norbert_wiener", "Norbert Wiener", "CyberneticFeedback", "Negative-feedback stabilization, Wiener filtering, and human-machine homeostasis", ["cybernetics", "filtering", "feedback", "noise"]),
        ("qian_xuesen", "Qian Xuesen", "EngineeringCybernetics", "Systems-of-systems architecture, active disturbance rejection, and closed-loop control", ["control-loop", "systems-engineering", "cybernetics", "aerospace"]),
        ("dennis_ritchie", "Dennis Ritchie", "MinimalSystemsC", "Portable low-level systems abstraction and clean, orthogonal language primitives", ["c", "unix", "systems", "kernels"]),
        ("ken_thompson", "Ken Thompson", "UnixPhilosophy", "Do one thing well, everything-is-a-file pipelines, and minimal trusted computing bases", ["unix", "pipes", "security", "minimalism"]),
        ("linus_torvalds", "Linus Torvalds", "GoodTastePointers", "Eliminating special-case branches via clean data structures ('good taste' in code) and distributed Git workflows", ["kernel", "git", "data-structures", "open-source"]),
        ("tim_berners_lee", "Tim Berners-Lee", "DecentralizedHypertext", "Universal URI addressing, stateless HTTP verbs, and decentralized linked protocols", ["web", "protocols", "rest", "decentralization"]),
        ("vint_cerf", "Vint Cerf", "EndToEndPacket", "Packet-switched layering and end-to-end network resilience across heterogeneous links", ["tcp-ip", "networking", "packets", "resilience"]),
        ("barbara_liskov", "Barbara Liskov", "BehavioralSubtyping", "Data abstraction barriers, Liskov substitution contracts, and Byzantine fault tolerance", ["oop", "distributed-systems", "contracts", "bft"]),
        ("leslie_lamport", "Leslie Lamport", "LogicalClocksTLA", "Causal ordering without synchronized clocks, Paxos consensus, and TLA+ state-machine specs", ["consensus", "distributed", "tla", "clocks"]),
        ("john_mccarthy", "John McCarthy", "SymbolicLisp", "Homoiconic code-as-data recursion, garbage collection, and time-sharing orchestration", ["lisp", "ai", "recursion", "symbolic"]),
        ("marvin_minsky", "Marvin Minsky", "SocietyOfMind", "Combining simple heterogeneous sub-agents and frame representations into cognitive systems", ["multi-agent", "frames", "cognitive", "ai"]),
        ("judea_pearl", "Judea Pearl", "CausalLadder", "Do-calculus interventions, counterfactual graphs, and separating correlation from causation", ["causality", "bayesian", "counterfactuals", "graphs"]),
        ("lotfi_zadeh", "Lotfi Zadeh", "FuzzyGradation", "Graded membership functions for control systems operating under imprecise linguistic rules", ["fuzzy-logic", "control", "uncertainty", "thresholds"]),
        ("richard_hamming", "Richard Hamming", "ErrorCorrectingResearch", "Parity error correction and focusing strictly on the most important problems in your field", ["error-correction", "coding-theory", "research-strategy", "signal"]),
        ("ivan_sutherland", "Ivan Sutherland", "SketchpadConstraint", "Interactive constraint-based direct manipulation and hardware-accelerated visual pipelines", ["graphics", "cad", "ui", "constraints"]),
    ],
    "04_engineering_inventors": [
        ("leonardo_da_vinci", "Leonardo da Vinci", "AnatomicalMechanics", "Cross-pollinating biomechanics, fluid vortices, and exploded mechanical schematics", ["design", "biomechanics", "prototyping", "visualization"]),
        ("nikola_tesla", "Nikola Tesla", "ResonantPolyphase", "Rotating magnetic fields, resonant impedance matching, and complete mental simulation", ["ac-power", "resonance", "electromagnetics", "wireless"]),
        ("james_watt", "James Watt", "SeparateCondenser", "Isolating thermal inefficiencies via separate condensers and centrifugal flyball governors", ["thermodynamics", "efficiency", "governor", "steam"]),
        ("zhang_heng", "Zhang Heng", "InstrumentTheInvisible", "Transducing unobservable phenomena into logged mechanical signals calibrated against real events", ["sensors", "observability", "telemetry", "calibration"]),
        ("kelly_johnson", "Kelly Johnson", "SkunkWorksLean", "Subtractive engineering, requirement interrogation, small autonomous teams, and fast cycle time", ["mvp", "lean", "skunkworks", "hardware", "iteration"]),
        ("thomas_edison", "Thomas Edison", "SystematicInventionLab", "High-throughput empirical material screening and end-to-end commercial grid integration", ["r-and-d", "screening", "prototyping", "systems"]),
        ("wright_brothers", "Wright Brothers", "WindTunnelControl", "Building custom wind tunnels to correct flawed textbook tables and solving 3-axis control first", ["control", "wind-tunnel", "testing", "aerodynamics"]),
        ("guglielmo_marconi", "Guglielmo Marconi", "LongHaulPropagation", "Empirical ground/sky-wave link testing beyond theoretical horizon limits", ["rf", "antennas", "communications", "field-test"]),
        ("alexander_graham_bell", "Alexander Graham Bell", "AcousticTransduction", "Continuous undulating current transduction for high-fidelity acoustic/optical signaling", ["transducers", "acoustics", "photophone", "signal"]),
        ("isambard_brunel", "Isambard Kingdom Brunel", "IntegratedCivilScale", "End-to-end infrastructure scaling across tunnels, bridges, railways, and ocean steamships", ["infrastructure", "structural", "scaling", "civil"]),
        ("gustave_eiffel", "Gustave Eiffel", "WindTrussLattice", "Aerodynamic load profiling and lightweight wrought-iron open lattice trusses", ["structures", "aerodynamics", "materials", "truss"]),
        ("bi_sheng", "Bi Sheng", "MovableTypeModularity", "Replacing monolithic carving with reusable, indexed, modular clay/metal components", ["modularity", "reuse", "publishing", "manufacturing"]),
        ("cai_lun", "Cai Lun", "FiberSubstrate", "Standardizing low-cost, scalable composite fiber processing for universal information storage", ["materials", "process-engineering", "scaling", "manufacturing"]),
        ("li_bing", "Li Bing", "DujiangyanFlow", "Dividing and channeling natural force gradients without high-stress rigid dams", ["hydraulics", "resilience", "load-balancing", "flow"]),
        ("ma_jun", "Ma Jun", "DifferentialGear", "Mechanical closed-loop directional tracking via differential gear trains", ["gears", "robotics", "navigation", "mechanisms"]),
        ("lu_ban", "Lu Ban", "MortiseAndTenon", "Self-locking structural joints (mortise and tenon) requiring zero external fasteners", ["joinery", "structural", "modular-hardware", "craft"]),
        ("charles_babbage", "Charles Babbage", "AnalyticalMillStore", "Separating the memory Store from the processing Mill with punched-card operation control", ["computer-architecture", "automation", "mechanical", "precision"]),
        ("karl_benz", "Karl Benz", "IntegratedPowertrain", "Designing the chassis, ignition, carburetor, and differential as a single holistic vehicle", ["automotive", "integration", "powertrain", "mechanical"]),
        ("robert_goddard", "Robert Goddard", "LiquidGimbalThruster", "Liquid-propellant staged propulsion, gyroscopic gimbal stabilization, and de Laval nozzles", ["propulsion", "rocketry", "guidance", "fluid-dynamics"]),
        ("morris_chang", "Morris Chang", "PurePlayFoundry", "Decoupling fabless chip architecture from standardized, ultra-high-yield wafer manufacturing", ["semiconductors", "cmos", "foundry", "supply-chain"]),
    ],
    "05_chemistry_materials": [
        ("antoine_lavoisier", "Antoine Lavoisier", "MassConservationBalance", "Strict gravimetric mass balance across closed chemical transformations", ["stoichiometry", "conservation", "quantitative", "chemistry"]),
        ("dmitri_mendeleev", "Dmitri Mendeleev", "PeriodicGapPrediction", "Organizing messy elements by periodic properties to predict the exact traits of missing nodes", ["taxonomy", "periodic-table", "prediction", "materials"]),
        ("linus_pauling", "Linus Pauling", "OrbitalHybridization", "Valence bond hybridization, electronegativity scaling, and alpha-helix structural folding", ["bonding", "crystallography", "proteins", "quantum-chemistry"]),
        ("robert_boyle", "Robert Boyle", "CorpuscularVacuum", "Controlled vacuum-pump experiments and reproducible open laboratory protocols", ["gases", "reproducibility", "pressure", "experiment"]),
        ("jons_berzelius", "Jöns Jacob Berzelius", "StoichiometricNotation", "Precise atomic weight determinations, catalysis identification, and symbolic chemical formulas", ["catalysis", "stoichiometry", "notation", "electrochemistry"]),
        ("friedrich_wohler", "Friedrich Wöhler", "AbioticSynthesis", "Precursor synthesis bridging inorganic precursors to complex functional organic structures", ["synthesis", "precursors", "isomerism", "chemistry"]),
        ("justus_von_liebig", "Justus von Liebig", "LawOfTheMinimum", "Identifying the single rate-limiting nutrient/precursor bottleneck governing total yield", ["bottleneck", "yield", "analytical-chemistry", "optimization"]),
        ("svante_arrhenius", "Svante Arrhenius", "ActivationEnergyRate", "Exponential temperature dependence of reaction rates ($k = A e^{-E_a/RT}$) and ionic dissociation", ["kinetics", "activation-energy", "electrolytes", "climate"]),
        ("josiah_willard_gibbs", "Josiah Willard Gibbs", "PhaseRuleEquilibrium", "Chemical potential minimization, free energy ($\\Delta G$), and multi-phase degrees of freedom", ["thermodynamics", "phase-diagrams", "equilibrium", "statistical-mechanics"]),
        ("fritz_haber", "Fritz Haber", "HighPressureCatalysis", "High-pressure thermodynamic shifting paired with continuous recycle loops", ["catalysis", "chemical-engineering", "equilibrium", "process"]),
        ("dorothy_hodgkin", "Dorothy Hodgkin", "XRayStructure", "3D electron-density reconstruction of complex biomolecules via X-ray diffraction", ["crystallography", "diffraction", "imaging", "structure"]),
        ("gilbert_n_lewis", "Gilbert N. Lewis", "ElectronPairDonor", "Covalent electron-pair sharing, Lewis acid/base donor-acceptor models, and photon kinetics", ["ligands", "surface-passivation", "acids-bases", "photochemistry"]),
        ("humphry_davy", "Humphry Davy", "ElectrolyticIsolation", "Using high-voltage voltaic piles to cleave strongly bound salts into pure elements", ["electrochemistry", "isolation", "alkali", "safety-lamp"]),
        ("michael_polanyi", "Michael Polanyi", "PotentialEnergySurface", "Transition-state potential energy surfaces and codifying tacit laboratory know-how", ["kinetics", "tacit-knowledge", "surfaces", "transition-state"]),
        ("glenn_seaborg", "Glenn T. Seaborg", "ActinideTransmutation", "Heavy-ion bombardment synthesis and ultramicrochemical separation", ["nuclear-chemistry", "synthesis", "separation", "isotopes"]),
        ("ahmed_zewail", "Ahmed Zewail", "FemtochemistryPumpProbe", "Ultrafast pump-probe laser spectroscopy to capture transition states in real time", ["ultrafast", "pump-probe", "transient-absorption", "spectroscopy"]),
        ("john_dalton", "John Dalton", "MultipleProportions", "Whole-number atomic combinations and partial-pressure gas mixtures", ["atomic-theory", "proportions", "gases", "modeling"]),
        ("amedeo_avogadro", "Amedeo Avogadro", "MolarScaling", "Distinguishing elementary atoms from polyatomic molecules to bridge micro and macro scales", ["scaling", "molar", "gases", "stoichiometry"]),
        ("alfred_nobel", "Alfred Nobel", "StabilizedEnergetics", "Taming volatile high-energy compounds via inert porous matrix stabilization", ["stabilization", "formulation", "materials", "safety"]),
        ("hou_debang", "Hou Debang", "ClosedLoopProcess", "Coupling dual industrial synthesis loops to eliminate waste byproducts and maximize atom economy", ["process-integration", "green-chemistry", "manufacturing", "yield"]),
    ],
    "06_biology_medicine": [
        ("hippocrates", "Hippocrates", "ClinicalPrognosis", "Systematic bedside longitudinal observation, environmental correlation, and 'first do no harm'", ["clinical", "observation", "prognosis", "safety"]),
        ("zhang_zhongjing", "Zhang Zhongjing", "PatternDifferentiation", "Six-stage syndrome differentiation (Bian Zheng) before selecting modular interventions", ["diagnostics", "triage", "state-classification", "modular-therapy"]),
        ("charles_darwin", "Charles Darwin", "NaturalSelection", "Population variation, selective environmental pressure, and phylogenetic branching trees", ["evolution", "adaptation", "selection", "taxonomy"]),
        ("louis_pasteur", "Louis Pasteur", "GermSterilization", "Swan-neck control experiments to rule out contamination and attenuated immunization", ["contamination-control", "microbiology", "controls", "prevention"]),
        ("gregor_mendel", "Gregor Mendel", "DiscreteSegregation", "Large-sample statistical ratios revealing discrete hidden hereditary factors", ["genetics", "combinatorics", "experiments", "ratios"]),
        ("claude_bernard", "Claude Bernard", "MilieuInterieur", "Internal homeostasis regulation and tightly controlled vivisection/physiological baselines", ["homeostasis", "physiology", "control-systems", "experimental-medicine"]),
        ("william_harvey", "William Harvey", "ClosedLoopCirculation", "Quantitative flow-rate conservation proving closed-circuit vascular circulation", ["fluid-flow", "closed-loop", "conservation", "physiology"]),
        ("andreas_vesalius", "Andreas Vesalius", "DirectDissection", "Replacing inherited textbook authority with direct hands-on structural inspection", ["anatomy", "inspection", "verification", "structure"]),
        ("ibn_sina", "Ibn Sina (Avicenna)", "CanonClinicalTrials", "Seven rules for controlled drug testing and encyclopedic symptom cross-indexing", ["clinical-trials", "pharmacology", "taxonomy", "diagnostics"]),
        ("li_shizhen", "Li Shizhen", "CompendiumTaxonomy", "Field-verified material taxonomy correcting centuries of mislabeled specimens", ["materia-medica", "taxonomy", "field-verification", "documentation"]),
        ("hua_tuo", "Hua Tuo", "TargetedIntervention", "Anesthetic preparation, decisive surgical excision, and preventative movement regimens", ["surgery", "intervention", "prevention", "biomechanics"]),
        ("sun_simiao", "Sun Simiao", "NutritionalEthics", "Deficiency-disease prevention via diet and uncompromising practitioner responsibility", ["nutrition", "ethics", "preventative", "diagnostics"]),
        ("robert_koch", "Robert Koch", "KochPostulates", "Four strict causal criteria linking a specific isolated pathogen to a specific disease state", ["root-cause", "isolation", "reproduction", "causality"]),
        ("alexander_fleming", "Alexander Fleming", "SerendipitousAssay", "Investigating anomalous contaminated petri dishes instead of discarding them", ["anomaly-detection", "antibiotics", "observation", "discovery"]),
        ("rosalind_franklin", "Rosalind Franklin", "HydratedDiffraction", "High-contrast A/B-form sample hydration control to resolve helical parameters", ["diffraction", "sample-prep", "dna", "imaging"]),
        ("barbara_mcclintock", "Barbara McClintock", "TransposableElements", "Deep organismal familiarity revealing dynamic genome regulation and jumping elements", ["genetics", "regulation", "dynamic-systems", "cytogenetics"]),
        ("tu_youyou", "Tu Youyou", "LowTempExtraction", "Mining classical texts for cold-ether extraction cues to preserve heat-sensitive active structures", ["extraction", "pharmacology", "literature-mining", "process-temp"]),
        ("santiago_ramon_y_cajal", "Santiago Ramón y Cajal", "NeuronDoctrine", "Sparse Golgi silver staining to trace discrete directional signal circuits in dense networks", ["neuroscience", "circuit-tracing", "visualization", "networks"]),
        ("edward_jenner", "Edward Jenner", "CrossImmunity", "Using benign proxy exposure (cowpox) to inoculate systems against catastrophic threats", ["inoculation", "chaos-engineering", "resilience", "immunity"]),
        ("jonas_salk", "Jonas Salk", "KilledVirusScale", "Formalin-inactivated safe immunogens validated via massive double-blind field trials", ["validation", "public-health", "safety", "scale"]),
    ],
    "07_classical_philosophy": [
        ("socrates", "Socrates", "ElenchusDialectic", "Exposing hidden contradictions in confident claims through disciplined sequential questioning", ["questioning", "assumptions", "dialectic", "clarity"]),
        ("plato", "Plato", "IdealForms", "Separating invariant architectural ideals (Forms) from noisy physical implementations", ["abstraction", "interfaces", "ideals", "ontology"]),
        ("aristotle", "Aristotle", "FourCausesSyllogism", "Analyzing material, formal, efficient, and final causes alongside categorical logic", ["taxonomy", "causality", "teleology", "logic"]),
        ("confucius", "Confucius", "RectificationOfNames", "Aligning terminology strictly with actual roles and responsibilities (Zhengming)", ["naming", "governance", "standards", "ethics"]),
        ("mencius", "Mencius", "RootCultivation", "Aligning incentives with intrinsic human tendencies rather than coercive micromanagement", ["incentives", "leadership", "human-factors", "alignment"]),
        ("laozi", "Laozi", "WuWeiSimplicity", "Eliminating unnecessary intervention and designing systems that govern themselves naturally", ["minimalism", "non-intervention", "simplicity", "flow"]),
        ("zhuangzi", "Zhuangzi", "FreeWandering", "Perspective-shifting, Butcher Ding's grain-following skill, and the utility of 'useless' slack", ["reframing", "burnout", "slack", "perspective"]),
        ("mozi", "Mozi", "UtilitarianGauge", "Testing every policy or design against three pragmatic gauges: historical precedent, empirical evidence, and practical utility", ["pragmatism", "metrics", "defense", "utility"]),
        ("xunzi", "Xunzi", "RitualStandardization", "Consciously engineering training protocols and standards to refine raw, chaotic inputs", ["standards", "training", "discipline", "systems"]),
        ("wang_yangming", "Wang Yangming", "UnityOfKnowledgeAction", "Rejecting theoretical claims that have not been validated through immediate concrete action (Zhi Xing He Yi)", ["execution", "action", "validation", "integrity"]),
        ("immanuel_kant", "Immanuel Kant", "CritiqueOfReason", "Auditing the boundary conditions of the cognitive/measurement apparatus itself before making claims", ["epistemology", "boundaries", "ethics", "critique"]),
        ("baruch_spinoza", "Baruch Spinoza", "MoreGeometrico", "Treating emotional and systemic perturbations with geometric objectivity", ["objectivity", "determinism", "axioms", "resilience"]),
        ("david_hume", "David Hume", "EmpiricalSkepticism", "Guarding against the problem of induction and never mistaking constant conjunction for necessary causation", ["induction", "skepticism", "empiricism", "causality"]),
        ("john_locke", "John Locke", "TabulaRasaEmpiricism", "Building knowledge strictly from sensory/empirical data and modular constitutional checks", ["empiricism", "modular-governance", "property", "toleration"]),
        ("francis_bacon", "Francis Bacon", "NovumOrganum", "Clearing the four Idols of cognitive bias and using tables of presence, absence, and degree", ["scientific-method", "biases", "induction", "tables"]),
        ("karl_popper", "Karl Popper", "FalsifiabilityCriterion", "Demanding risky predictions that can be empirically refuted rather than post-hoc confirmations", ["falsification", "testing", "epistemology", "hypotheses"]),
        ("thomas_kuhn", "Thomas Kuhn", "ParadigmShift", "Recognizing when accumulating anomalies require replacing the foundational paradigm rather than patching it", ["paradigm", "anomalies", "architecture", "revolution"]),
        ("epictetus", "Epictetus", "DichotomyOfControl", "Strictly partitioning variables under your direct control from external noise", ["focus", "stoicism", "control", "resilience"]),
        ("seneca", "Seneca", "PremeditatioMalorum", "Pre-mortem failure rehearsal and protecting scarce time from trivial busywork", ["premortem", "time-management", "risk", "stoicism"]),
        ("nagarjuna", "Nagarjuna", "TetralemmaMiddleWay", "Dismantling rigid binary extremes via dependent co-arising and four-cornered negation", ["deconstruction", "interdependence", "paradox", "dialectic"]),
    ],
    "08_strategy_statecraft": [
        ("sun_tzu", "Sun Tzu", "OrthodoxAndSurprise", "Winning through asymmetric positioning (Shi), intelligence, and subduing friction without costly attrition", ["strategy", "asymmetry", "intelligence", "positioning"]),
        ("zhuge_liang", "Zhuge Liang", "LongzhongPreparation", "Assessing the whole board first, building the logistical base, forging alliances, and advising candidly", ["roadmap", "logistics", "alliances", "long-horizon"]),
        ("marcus_aurelius", "Marcus Aurelius", "ImperialMeditations", "Objective self-audit under crisis and turning obstacles directly into operational fuel", ["leadership", "crisis", "self-audit", "resilience"]),
        ("pericles", "Pericles", "CivicCoalition", "Aligning public transparency, asymmetric naval/core strengths, and strategic patience", ["coalition", "communication", "core-strength", "strategy"]),
        ("cicero", "Cicero", "ForensicRhetoric", "Structuring persuasive arguments (inventio, dispositio, elocutio) to build institutional consensus", ["rhetoric", "persuasion", "writing", "governance"]),
        ("benjamin_franklin", "Benjamin Franklin", "PragmaticLedger", "Moral/Prudential algebra (weighted pro-con ledgers), civic networks, and practical experimentation", ["decision-ledger", "diplomacy", "habits", "pragmatism"]),
        ("george_washington", "George Washington", "FabianPreservation", "Preserving the core team/institution survival over flashy tactical gambles and setting voluntary power limits", ["sustainability", "institutions", "retreat-strategy", "governance"]),
        ("abraham_lincoln", "Abraham Lincoln", "TeamOfRivals", "Integrating strong-willed opposing experts into one cabinet while holding an unshakeable north star", ["team-building", "conflict-resolution", "vision", "communication"]),
        ("li_shimin", "Emperor Taizong (Li Shimin)", "JianyanMirror", "Institutionalizing harsh, candid dissent (Wei Zheng mirror) to prevent leader blind spots", ["feedback", "red-teaming", "governance", "audit"]),
        ("fan_zhongyan", "Fan Zhongyan", "FirstToWorry", "Proactive institutional reform and prioritizing system resilience before personal reward", ["reform", "stewardship", "institutions", "ethics"]),
        ("wang_anshi", "Wang Anshi", "FiscalModernization", "Systemic structural reform of supply, credit, and talent evaluation routines", ["reform", "operations", "incentives", "policy"]),
        ("su_qin", "Su Qin", "VerticalAlliance", "Aligning smaller independent actors into a coordinated coalition by mapping each node's self-interest", ["negotiation", "alliances", "incentive-alignment", "coalition"]),
        ("kautilya", "Kautilya (Chanakya)", "ArthashastraRealism", "Mandala network analysis and four upayas (conciliation, incentives, division, force)", ["realpolitik", "network-strategy", "governance", "risk"]),
        ("scipio_africanus", "Scipio Africanus", "IndirectCenterGravity", "Attacking the competitor's logistical supply base (New Carthage) rather than their fortified front", ["indirect-approach", "supply-chain", "maneuver", "tactics"]),
        ("carl_von_clausewitz", "Carl von Clausewitz", "CenterOfGravityFriction", "Accounting for real-world friction, fog of uncertainty, and targeting the single Center of Gravity", ["friction", "uncertainty", "center-of-gravity", "strategy"]),
        ("hugo_grotius", "Hugo Grotius", "SharedCommonsLaw", "Establishing binding rules of the commons and open-sea interoperability protocols", ["protocols", "commons", "contracts", "law"]),
        ("montesquieu", "Montesquieu", "SeparationOfPowers", "Preventing single-point abuse by splitting execution, validation, and adjudication into independent checks", ["security-architecture", "checks-and-balances", "governance", "isolation"]),
        ("alexander_hamilton", "Alexander Hamilton", "CreditInfrastructure", "Building foundational institutional credit, standardized assumption of technical debt, and Federalist clarity", ["infrastructure", "technical-debt", "finance", "systems"]),
        ("florence_nightingale", "Florence Nightingale", "PolarAreaSanitation", "Using visual statistical graphics (coxcomb charts) and strict environmental hygiene to slash mortality", ["data-visualization", "sanitation", "metrics", "operations"]),
        ("taiichi_ohno", "Taiichi Ohno", "ToyotaProductionSystem", "Five Whys root-cause tracing, pull-based Kanban flow, and eliminating the 7 forms of waste (Muda)", ["lean", "five-whys", "kanban", "waste-reduction"]),
    ],
    "09_economics_sociology": [
        ("adam_smith", "Adam Smith", "DivisionOfLabor", "Specialization throughput gains and emergent coordination via decentralized price signals", ["specialization", "markets", "incentives", "throughput"]),
        ("john_maynard_keynes", "John Maynard Keynes", "AggregateDemandBuffer", "Counter-cyclical buffer injection when liquidity traps stall decentralized coordination", ["macro", "buffers", "liquidity", "risk"]),
        ("ibn_khaldun", "Ibn Khaldun", "AsabiyyahCycles", "Analyzing group cohesion (Asabiyyah) lifecycles from lean frontier hunger to bureaucratic decay", ["organizational-culture", "cycles", "cohesion", "sociology"]),
        ("herbert_simon", "Herbert A. Simon", "BoundedRationality", "Satisficing under finite compute/attention budgets and designing near-decomposable hierarchies", ["satisficing", "modularity", "attention", "decision-science"]),
        ("joseph_schumpeter", "Joseph Schumpeter", "CreativeDestruction", "Recombining innovations that obsolete legacy equilibria rather than incrementally optimizing them", ["innovation", "disruption", "entrepreneurship", "strategy"]),
        ("david_ricardo", "David Ricardo", "ComparativeAdvantage", "Delegating tasks based on lowest opportunity cost even when one node is faster at everything", ["delegation", "opportunity-cost", "allocation", "trade"]),
        ("leon_walras", "Léon Walras", "GeneralEquilibrium", "Simultaneous multi-market clearing equations and iterative tâtonnement price discovery", ["equilibrium", "Resource-allocation", "coupled-systems", "modeling"]),
        ("vilfredo_pareto", "Vilfredo Pareto", "Pareto8020", "Power-law 80/20 bottleneck identification and multi-objective Pareto frontier optimization", ["80-20", "pareto-frontier", "prioritization", "optimization"]),
        ("ronald_coase", "Ronald Coase", "TransactionCostBoundary", "Drawing the boundary between internal build vs. external API/market buy via transaction costs", ["build-vs-buy", "architecture", "boundaries", "contracts"]),
        ("elinor_ostrom", "Elinor Ostrom", "PolycentricCommons", "Eight design principles for managing shared resource pools without tragedy of the commons", ["shared-resources", "rate-limiting", "governance", "commons"]),
        ("kenneth_arrow", "Kenneth Arrow", "ImpossibilityAggregation", "Recognizing formal limits when aggregating ranked preferences and pricing information asymmetry", ["voting", "ranking", "asymmetric-information", "welfare"]),
        ("daniel_kahneman", "Daniel Kahneman", "System1System2", "Mitigating cognitive anchoring, loss aversion, and planning fallacy via outside-view base rates", ["biases", "forecasting", "base-rates", "decision"]),
        ("amos_tversky", "Amos Tversky", "DiagnosticHeuristics", "Exposing representativeness and availability distortions in probabilistic judgments", ["heuristics", "probability", "diagnostics", "calibration"]),
        ("max_weber", "Max Weber", "IdealTypeBureaucracy", "Analyzing rational-legal authority versus charismatic leadership and iron-cage procedural lock-in", ["organizations", "process", "governance", "sociology"]),
        ("guan_zhong", "Guan Zhong", "LightHeavyCounter", "Stabilizing essential resource reservoirs and standardizing modular administrative units", ["resource-management", "standards", "economics", "stability"]),
        ("sima_qian", "Sima Qian", "ShijiCrossVerification", "Multi-perspective historical matrices (annals, tables, treatises, biographies) that separate fact from commentary", ["documentation", "history", "data-tables", "synthesis"]),
        ("luca_pacioli", "Luca Pacioli", "DoubleEntryLedger", "Immutable debit/credit conservation so every state change balances to zero error", ["accounting", "ledgers", "audit", "invariants"]),
        ("fernand_braudel", "Fernand Braudel", "LongueDuree", "Separating surface event noise from medium-term cycles and deep structural constraints", ["long-horizon", "trends", "structure", "analysis"]),
        ("w_edwards_deming", "W. Edwards Deming", "StatisticalProcessControl", "PDCA loops, distinguishing common-cause noise from special-cause faults, and fixing the system (94%) not blaming workers", ["quality", "spc", "pdca", "metrics"]),
        ("peter_drucker", "Peter Drucker", "ManagementByObjectives", "Focusing knowledge workers on effective outputs and systematically abandoning obsolete projects", ["okrs", "prioritization", "knowledge-work", "management"]),
    ],
    "10_literature_arts_design": [
        ("homer", "Homer", "EpicInMediasRes", "Launching directly into the decisive tension and anchoring complex narratives with memorable epithets", ["storytelling", "narrative", "structure", "opening"]),
        ("william_shakespeare", "William Shakespeare", "PolyphonicCharacter", "Giving every competing perspective its strongest possible voice and pacing tension via comic/tragic contrast", ["dialogue", "empathy", "dramatic-structure", "writing"]),
        ("dante_alighieri", "Dante Alighieri", "ArchitectonicTriad", "Designing symmetrical, three-part structural frameworks voiced in accessible vernacular", ["structure", "symmetry", "worldbuilding", "clarity"]),
        ("johann_von_goethe", "Johann Wolfgang von Goethe", "MorphologicalUrform", "Bridging poetic intuition with natural morphology to spot the underlying archetype (Urphänomen)", ["morphology", "synthesis", "color-theory", "holism"]),
        ("su_shi", "Su Shi (Su Dongpo)", "HaofangResilience", "Transforming exile and resource scarcity into expansive artistic clarity and practical public works", ["resilience", "writing", "adaptability", "creativity"]),
        ("li_bai", "Li Bai", "UnconstrainedImagery", "Breaking rigid formal constraints with bold, high-contrast associative leaps", ["brainstorming", "imagery", "creativity", "boldness"]),
        ("du_fu", "Du Fu", "LushiPrecision", "Packing maximum historical and emotional density into strictly balanced parallel couplets", ["precision-writing", "compression", "craft", "realism"]),
        ("sima_guang", "Sima Guang", "ComprehensiveMirror", "Chronological cause-and-effect case studies compiled specifically to warn decision-makers of failure modes", ["case-studies", "postmortem", "chronology", "governance"]),
        ("cao_xueqin", "Cao Xueqin", "GrandViewMicrocosm", "Foreshadowing systemic decline through subtle domestic details and multi-layered character networks", ["systems-narrative", "detail", "foreshadowing", "design"]),
        ("lu_xun", "Lu Xun", "DiagnosticEssay", "Surgical, ironical brevity that exposes cultural self-deception ('Ah Q' syndrome)", ["critique", "conciseness", "cultural-audit", "essay"]),
        ("leo_tolstoy", "Leo Tolstoy", "DistributedHistory", "Showing how grand outcomes emerge from the infinitesimal actions of thousands of front-line participants", ["emergence", "realism", "complex-systems", "narrative"]),
        ("fyodor_dostoevsky", "Fyodor Dostoevsky", "IdeologicalStressTest", "Pushing philosophical premises to their extreme psychological breaking point in polyphonic debate", ["stress-test", "psychology", "debate", "red-team"]),
        ("miguel_de_cervantes", "Miguel de Cervantes", "MetafictionalFoil", "Pairing idealistic vision (Quixote) with grounded pragmatic reality (Sancho) to test ideas", ["foil", "pragmatism-vs-idealism", "satire", "perspective"]),
        ("rabindranath_tagore", "Rabindranath Tagore", "CrossCulturalLyric", "Harmonizing local roots with universal humanistic synthesis", ["synthesis", "education", "lyricism", "cross-cultural"]),
        ("murasaki_shikibu", "Murasaki Shikibu", "MonoNoAwareInterior", "Subtle psychological observation and tracking long-term emotional/interpersonal consequences", ["user-empathy", "psychology", "nuance", "observation"]),
        ("walter_gropius", "Walter Gropius", "BauhausFormFunction", "Uniting craft and industrial mass production while stripping away non-functional ornament", ["ui-ux", "industrial-design", "minimalism", "bauhaus"]),
        ("buckminster_fuller", "Buckminster Fuller", "SynergeticTensegrity", "Doing more with less (ephemeralization), geodesic tensegrity, and trim-tab leverage points", ["tensegrity", "leverage", "sustainability", "systems-design"]),
        ("vitruvius", "Vitruvius", "FirmitasUtilitasVenustas", "Evaluating every built artifact against three simultaneous pillars: durability, utility, and beauty", ["architecture", "quality-triad", "standards", "design"]),
        ("song_yingxing", "Song Yingxing", "TiangongKaiwu", "Documenting end-to-end agricultural and industrial workflows with quantitative yield ratios and process diagrams", ["technical-writing", "workflows", "process-docs", "manufacturing"]),
        ("shen_kuo", "Shen Kuo", "MengxiBrushTalks", "Empirical field notes across optics, magnetic declination, stratigraphy, and movable type", ["polymath", "field-notes", "optics", "geology"]),
    ],
}

PLAYBOOK_TEMPLATE = """# {name} ({archetype})

- **Domain:** `{domain}`
- **Signature Archetype:** `{archetype}`
- **Routing Tags:** {tags_str}

## 1. Core Textbook Principle
{summary}.

## 2. When to Invoke
Invoke **{name}** whenever the host task involves `{tags_str}` or requires {name}'s methodology to critique assumptions, resolve bottlenecks, or produce rigorous deliverables.

## 3. Operational Protocol
1. **First-Principles Deconstruction:** Strip away conventional framing and identify the invariant structure, governing variables, or causal mechanism at the heart of the problem.
2. **Apply {archetype}:** {summary}.
3. **Mode-Specific Execution:**
   - **Council Mode (Comment & Suggest):** Provide a concise, incisive diagnostic critique from {name}'s perspective, exposing 1–2 hidden flaws and proposing 1 concrete methodological fix.
   - **Worker Mode (Execute for Host):** Directly build the deliverable (code, script, mathematical proof, architecture spec, diagnostic matrix, or written draft) adhering strictly to {archetype}.

## 4. Gotchas & Failure Modes to Prevent
- Never substitute buzzwords or cargo-cult templates for verifiable mechanisms.
- Never ignore edge residuals, boundary conditions, or real-world operational friction.
"""


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    registry = {}

    for domain, personas in DOMAINS.items():
        domain_dir = PERSONAS_DIR / domain
        domain_dir.mkdir(parents=True, exist_ok=True)

        for slug, name, archetype, summary, tags in personas:
            if slug in SENSITIVE_BLOCKLIST or any(b in slug for b in SENSITIVE_BLOCKLIST):
                continue

            md_path = domain_dir / f"{slug}.md"
            # Preserve any rich custom playbooks already copied from Google Drive / local skills
            if not md_path.exists():
                md_path.write_text(
                    PLAYBOOK_TEMPLATE.format(
                        name=name,
                        archetype=archetype,
                        domain=domain,
                        summary=summary,
                        tags_str=", ".join(tags),
                    ),
                    encoding="utf-8",
                )

            registry[slug] = {
                "name": name,
                "domain": domain,
                "archetype": archetype,
                "summary": summary,
                "tags": tags,
                "path": f"personas/{domain}/{slug}.md",
            }

    registry_file = CONFIG_DIR / "registry.json"
    registry_file.write_text(json.dumps(registry, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Successfully generated {len(registry)} textbook personas across {len(DOMAINS)} domains.")


if __name__ == "__main__":
    main()
