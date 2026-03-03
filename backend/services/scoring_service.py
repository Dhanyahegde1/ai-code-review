def calculate_score(analysis_result):
    score = 100
    score -= len(analysis_result["syntax_errors"]) * 30
    score -= len(analysis_result["security_issues"]) * 20
    score -= len(analysis_result["style_issues"]) * 10
    score -= len(analysis_result["complexity_issues"]) * 5
    return max(score, 0)