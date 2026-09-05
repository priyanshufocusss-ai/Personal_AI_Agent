from ddgs import DDGS


def search_web(query):

    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=10))

    return results


def get_trust_score(url):

    official_domains = [
        "python.org",
        "docs.python.org",
        "developer.mozilla.org",
        "learn.microsoft.com",
        "ai.google.dev",
        "openai.com",
        "drdo.gov.in",
        "isro.gov.in",
        "india.gov.in"
    ]

    authority_domains = [
        "github.com",
        "stackoverflow.com",
        "wikipedia.org",
        "arxiv.org",
        "ieee.org"
    ]

    for domain in official_domains:
        if domain in url:
            return 100

    for domain in authority_domains:
        if domain in url:
            return 80

    if ".gov" in url or ".gov.in" in url:
        return 100

    if ".edu" in url:
        return 90

    return 20


def rank_results(results):

    for result in results:
        result["score"] = get_trust_score(
            result["href"]
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results