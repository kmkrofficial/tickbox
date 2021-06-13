import math


def cosineSimilarity(c1, c2):
    terms = set(c1).union(c2)
    dot_prod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    mag_a = math.sqrt(sum(c1.get(k, 0) ** 2 for k in terms))
    mag_b = math.sqrt(sum(c2.get(k, 0) ** 2 for k in terms))
    return dot_prod / (mag_a * mag_b)

