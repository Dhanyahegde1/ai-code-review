def rule_based_ai(analysis_result):
    suggestions = []

    if analysis_result["syntax_errors"]:
        suggestions.append("Fix syntax errors before improvements.")

    for issue in analysis_result["security_issues"]:
        suggestions.append("Security issue: " + issue["issue"])

    for issue in analysis_result["style_issues"]:
        suggestions.append("Style issue: " + issue["issue"])

    for issue in analysis_result["complexity_issues"]:
        suggestions.append("Complexity issue: " + issue["issue"])

    if not suggestions:
        suggestions.append("Code looks clean. No major issues found.")

    return suggestions