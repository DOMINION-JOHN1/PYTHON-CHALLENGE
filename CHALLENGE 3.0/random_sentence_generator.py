import random

articles = ["the", "a", "one", "some", "any"]
nouns = ["boy", "girl", "dog", "town", "car"]
verbs = ["drove", "jumped", "ran", "walked", "skipped"]
prepositions = ["to", "from", "over", "under", "on"]


def generate_sentence():
    sentence = [random.choice(articles), random.choice(nouns), random.choice(verbs), random.choice(prepositions), random.choice(articles), random.choice(nouns)]
    return " ".join(sentence).capitalize() + "."

[print(generate_sentence()) for _ in range(20)]

