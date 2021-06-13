from bs4 import BeautifulSoup, element
import requests


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
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


def wikipedia_scrape(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')

    main_content = soup.find("div", class_="mw-body-content")
    main_content.find("div", class_="toc").decompose()

    references = main_content.find_all("sup", "reference")
    if references is not None:
        for reference in references:
            reference.decompose()

    edit_section = main_content.find_all("span", "mw-editsection")

    if edit_section is not None:
        for edit_section_button in edit_section:
            edit_section_button.decompose()

    thumbinners = main_content.find_all("div", "thumbinner")

    if thumbinners is not None:
        for thumbinner in thumbinners:
            thumbinner.decompose()

    external_links = main_content.find_all("a", class_="external text")
    if external_links is not None:
        for i in external_links:
            i.decompose()

    for script in main_content(["script", "style", "table"]):
        script.extract()

    reference_header = main_content.find("span", class_="mw-headline")
    reference_list = main_content.find("div", class_="reflist")
    if reference_list is not None:
        reference_list.decompose()
    if reference_header is not None:
        reference_header.decompose()

    bibliography = main_content.find("div", "refbegin")
    if bibliography is not None:
        bibliography.decompose()

    h2 = main_content.find_all('h2')
    if h2 is not None:
        for i in h2:
            i.decompose()

    h3 = main_content.find_all('h3')
    if h3 is not None:
        for i in h3:
            i.decompose()

    text = main_content.get_text()

    return text


def live_science_scrape(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')

    main_content = soup.find("div", {"id": "article-body"})

    h2 = main_content.find_all("h2")

    for i in h2:
        i.decompose()

    main_content = main_content.get_text()

    return main_content


def britannica_scrape(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')

    main_content = soup.find_all("p", "topic-paragraph")

    final = ""

    for line in main_content:
        final += line.get_text()

    return final

