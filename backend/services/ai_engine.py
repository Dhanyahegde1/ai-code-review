#rule_based ai
import subprocess
import time
from datetime import datetime

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
    capture_output=True,
    encoding="utf-8",
    errors="replace"
)

    return result.stdout.strip()

# adding timestamp for each ai-models
def run_ai_engine(code, analysis_result):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    start_total = time.time()

    # Rule based timing
    start_rule = time.time()
    rule_suggestions = rule_based_ai(analysis_result)
    rule_time = time.time() - start_rule

    # LLM timing
    start_llm = time.time()
    llm_result = llm_suggestions(code)
    llm_time = time.time() - start_llm

    total_time = time.time() - start_total

    return {
        "timestamp": timestamp,
        "rule_based_time_in_ms": round(rule_time * 1000, 3),
        "llm_time_in_sec": round(llm_time, 3),
        "total_time_in_sec": round(total_time, 3),
        "rule_based_suggestions": rule_suggestions,
        "llm_suggestions": llm_result
    }