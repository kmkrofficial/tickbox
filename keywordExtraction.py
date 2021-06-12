import spacy


def getKeywordsFromOnline(text):
    nlp = spacy.load("en_core_sci_lg")
    doc = nlp(text)
    print(doc.ents)
