# Central place for rules

# Complexity thresholds
MAX_IF_COUNT = 10

# Security risky functions
DANGEROUS_FUNCTIONS = [
    "eval(",
    "exec(",
]

# Style anti-patterns
STYLE_ISSUES = {
    "print(": "Avoid print statements in production code"
}

# Scoring penalties
SCORE_PENALTIES = {
    "syntax": 30,
    "security": 20,
    "style": 10,
    "complexity": 5
}