# Parsing & counting helpers

def count_keyword(code: str, keyword: str) -> int:
    """
    Counts occurrences of a keyword in code.
    """
    return code.count(keyword)


def contains_any(code: str, patterns: list) -> list:
    """
    Returns list of patterns found in code.
    """
    return [p for p in patterns if p in code]