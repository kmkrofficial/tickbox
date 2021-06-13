from googlesearch import search


def searchForInternetResults(query):
    search_results = search(query, stop=15)
    verified_websites = ["geeksforgeeks", "wikipedia", "livescience", "britannica"]

    final_results = []

    for result in search_results:
        for verified_website in verified_websites:
            if result.find(verified_website) != -1:
                final_results.append(result)

    return final_results
