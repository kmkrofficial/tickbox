from bs4 import BeautifulSoup
import requests
from keywordExtraction import getKeywordsFromOnline


def geeksforgeeks_scrape(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')
    article = soup.find("article", class_="content")

    code_containers = article.findAll("div", class_="code-container")
    code_outputs = article.find("div", class_="code-output")

    article.find("div", class_="title").decompose()
    article.find("div", class_="media").decompose()
    if code_containers is not None:
        for code_container in code_containers:
            code_container.decompose()
    if code_outputs is not None:
        for code_output in code_outputs:
            code_output.decompose()

    for script in article(["script", "style", "table"]):
        script.extract()  # rip it out

    text = article.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = list(phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    # text = '\n'.join(chunk for chunk in chunks if chunk)
    return ''.join(chunks)


print(getKeywordsFromOnline(geeksforgeeks_scrape("https://www.geeksforgeeks.org/file-handling-python/")))

