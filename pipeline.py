import cosineSimilarity
import linkFetch
from extractText import checkFormatAndReturnText
from keywordExtraction import getKeywords
from scrapeWebsite import scrape_identifier


def internetFetchAndKeywordExtract(query):

    links_obtained = linkFetch.searchForInternetResults(query)

    answer_keys = []
    for linkObtained in links_obtained:
        answer_keys.append(scrape_identifier(linkObtained))

    answer_key_keywords_extracted = []
    for answer_key in answer_keys:
        answer_key_keywords_extracted.append(getKeywords(answer_key))

    return answer_key_keywords_extracted


def studentAnswerScriptExtract(file):
    text = checkFormatAndReturnText(file)
    return getKeywords(text)


def getCosineSimilarity(query, file_name):

    internet_fetch = internetFetchAndKeywordExtract(query)
    answer_script = studentAnswerScriptExtract(file_name)

    average_cosine = 0
    for i in internet_fetch:
        cosine = cosineSimilarity.cosineSimilarity(i, answer_script)
        print(cosine)
        average_cosine += cosine

    average_cosine /= len(internet_fetch)
    print(average_cosine)


getCosineSimilarity("Amoeba", "static/sample.docx")