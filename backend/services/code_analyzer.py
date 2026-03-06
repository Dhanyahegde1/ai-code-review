from backend.workers.constants import MAX_IF_COUNT, DANGEROUS_FUNCTIONS
from backend.workers.parser import count_keyword, contains_any
from backend.workers.helpers import check_syntax

def analyze_code(code: str):
    result = {
        "syntax_errors": [],
        "style_issues": [],
        "complexity_issues": [],
        "security_issues": []
    }
     # Syntax check using helper
    syntax_error = check_syntax(code)
    if syntax_error:
        result["syntax_errors"].append(syntax_error)
        return result

    # Security checks using constants + parser
    dangerous_found = contains_any(code, DANGEROUS_FUNCTIONS)
    for item in dangerous_found:
        result["security_issues"].append({
            "issue": f"Use of {item} is unsafe"
        })

    # Style checks
    if "print(" in code:
        result["style_issues"].append({
            "issue": "Avoid print statements in production code"
        })

    # Complexity check using constant
    if count_keyword(code, "if") > MAX_IF_COUNT:
        result["complexity_issues"].append({
            "issue": "Too many conditional statements"
        })

    return result
