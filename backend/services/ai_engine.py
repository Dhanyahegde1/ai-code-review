#rule_based ai
import subprocess

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

# open-source llm for suggestions
def llm_suggestions(code: str) -> str:
    prompt = f"Review this Python code and suggest improvements:\n\n{code}"

    result = subprocess.run(
        ["ollama", "run", "phi3:mini"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()