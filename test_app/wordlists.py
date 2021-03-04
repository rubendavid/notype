import random

COMMON = [
    "a",
    "ability",
    "able",
    "about",
    "above",
    "accept",
    "according",
    "account",
    "across",
    "act",
    "action",
    "activity",
    "actually",
    "add",
    "address",
    "administration",
    "admit",
    "adult",
    "affect",
    "after",
    "again",
    "against",
    "age",
    "agency",
    "agent",
    "ago",
    "agree",
    "agreement",
    "ahead",
    "air",
    "all",
    "allow",
    "almost",
    "alone",
    "along",
    "already",
    "also",
    "although",
    "always",
    "american",
    "among",
    "amount",
    "analysis",
    "and",
    "animal",
    "another",
    "answer",
    "any",
    "anyone",
    "anything",
    "appear",
    "apply",
    "approach",
    "area",
    "argue",
    "arm",
    "around",
    "arrive",
    "art",
    "article",
    "artist",
    "as",
    "ask",
    "assume",
    "at",
    "attack",
    "attention",
    "attorney",
    "audience",
    "author",
    "authority",
    "available",
    "avoid",
    "away",
    "baby",
    "back",
    "bad",
    "bag",
    "ball",
    "bank",
    "bar",
    "base",
    "be",
    "beat",
    "beautiful",
    "because",
    "become",
    "bed",
    "before",
    "begin",
    "behavior",
    "behind",
    "believe",
    "benefit",
    "best",
    "better",
    "between",
    "beyond",
    "big",
    "bill",
    "billion",
    "bit",
    "black",
    "blood",
    "blue",
    "board",
    "body",
    "book",
    "born",
    "both",
    "box",
    "boy",
    "break",
    "bring",
    "brother",
    "budget",
    "build",
    "building",
    "business",
    "but",
    "buy",
    "by",
    "call",
    "camera",
    "campaign",
    "can",
    "cancer",
    "candidate",
    "capital",
    "car",
    "card",
    "care",
    "career",
    "carry",
    "case",
    "catch",
    "cause",
    "cell",
    "center",
    "central",
    "century",
    "certain",
    "certainly",
    "chair",
    "challenge",
    "chance",
    "change",
    "character",
    "charge",
    "check",
    "child",
    "choice",
    "choose",
    "church",
    "citizen",
    "city",
    "civil",
    "claim",
    "class",
    "clear",
    "clearly",
    "close",
    "coach",
    "cold",
    "collection",
    "college",
    "color",
    "come",
    "commercial",
    "common",
    "community",
    "company",
    "compare",
    "computer",
    "concern",
    "condition",
    "conference",
    "congress",
    "consider",
    "consumer",
    "contain",
    "continue",
    "control",
    "cost",
    "could",
    "country",
    "couple",
    "course",
    "court",
    "cover",
    "create",
    "crime",
    "cultural",
    "culture",
    "cup",
    "current",
    "customer",
    "cut",
    "dark",
    "data",
    "daughter",
    "day",
    "dead",
    "deal",
    "death",
    "debate",
    "decade",
    "decide",
    "decision",
    "deep",
    "defense",
    "degree",
    "democrat",
    "democratic",
    "describe",
    "design",
    "despite",
    "detail",
    "determine",
    "develop",
    "development",
    "die",
    "difference",
    "different",
    "difficult",
    "dinner",
    "direction",
    "director",
    "discover",
    "discuss",
    "discussion",
    "disease",
    "do",
    "doctor",
    "dog",
    "door",
    "down",
    "draw",
    "dream",
    "drive",
    "drop",
    "drug",
    "during",
    "each",
    "early",
    "east",
    "easy",
    "eat",
    "economic",
    "economy",
    "edge",
    "education",
    "effect",
    "effort",
    "eight",
    "either",
    "election",
    "else",
    "employee",
    "end",
    "energy",
    "enjoy",
    "enough",
    "enter",
    "entire",
    "environment",
    "environmental",
    "especially",
    "establish",
    "even",
    "evening",
    "event",
    "ever",
    "every",
    "everybody",
    "everyone",
    "everything",
    "evidence",
    "exactly",
    "example",
    "executive",
    "exist",
    "expect",
    "experience",
    "expert",
    "explain",
    "eye",
    "face",
    "fact",
    "factor",
    "fail",
    "fall",
    "family",
    "far",
    "fast",
    "father",
    "fear",
    "federal",
    "feel",
    "feeling",
    "few",
    "field",
    "fight",
    "figure",
    "fill",
    "film",
    "final",
    "finally",
    "financial",
    "find",
    "fine",
    "finger",
    "finish",
    "fire",
    "firm",
    "first",
    "fish",
    "five",
    "floor",
    "fly",
    "focus",
    "follow",
    "food",
    "foot",
    "for",
    "force",
    "foreign",
    "forget",
    "form",
    "former",
    "forward",
    "four",
    "free",
    "friend",
    "from",
    "front",
    "full",
    "fund",
    "future",
    "game",
    "garden",
    "gas",
    "general",
    "generation",
    "get",
    "girl",
    "give",
    "glass",
    "go",
    "goal",
    "good",
    "government",
    "great",
    "green",
    "ground",
    "group",
    "grow",
    "growth",
    "guess",
    "gun",
    "guy",
    "hair",
    "half",
    "hand",
    "hang",
    "happen",
    "happy",
    "hard",
    "have",
    "he",
    "head",
    "health",
    "hear",
    "heart",
    "heat",
    "heavy",
    "help",
    "her",
    "here",
    "herself",
    "high",
    "him",
    "himself",
    "his",
    "history",
    "hit",
    "hold",
    "home",
    "hope",
    "hospital",
    "hot",
    "hotel",
    "hour",
    "house",
    "how",
    "however",
    "huge",
    "human",
    "hundred",
    "husband",
    "i",
    "idea",
    "identify",
    "if",
    "image",
    "imagine",
    "impact",
    "important",
    "improve",
    "in",
    "include",
    "including",
    "increase",
    "indeed",
    "indicate",
    "individual",
    "industry",
    "information",
    "inside",
    "instead",
    "institution",
    "interest",
    "interesting",
    "international",
    "interview",
    "into",
    "investment",
    "involve",
    "issue",
    "it",
    "item",
    "its",
    "itself",
    "job",
    "join",
    "just",
    "keep",
    "key",
    "kid",
    "kill",
    "kind",
    "kitchen",
    "know",
    "knowledge",
    "land",
    "language",
    "large",
    "last",
    "late",
    "later",
    "laugh",
    "law",
    "lawyer",
    "lay",
    "lead",
    "leader",
    "learn",
    "least",
    "leave",
    "left",
    "leg",
    "legal",
    "less",
    "let",
    "letter",
    "level",
    "lie",
    "life",
    "light",
    "like",
    "likely",
    "line",
    "list",
    "listen",
    "little",
    "live",
    "local",
    "long",
    "look",
    "lose",
    "loss",
    "lot",
    "love",
    "low",
    "machine",
    "magazine",
    "main",
    "maintain",
    "major",
    "majority",
    "make",
    "man",
    "manage",
    "management",
    "manager",
    "many",
    "market",
    "marriage",
    "material",
    "matter",
    "may",
    "maybe",
    "me",
    "mean",
    "measure",
    "media",
    "medical",
    "meet",
    "meeting",
    "member",
    "memory",
    "mention",
    "message",
    "method",
    "middle",
    "might",
    "military",
    "million",
    "mind",
    "minute",
    "miss",
    "mission",
    "model",
    "modern",
    "moment",
    "money",
    "month",
    "more",
    "morning",
    "most",
    "mother",
    "mouth",
    "move",
    "movement",
    "movie",
    "mr",
    "mrs",
    "much",
    "music",
    "must",
    "my",
    "myself",
    "name",
    "nation",
    "national",
    "natural",
    "nature",
    "near",
    "nearly",
    "necessary",
    "need",
    "network",
    "never",
    "new",
    "news",
    "newspaper",
    "next",
    "nice",
    "night",
    "no",
    "none",
    "nor",
    "north",
    "not",
    "note",
    "nothing",
    "notice",
    "now",
    "n't",
    "number",
    "occur",
    "of",
    "off",
    "offer",
    "office",
    "officer",
    "official",
    "often",
    "oh",
    "oil",
    "ok",
    "old",
    "on",
    "once",
    "one",
    "only",
    "onto",
    "open",
    "operation",
    "opportunity",
    "option",
    "or",
    "order",
    "organization",
    "other",
    "others",
    "our",
    "out",
    "outside",
    "over",
    "own",
    "owner",
    "page",
    "pain",
    "painting",
    "paper",
    "parent",
    "part",
    "participant",
    "particular",
    "particularly",
    "partner",
    "party",
    "pass",
    "past",
    "patient",
    "pattern",
    "pay",
    "peace",
    "people",
    "per",
    "perform",
    "performance",
    "perhaps",
    "period",
    "person",
    "personal",
    "phone",
    "physical",
    "pick",
    "picture",
    "piece",
    "place",
    "plan",
    "plant",
    "play",
    "player",
    "pm",
    "point",
    "police",
    "policy",
    "political",
    "politics",
    "poor",
    "popular",
    "population",
    "position",
    "positive",
    "possible",
    "power",
    "practice",
    "prepare",
    "present",
    "president",
    "pressure",
    "pretty",
    "prevent",
    "price",
    "private",
    "probably",
    "problem",
    "process",
    "produce",
    "product",
    "production",
    "professional",
    "professor",
    "program",
    "project",
    "property",
    "protect",
    "prove",
    "provide",
    "public",
    "pull",
    "purpose",
    "push",
    "put",
    "quality",
    "question",
    "quickly",
    "quite",
    "race",
    "radio",
    "raise",
    "range",
    "rate",
    "rather",
    "reach",
    "read",
    "ready",
    "real",
    "reality",
    "realize",
    "really",
    "reason",
    "receive",
    "recent",
    "recently",
    "recognize",
    "record",
    "red",
    "reduce",
    "reflect",
    "region",
    "relate",
    "relationship",
    "religious",
    "remain",
    "remember",
    "remove",
    "report",
    "represent",
    "republican",
    "require",
    "research",
    "resource",
    "respond",
    "response",
    "responsibility",
    "rest",
    "result",
    "return",
    "reveal",
    "rich",
    "right",
    "rise",
    "risk",
    "road",
    "rock",
    "role",
    "room",
    "rule",
    "run",
    "safe",
    "same",
    "save",
    "say",
    "scene",
    "school",
    "science",
    "scientist",
    "score",
    "sea",
    "season",
    "seat",
    "second",
    "section",
    "security",
    "see",
    "seek",
    "seem",
    "sell",
    "send",
    "senior",
    "sense",
    "series",
    "serious",
    "serve",
    "service",
    "set",
    "seven",
    "several",
    "sex",
    "sexual",
    "shake",
    "share",
    "she",
    "shoot",
    "short",
    "shot",
    "should",
    "shoulder",
    "show",
    "side",
    "sign",
    "significant",
    "similar",
    "simple",
    "simply",
    "since",
    "sing",
    "single",
    "sister",
    "sit",
    "site",
    "situation",
    "six",
    "size",
    "skill",
    "skin",
    "small",
    "smile",
    "so",
    "social",
    "society",
    "soldier",
    "some",
    "somebody",
    "someone",
    "something",
    "sometimes",
    "son",
    "song",
    "soon",
    "sort",
    "sound",
    "source",
    "south",
    "southern",
    "space",
    "speak",
    "special",
    "specific",
    "speech",
    "spend",
    "sport",
    "spring",
    "staff",
    "stage",
    "stand",
    "standard",
    "star",
    "start",
    "state",
    "statement",
    "station",
    "stay",
    "step",
    "still",
    "stock",
    "stop",
    "store",
    "story",
    "strategy",
    "street",
    "strong",
    "structure",
    "student",
    "study",
    "stuff",
    "style",
    "subject",
    "success",
    "successful",
    "such",
    "suddenly",
    "suffer",
    "suggest",
    "summer",
    "support",
    "sure",
    "surface",
    "system",
    "table",
    "take",
    "talk",
    "task",
    "tax",
    "teach",
    "teacher",
    "team",
    "technology",
    "television",
    "tell",
    "ten",
    "tend",
    "term",
    "test",
    "than",
    "thank",
    "that",
    "the",
    "their",
    "them",
    "themselves",
    "then",
    "theory",
    "there",
    "these",
    "they",
    "thing",
    "think",
    "third",
    "this",
    "those",
    "though",
    "thought",
    "thousand",
    "threat",
    "three",
    "through",
    "throughout",
    "throw",
    "thus",
    "time",
    "to",
    "today",
    "together",
    "tonight",
    "too",
    "top",
    "total",
    "tough",
    "toward",
    "town",
    "trade",
    "traditional",
    "training",
    "travel",
    "treat",
    "treatment",
    "tree",
    "trial",
    "trip",
    "trouble",
    "true",
    "truth",
    "try",
    "turn",
    "tv",
    "two",
    "type",
    "under",
    "understand",
    "unit",
    "until",
    "up",
    "upon",
    "us",
    "use",
    "usually",
    "value",
    "various",
    "very",
    "victim",
    "view",
    "violence",
    "visit",
    "voice",
    "vote",
    "wait",
    "walk",
    "wall",
    "want",
    "war",
    "watch",
    "water",
    "way",
    "we",
    "weapon",
    "wear",
    "week",
    "weight",
    "well",
    "west",
    "western",
    "what",
    "whatever",
    "when",
    "where",
    "whether",
    "which",
    "while",
    "white",
    "who",
    "whole",
    "whom",
    "whose",
    "why",
    "wide",
    "wife",
    "will",
    "win",
    "wind",
    "window",
    "wish",
    "with",
    "within",
    "without",
    "woman",
    "wonder",
    "word",
    "work",
    "worker",
    "world",
    "worry",
    "would",
    "write",
    "writer",
    "wrong",
    "yard",
    "yeah",
    "year",
    "yes",
    "yet",
    "you",
    "young",
    "your",
    "yourself",
]

COMMON_LENGTH_DICT = {
    2: ['as', 'at', 'be', 'by', 'do', 'go', 'he', 'if', 'in', 'it', 'me', 'my', 'no', 'of', 'oh', 'ok', 'on', 'or', 'so', 'to', 'up', 'us', 'we'], 
    3: ['act', 'add', 'age', 'ago', 'air', 'all', 'and', 'any', 'arm', 'art', 'ask', 'bad', 'bag', 'bar', 'bed', 'big', 'bit', 'box', 'boy', 'but', 'buy', 'can', 'car', 'cup', 'cut', 'day', 'die', 'dog', 'eat', 'end', 'eye', 'far', 'few', 'fly', 'for', 'gas', 'get', 'gun', 'guy', 'her', 'him', 'his', 'hit', 'hot', 'how', 'its', 'job', 'key', 'kid', 'law', 'lay', 'leg', 'let', 'lie', 'lot', 'low', 'man', 'may', 'mrs', 'new', 'nor', 'not', 'now', "n't", 'off', 'oil', 'old', 'one', 'our', 'out', 'own', 'pay', 'per', 'put', 'red', 'run', 'say', 'sea', 'see', 'set', 'sex', 'she', 'sit', 'six', 'son', 'tax', 'ten', 'the', 'too', 'top', 'try', 'two', 'use', 'war', 'way', 'who', 'why', 'win', 'yes', 'yet', 'you'], 
    4: ['able', 'also', 'area', 'away', 'baby', 'back', 'ball', 'bank', 'base', 'beat', 'best', 'bill', 'blue', 'body', 'book', 'born', 'both', 'call', 'card', 'care', 'case', 'cell', 'city', 'cold', 'come', 'cost', 'dark', 'data', 'dead', 'deal', 'deep', 'door', 'down', 'draw', 'drop', 'drug', 'each', 'east', 'easy', 'edge', 'else', 'even', 'ever', 'face', 'fact', 'fail', 'fall', 'fast', 'fear', 'feel', 'fill', 'film', 'find', 'fine', 'fire', 'firm', 'fish', 'five', 'food', 'foot', 'form', 'four', 'free', 'from', 'full', 'fund', 'game', 'girl', 'give', 'goal', 'good', 'grow', 'hair', 'half', 'hand', 'hang', 'hard', 'have', 'head', 'hear', 'heat', 'help', 'here', 'high', 'hold', 'home', 'hope', 'hour', 'huge', 'idea', 'into', 'item', 'join', 'just', 'keep', 'kill', 'kind', 'know', 'land', 'last', 'late', 'lead', 'left', 'less', 'life', 'like', 'line', 'list', 'live', 'long', 'look', 'lose', 'loss', 'love', 'main', 'make', 'many', 'mean', 'meet', 'mind', 'miss', 'more', 'most', 'move', 'much', 'must', 'name', 'near', 'need', 'news', 'next', 'nice', 'none', 'note', 'once', 'only', 'onto', 'open', 'over', 'page', 'pain', 'part', 'pass', 'past', 'pick', 'plan', 'play', 'poor', 'pull', 'push', 'race', 'rate', 'read', 'real', 'rest', 'rich', 'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'safe', 'same', 'save', 'seat', 'seek', 'seem', 'sell', 'send', 'shot', 'show', 'side', 'sign', 'sing', 'site', 'size', 'skin', 'some', 'song', 'soon', 'sort', 'star', 'stay', 'step', 'stop', 'such', 'sure', 'take', 'talk', 'task', 'team', 'tell', 'tend', 'term', 'test', 'than', 'that', 'them', 'then', 'they', 'this', 'thus', 'time', 'town', 'tree', 'trip', 'true', 'turn', 'type', 'unit', 'upon', 'very', 'view', 'vote', 'wait', 'walk', 'wall', 'want', 'wear', 'week', 'well', 'west', 'what', 'when', 'whom', 'wide', 'wife', 'will', 'wind', 'wish', 'with', 'word', 'work', 'yard', 'yeah', 'year', 'your'], 
    5: ['about', 'above', 'admit', 'adult', 'after', 'again', 'agent', 'agree', 'ahead', 'allow', 'alone', 'along', 'among', 'apply', 'argue', 'avoid', 'begin', 'black', 'blood', 'board', 'break', 'bring', 'build', 'carry', 'catch', 'cause', 'chair', 'check', 'child', 'civil', 'claim', 'class', 'clear', 'close', 'coach', 'color', 'could', 'court', 'cover', 'crime', 'death', 'dream', 'drive', 'early', 'eight', 'enjoy', 'enter', 'event', 'every', 'exist', 'field', 'fight', 'final', 'first', 'floor', 'focus', 'force', 'front', 'glass', 'great', 'green', 'group', 'guess', 'happy', 'heart', 'heavy', 'hotel', 'house', 'human', 'image', 'issue', 'large', 'later', 'laugh', 'learn', 'least', 'leave', 'legal', 'level', 'light', 'local', 'major', 'maybe', 'media', 'might', 'model', 'money', 'month', 'mouth', 'movie', 'music', 'never', 'night', 'north', 'occur', 'offer', 'often', 'order', 'other', 'owner', 'paper', 'party', 'peace', 'phone', 'piece', 'place', 'plant', 'point', 'power', 'price', 'prove', 'quite', 'radio', 'raise', 'range', 'reach', 'ready', 'right', 'scene', 'score', 'sense', 'serve', 'seven', 'shake', 'share', 'shoot', 'short', 'since', 'skill', 'small', 'smile', 'sound', 'south', 'space', 'speak', 'spend', 'sport', 'staff', 'stage', 'stand', 'start', 'state', 'still', 'stock', 'store', 'story', 'study', 'stuff', 'style', 'table', 'teach', 'thank', 'their', 'there', 'these', 'thing', 'think', 'third', 'those', 'three', 'throw', 'today', 'total', 'tough', 'trade', 'treat', 'trial', 'truth', 'under', 'until', 'value', 'visit', 'voice', 'watch', 'water', 'where', 'which', 'while', 'white', 'whole', 'whose', 'woman', 'world', 'worry', 'would', 'write', 'wrong', 'young'], 
    6: ['accept', 'across', 'action', 'affect', 'agency', 'almost', 'always', 'amount', 'animal', 'answer', 'anyone', 'appear', 'around', 'arrive', 'artist', 'assume', 'attack', 'author', 'become', 'before', 'behind', 'better', 'beyond', 'budget', 'camera', 'cancer', 'career', 'center', 'chance', 'change', 'charge', 'choice', 'choose', 'church', 'common', 'couple', 'course', 'create', 'debate', 'decade', 'decide', 'degree', 'design', 'detail', 'dinner', 'doctor', 'during', 'effect', 'effort', 'either', 'energy', 'enough', 'entire', 'expect', 'expert', 'factor', 'family', 'father', 'figure', 'finger', 'finish', 'follow', 'forget', 'former', 'friend', 'future', 'garden', 'ground', 'growth', 'happen', 'health', 'impact', 'indeed', 'inside', 'itself', 'lawyer', 'leader', 'letter', 'likely', 'listen', 'little', 'manage', 'market', 'matter', 'member', 'memory', 'method', 'middle', 'minute', 'modern', 'moment', 'mother', 'myself', 'nation', 'nature', 'nearly', 'notice', 'number', 'office', 'option', 'others', 'parent', 'people', 'period', 'person', 'player', 'police', 'policy', 'pretty', 'public', 'rather', 'really', 'reason', 'recent', 'record', 'reduce', 'region', 'relate', 'remain', 'remove', 'report', 'result', 'return', 'reveal', 'school', 'season', 'second', 'senior', 'series', 'sexual', 'should', 'simple', 'simply', 'single', 'sister', 'social', 'source', 'speech', 'spring', 'street', 'strong', 'suffer', 'summer', 'system', 'theory', 'though', 'threat', 'toward', 'travel', 'victim', 'weapon', 'weight', 'window', 'within', 'wonder', 'worker', 'writer'], 
    7: ['ability', 'account', 'address', 'against', 'already', 'another', 'article', 'because', 'believe', 'benefit', 'between', 'billion', 'brother', 'capital', 'central', 'century', 'certain', 'citizen', 'clearly', 'college', 'company', 'compare', 'concern', 'contain', 'control', 'country', 'culture', 'current', 'defense', 'despite', 'develop', 'discuss', 'disease', 'economy', 'evening', 'exactly', 'example', 'explain', 'federal', 'feeling', 'finally', 'foreign', 'forward', 'general', 'herself', 'himself', 'history', 'however', 'hundred', 'husband', 'imagine', 'improve', 'include', 'instead', 'involve', 'kitchen', 'machine', 'manager', 'measure', 'medical', 'meeting', 'mention', 'message', 'million', 'mission', 'morning', 'natural', 'network', 'nothing', 'officer', 'outside', 'partner', 'patient', 'pattern', 'perform', 'perhaps', 'picture', 'popular', 'prepare', 'present', 'prevent', 'private', 'problem', 'process', 'produce', 'product', 'program', 'project', 'protect', 'provide', 'purpose', 'quality', 'quickly', 'reality', 'realize', 'receive', 'reflect', 'require', 'respond', 'science', 'section', 'serious', 'service', 'several', 'similar', 'society', 'soldier', 'someone', 'special', 'station', 'student', 'subject', 'success', 'suggest', 'support', 'surface', 'teacher', 'thought', 'through', 'tonight', 'trouble', 'usually', 'various', 'western', 'whether', 'without'], 
    8: ['activity', 'actually', 'although', 'american', 'analysis', 'anything', 'approach', 'attorney', 'audience', 'behavior', 'building', 'business', 'campaign', 'computer', 'congress', 'consider', 'consumer', 'continue', 'cultural', 'customer', 'daughter', 'decision', 'democrat', 'describe', 'director', 'discover', 'economic', 'election', 'employee', 'everyone', 'evidence', 'hospital', 'identify', 'increase', 'indicate', 'industry', 'interest', 'language', 'magazine', 'maintain', 'majority', 'marriage', 'material', 'military', 'movement', 'national', 'official', 'painting', 'personal', 'physical', 'politics', 'position', 'positive', 'possible', 'practice', 'pressure', 'probably', 'property', 'question', 'recently', 'remember', 'research', 'resource', 'response', 'security', 'shoulder', 'somebody', 'southern', 'specific', 'standard', 'strategy', 'suddenly', 'thousand', 'together', 'training', 'violence', 'whatever', 'yourself'], 
    9: ['according', 'agreement', 'attention', 'authority', 'available', 'beautiful', 'candidate', 'certainly', 'challenge', 'character', 'community', 'condition', 'determine', 'different', 'difficult', 'direction', 'education', 'establish', 'everybody', 'executive', 'financial', 'important', 'including', 'interview', 'knowledge', 'necessary', 'newspaper', 'operation', 'political', 'president', 'professor', 'recognize', 'religious', 'represent', 'scientist', 'situation', 'something', 'sometimes', 'statement', 'structure', 'treatment'], 
    10: ['collection', 'commercial', 'conference', 'democratic', 'difference', 'discussion', 'especially', 'everything', 'experience', 'generation', 'government', 'individual', 'investment', 'management', 'particular', 'population', 'production', 'republican', 'successful', 'technology', 'television', 'themselves', 'throughout', 'understand'], 
    11: ['development', 'environment', 'information', 'institution', 'interesting', 'opportunity', 'participant', 'performance', 'significant', 'traditional'], 
    12: ['organization', 'particularly', 'professional', 'relationship'],
    13: ['environmental', 'international'], 
    14: ['administration', 'responsibility'], 
}

# def create_length_dict():
#     length_dict = {}
#     for word in COMMON:
#         if len(word) not in length_dict:
#             length_dict[len(word)] = []
#         length_dict[len(word)].append(word)
#     return length_dict 

def get_new_test(length, difficulty):
    words = []

    # medium
    if difficulty == 2:
        max_word_length = 10
    # hard
    elif difficulty == 3:
        max_word_length = 14
    # default - easy
    else:
        max_word_length = 6

    wordlists = [words for word_length, words in COMMON_LENGTH_DICT.items() if word_length <= max_word_length]
    wordlist = [item for sublist in wordlists for item in sublist]

    for _ in range(length):
        word = wordlist[random.randint(0, len(wordlist)-1)]
        words.append(word)
    return words