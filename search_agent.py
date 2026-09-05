from search import search_web
from search import rank_results
from google import genai
from config import API_KEY
from router import get_search_query

client = genai.Client(api_key=API_KEY)

query = input("Question: ")
search_query = get_search_query(query)
print("\nSearching:", search_query)

results = search_web(search_query)

results = rank_results(results)

top_results = results[:5]

context = ""

for result in top_results:
    context += f"""
Title: {result['title']}
Link: {result['href']}
Info: {result['body']}
Trust Score: {result['score']}
"""

prompt = f"""
Answer the user's question using ONLY the provided sources.

Question:
{query}

Sources:
{context}

Rules:
- Answer in as few words as possible.
- Give the direct answer only.
- No long paragraphs.
- Use bullet points if needed.
- Mention the best source.
- Prefer higher trust score sources.
- Explain in detail ONLY if the user asks.
"""

print("\nTOP SOURCES:\n")

for result in top_results:
    print(result["title"])
    print(result["href"])
    print("Score:", result["score"])
    print()

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nAnswer:\n")
    answer = response.text.strip()

    print(answer)

except Exception as e:
    print("\nError:", e)