from googlesearch import search

query = "What is encapsulation in java?"

search_results = search(query, stop=15)
verified_websites = ["geeksforgeeks", "w3schools", "programiz", "javarevisited"]

final_results = []

for result in search_results:
    for verified_website in verified_websites:
        if result.find(verified_website) != -1:
            final_results.append(result)

for i in final_results:
    print(i)