import spacy


def getKeywords(text):
    nlp = spacy.load("en_core_sci_lg")
    doc = nlp(text)
    entities = doc.ents
    result = []
    for entity in entities:
        string = str(entity).strip()
        if string not in result:
            result.append(string)
    return result


