
def get_holland_code(scores):
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return "".join([x[0] for x in sorted_scores[:3]])
