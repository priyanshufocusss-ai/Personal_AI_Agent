from search import search_web
from search import rank_results

results = search_web("site:python.org What is Python")

results = rank_results(results)

for result in results:

    print()
    print("Score :", result["score"])
    print("Title :", result["title"])
    print("Link  :", result["href"])