def analyze_code(code: str):
    result = {
        "syntax_errors": [],
        "style_issues": [],
        "complexity_issues": [],
        "security_issues": []
    }

    try:
        compile(code, "<string>", "exec")
    except SyntaxError as e:
        result["syntax_errors"].append({
            "line": e.lineno,
            "message": str(e)
        })
        return result

    if "eval(" in code:
        result["security_issues"].append({
            "issue": "Use of eval() is unsafe"
        })

    if "exec(" in code:
        result["security_issues"].append({
            "issue": "Use of exec() is unsafe"
        })

    if "print(" in code:
        result["style_issues"].append({
            "issue": "Avoid print statements in production code"
        })

    if code.count("if") > 10:
        result["complexity_issues"].append({
            "issue": "Too many conditional statements"
        })

    return result