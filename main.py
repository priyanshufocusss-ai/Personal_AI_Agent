print("=== Priyanshu AI Agent ===")
from google import genai
from config import API_KEY

client = genai.Client(api_key=API_KEY)

# Read profile
with open("profile.txt", "r") as file:
    profile = file.read()

# Read memory
with open("memory.txt", "r") as file:
    memory = file.read()

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    prompt = f"""
    User Profile:
    {profile}

    Previous Memory:
    {memory}

    Rules:
    - Improve the user's English.
    - Keep answers concise.

    User Message:
    {user}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_reply = response.text

        print("\nAI:", ai_reply)

        # Save memory
        with open("memory.txt", "a") as file:
            file.write(f"\nUser: {user}\n")
            file.write(f"AI: {ai_reply}\n")

    except Exception as e:
        print("\nGemini Error:", e)
        continue