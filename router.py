def get_search_query(query):

    q = query.lower()

    # Python
    if "python" in q:
        return "site:python.org OR site:docs.python.org " + query

    # DRDO
    elif "drdo" in q:
        return "site:drdo.gov.in " + query

    # ISRO
    elif "isro" in q:
        return "site:isro.gov.in " + query

    # Aadhaar
    elif "aadhaar" in q or "aadhar" in q:
        return "site:uidai.gov.in " + query

    # ChatGPT/OpenAI
    elif "chatgpt" in q or "openai" in q:
        return "site:openai.com " + query

    # Default Search
    else:
        return query