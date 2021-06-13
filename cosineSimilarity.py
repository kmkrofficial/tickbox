from collections import Counter


def cosineSimilarity(c1, c2):

    # count word occurrences
    a_vals = Counter(c1)
    b_vals = Counter(c2)

    # convert to word-vectors
    words = list(a_vals.keys() | b_vals.keys())
    a_vect = [a_vals.get(word, 0) for word in words]  # [0, 0, 1, 1, 2, 1]
    b_vect = [b_vals.get(word, 0) for word in words]  # [1, 1, 1, 0, 1, 0]

    # find cosine
    len_a = sum(av * av for av in a_vect) ** 0.5  # sqrt(7)
    len_b = sum(bv * bv for bv in b_vect) ** 0.5  # sqrt(4)
    dot = sum(av * bv for av, bv in zip(a_vect, b_vect))  # 3
    cosine = dot / (len_a * len_b)  # 0.5669467

    return cosine