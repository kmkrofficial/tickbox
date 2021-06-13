from docx import Document


def checkFormatAndReturnText(file_name):
    if file_name.endswith(".txt"):
        return getTextFromTextFile(file_name)
    elif file_name.endswith(".docx"):
        return getTextFromDocxFile(file_name)
    else:
        return "Unidentified Format"


def getTextFromTextFile(file):
    with open(file, "r") as p:
        text = p.read()
    return text


def getTextFromDocxFile(file):
    document = Document(file)
    text = ""
    for para in document.paragraphs:
        text += para.text
    return text
