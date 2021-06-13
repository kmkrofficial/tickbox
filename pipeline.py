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


def getCosineSimilarityFromOnline(query, file_name):
    internet_fetch = internetFetchAndKeywordExtract(query)
    answer_script = studentAnswerScriptExtract(file_name)

    average_cosine = 0
    lis = []
    for i in internet_fetch:
        cosine = cosineSimilarity.cosineSimilarity(i, answer_script)
        lis.append(cosine)
        print(cosine)
        average_cosine += cosine
    average_cosine /= len(internet_fetch)
    lis.append(average_cosine)

    json = {
        file_name: {
            "answerText": checkFormatAndReturnText(file_name),
            "keywordsInText": len(answer_script),
            "keywords": answer_script,
            "cosineSimilarity": max(lis)
        }
    }

    return json


def getCosineSimilarityFromDrive(file_name1, file_name2):
    answer_key = studentAnswerScriptExtract(file_name1)
    answer_script = studentAnswerScriptExtract(file_name2)

    cosine = cosineSimilarity(answer_key, answer_script)

    json = {
        file_name2: {
            "answerText": checkFormatAndReturnText(file_name2),
            "keywordsInText": len(answer_script),
            "keywords": answer_script,
            "cosineSimilarity": cosine
        }
    }

    return json
