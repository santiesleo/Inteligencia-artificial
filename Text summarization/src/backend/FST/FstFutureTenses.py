from pyformlang.fst import FST


def create_fst_present_to_future_simple():
    fst = FST()

    
    for present, past in verbs_dic.items():
        fst.add_transitions([(0, present, 1, [past])])

    fst.add_start_state(0)
    fst.add_final_state(1)

    return fst


verbs_dic = {
    "he": "he will",
    "she":"she will",
    "it":"it will",
    "we":"we will",
    "you":"you will",
    "they":"they will",
    "i":"i will",
    "am":"be",
    "is":"be",
    "are":"be",

    "dances": "dance",
    "accepts": "accept",
    "adds": "add",
    "admires": "admire",
    "works": "work",
    "writes": "write",
    "abandons": "abandon",
    "accelerates": "accelerate",
    "accommodates": "accommodate",
    "accompanies": "accompany",
    "accomplishes": "accomplish",
    "accuses": "accuse",
    "achieves": "achieve",
    "acquires": "acquire",
    "acts": "act",
    "adapts": "adapt",
    "addresses": "address",
    "administers": "administer",
    "advances": "advance",
    "advertises": "advertise",
    "affects": "affect",
    "aims": "aim",
    "allocates": "allocate",
    "alters": "alter",
    "amends": "amend",
    "analyzes": "analyze",
    "announces": "announce",
    "anticipates": "anticipate",
    "appeals": "appeal",
    "appoints": "appoint",
    "appreciates": "appreciate",
    "approaches": "approach",
    "approves": "approve",
    "arises": "arise",
    "assesses": "assess",
    "assigns": "assign",
    "assists": "assist",
    "associates": "associate",
    "assumes": "assume",
    "assures": "assure",
    "attaches": "attach",
    "attempts": "attempt",
    "attends": "attend",
    "attracts": "attract",
    "authorizes": "authorize",
    "balances": "balance",
    "bases": "base",
    "beats": "beat",
    "behaves": "behave",
    "bends": "bend",
    "benefits": "benefit",
    "bets": "bet",
    "binds": "bind",
    "bites": "bite",
    "blames": "blame",
    "blows": "blow",
    "boosts": "boost",
    "burns": "burn",
    "bursts": "burst",
    "calculates": "calculate",
    "captures": "capture",
    "cares": "care",
    "casts": "cast",
    "causes": "cause",
    "celebrates": "celebrate",
    "challenges": "challenge",
    "characterizes": "characterize",
    "charges": "charge",
    "chases": "chase",
    "cheats": "cheat",
    "checks": "check",
    "clings": "cling",
    "collects": "collect",
    "combines": "combine",
    "commands": "command",
    "communicates": "communicate",
    "compares": "compare",
    "competes": "compete",
    "compiles": "compile",
    "composes": "compose",
    "comprises": "comprise",
    "computes": "compute",
    "conceives": "conceive",
    "concentrates": "concentrate",
    "concerns": "concern",
    "concludes": "conclude",
    "conducts": "conduct",
    "confesses": "confess",
    "confines": "confine",
    "confirms": "confirm",
    "confronts": "confront",
    "confuses": "confuse",
    "connects": "connect",
    "conserves": "conserve",
    "considers": "consider",
    "consists": "consist",
    "constitutes": "constitute",
    "constructs": "construct",
    "consults": "consult",
    "consumes": "consume",
    "contains": "contain",
    "contemplates": "contemplate",
    "contends": "contend",
    "contests": "contest",
    "contributes": "contribute",
    "controls": "control",
    "converts": "convert",
    "convinces": "convince",
    "cooperates": "cooperate",
    "coordinates": "coordinate",
    "copes": "cope",
    "corresponds": "correspond",
    "creeps": "creep",
    "cultivates": "cultivate",
    "cures": "cure",
    "dares": "dare",
    "deals": "deal",
    "debates": "debate",
    "decays": "decay",
    "deceives": "deceive",
    "declares": "declare",
    "declines": "decline",
    "decorates": "decorate",
    "decreases": "decrease",
    "dedicates": "dedicate",
    "deems": "deem",
    "defeats": "defeat",
    "defends": "defend",
    "defines": "define",
    "delays": "delay",
    "delegates": "delegate",
    "deletes": "delete",
    "deliberates": "deliberate",
    "demonstrates": "demonstrate",
    "departs": "depart",
    "depicts": "depict",
    "derives": "derive",
    "descends": "descend",
    "deserves": "deserve",
    "desires": "desire",
    "detects": "detect",
    "determines": "determine",
    "devotes": "devote",
    "diagnoses": "diagnose",
    "digs": "dig",
    "diminishes": "diminish",
    "directs": "direct",
    "disappears": "disappear",
    "discharges": "discharge",
    "discloses": "disclose",
    "disconnects": "disconnect",
    "discourages": "discourage",
    "displays": "display",
    "disposes": "dispose",
    "distinguishes": "distinguish",
    "distributes": "distribute",
    "dives": "dive",
    "divides": "divide",
    "drags": "drag",
    "drifts": "drift",
    "drips": "drip",
    "drops": "drop",
    "dwells": "dwell",
    "earns": "earn",
    "eats": "eat",
    "echoes": "echo",
    "educates": "educate",
    "elects": "elect",
    "eliminates": "eliminate",
    "embarrasses": "embarrass",
    "emerges": "emerge",
    "emphasizes": "emphasize",
    "employs": "employ",
    "enables": "enable",
    "encloses": "enclose",
    "encounters": "encounter",
    "encourages": "encourage",
    "endures": "endure",
    "enforces": "enforce",
    "engages": "engage",
    "enhances": "enhance",
    "ensures": "ensure",
    "entails": "entail",
    "entertains": "entertain",
    "equals": "equal",
    "equips": "equip",
    "erodes": "erode",
    "erupts": "erupt",
    "establishes": "establish",
    "estimates": "estimate",
    "evaluates": "evaluate",
    "evolves": "evolve",
    "exceeds": "exceed",
    "exchanges": "exchange",
    "excludes": "exclude",
    "excuses": "excuse",
    "executes": "execute",
    "exercises": "exercise",
    "exhausts": "exhaust",
    "exhibits": "exhibit",
    "expands": "expand",
    "experiences": "experience",
    "experiments": "experiment",
    "expires": "expire",
    "explains": "explain",
    "explodes": "explode",
    "exploits": "exploit",
    "explores": "explore",
    "exports": "export",
    "exposes": "expose",
    "expresses": "express",
    "extends": "extend",
    "faces": "face",
    "facilitates": "facilitate",
    "fades": "fade",
    "features": "feature",
    "feeds": "feed",
    "fetches": "fetch",
    "files": "file",
    "fills": "fill",
    "films": "film",
    "finances": "finance",
    "fires": "fire",
    "fixes": "fix",
    "flashes": "flash",
    "flees": "flee",
    "flings": "fling",
    "floats": "float",
    "floods": "flood",
    "flows": "flow",
    "folds": "fold",
    "forbids": "forbid",
    "forecasts": "forecast",
    "foresees": "foresee",
    "foretells": "foretell",
    "forms": "form",
    "formulates": "formulate",
    "fosters": "foster",
    "founds": "found",
    "frames": "frame",
    "frees": "free",
    "frightens": "frighten",
    "fulfills": "fulfill",
    "functions": "function",
    "funds": "fund",
    "gains": "gain",
    "gathers": "gather",
    "gazes": "gaze",
    "generates": "generate",
    "glances": "glance",
    "glows": "glow",
    "governs": "govern",
    "grabs": "grab",
    "grades": "grade",
    "grants": "grant",
    "grasps": "grasp",
    "greets": "greet",
    "grinds": "grind",
    "grips": "grip",
    "guarantees": "guarantee",
    "guards": "guard",
    "guides": "guide",
    "handles": "handle",
    "hangs": "hang",
    "harvests": "harvest",
    "heads": "head",
    "heals": "heal",
    "heats": "heat",
    "hesitates": "hesitate",
    "hires": "hire",
    "hosts": "host",
    "hunts": "hunt",
    "hurries": "hurry",
    "identifies": "identify",
    "ignores": "ignore",
    "illustrates": "illustrate",
    "imitates": "imitate",
    "implements": "implement",
    "implies": "imply",
    "imports": "import",
    "imposes": "impose",
    "impresses": "impress",
    "improves": "improve",
    "includes": "include",
    "incorporates": "incorporate",
    "increases": "increase",
    "induces": "induce",
    "influences": "influence",
    "informs": "inform",
    "initiates": "initiate",
    "injects": "inject",
    "injures": "injure",
    "inserts": "insert",
    "insists": "insist",
    "inspects": "inspect",
    "inspires": "inspire",
    "installs": "install",
    "institutes": "institute",
    "instructs": "instruct",
    "insures": "insure",
    "integrates": "integrate",
    "intends": "intend",
    "intensifies": "intensify",
    "interprets": "interpret",
    "interrupts": "interrupt",
    "intervenes": "intervene",
    "introduces": "introduce",
    "invents": "invent",
    "invests": "invest",
    "investigates": "investigate",
    "invites": "invite",
    "involves": "involve",
    "isolates": "isolate",
    "issues": "issue",
    "judges": "judge",
    "jumps": "jump",
    "justifies": "justify",
    "kicks": "kick",
    "kneels": "kneel",
    "knits": "knit",
    "labels": "label",
    "lacks": "lack",
    "lands": "land",
    "lasts": "last",
    "launches": "launch",
    "lays": "lay",
    "leads": "lead",
    "leans": "lean",
    "leaps": "leap",
    "learns": "learn",
    "lectures": "lecture",
    "lends": "lend",
    "levels": "level",
    "licenses": "license",
    "lifts": "lift",
    "lights": "light",
    "limits": "limit",
    "links": "link",
    "lists": "list",
    "locates": "locate",
    "locks": "lock",
    "logs": "log",
    "longs": "long",
    "looks": "look",
    "maintains": "maintain",
    "manages": "manage",
    "manufactures": "manufacture",
    "marches": "march",
    "marks": "mark",
    "markets": "market",
    "matches": "match",
    "matters": "matter",
    "measures": "measure",
    "melts": "melt",
    "mentions": "mention",
    "merges": "merge",
    "minds": "mind",
    "misses": "miss",
    "mixes": "mix",
    "models": "model",
    "modifies": "modify",
    "monitors": "monitor",
    "motivates": "motivate",
    "mounts": "mount",
    "names": "name",
    "neglects": "neglect",
    "negotiates": "negotiate",
    "nods": "nod",
    "nominates": "nominate",
    "notes": "note",
    "notifies": "notify",
    "observes": "observe",
    "obtains": "obtain",
    "occurs": "occur",
    "offends": "offend",
    "operates": "operate",
    "orders": "order",
    "organizes": "organize",
    "originates": "originate",
    "outlines": "outline",
    "overcomes": "overcome",
    "overlooks": "overlook",
    "overwhelms": "overwhelm",
    "owes": "owe",
    "owns": "own",
    "packs": "pack",
    "paints": "paint",
    "participates": "participate",
    "passes": "pass",
    "pauses": "pause",
    "performs": "perform",
    "permits": "permit",
    "persuades": "persuade",
    "picks": "pick",
    "pilots": "pilot",
    "pins": "pin",
    "places": "place",
    "plants": "plant",
    "pleases": "please",
    "plots": "plot",
    "points": "point",
    "possesses": "possess",
    "posts": "post",
    "pours": "pour",
    "practices": "practice",
    "praises": "praise",
    "prays": "pray",
    "plays": "play",
    "predicts": "predict",
    "prefers": "prefer",
    "prepares": "prepare",
    "prescribes": "prescribe",
    "presents": "present",
    "preserves": "preserve",
    "presses": "press",
    "pretends": "pretend",
    "prevails": "prevail",
    "prevents": "prevent",
    "prints": "print",
    "proceeds": "proceed",
    "processes": "process",
    "produces": "produce",
    "programs": "program",
    "progresses": "progress",
    "prohibits": "prohibit",
    "projects": "project",
    "promotes": "promote",
    "proposes": "propose",
    "protects": "protect",
    "protests": "protest",
    "provides": "provide",
    "publishes": "publish",
    "pulls": "pull",
    "pumps": "pump",
    "punches": "punch",
    "purchases": "purchase",
    "pursues": "pursue",
    "qualifies": "qualify",
    "questions": "question",
    "quits": "quit",
    "quotes": "quote",
    "races": "race",
    "rains": "rain",
    "raises": "raise",
    "ranks": "rank",
    "rates": "rate",
    "reaches": "reach",
    "reacts": "react",
    "reads": "read",
    "realizes": "realize",
    "receives": "receive",
    "recognizes": "recognize",
    "recommends": "recommend",
    "remembers": "remember",
    "repairs": "repair",
    "repeats": "repeat",
    "replaces": "replace",
    "replies": "reply",
    "reports": "report",
    "requests": "request",
    "rescues": "rescue",
    "retires": "retire",
    "returns": "return",
    "rides": "ride",
    "rings": "ring",
    "rises": "rise",
    "runs": "run",
    "saves": "save",
    "says": "say",
    "sees": "see",
    "sells": "sell",
    "sends": "send",
    "shakes": "shake",
    "shares": "share",
    "shoots": "shoot",
    "shows": "show",
    "shuts": "shut",
    "sings": "sing",
    "sits": "sit",
    "sleeps": "sleep",
    "speaks": "speak",
    "spends": "spend",
    "stands": "stand",
    "starts": "start",
    "stays": "stay",
    "steals": "steal",
    "stops": "stop",
    "studies": "study",
    "suggests": "suggest",
    "swims": "swim",
    "takes": "take",
    "talks": "talk",
    "teaches": "teach",
    "tells": "tell",
    "thinks": "think",
    "throws": "throw",
    "touches": "touch",
    "travels": "travel",
    "tries": "try",
    "turns": "turn",
    "understands": "understand",
    "uses": "use",
    "visits": "visit",
    "waits": "wait",
    "wakes": "wake",
    "walks": "walk",
    "wants": "want",
    "watches": "watch",
    "wins": "win",
    "wishes": "wish",
    "works": "work",
    "writes": "write"
}
