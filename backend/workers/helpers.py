# Small reusable checks used by analyzer

def check_syntax(code: str):
    """
    Returns syntax error info if present.
    """
    try:
        compile(code, "<string>", "exec")
        return None
    except SyntaxError as e:
        return {
            "line": e.lineno,
            "message": str(e)
        }