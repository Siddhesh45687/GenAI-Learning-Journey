
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.5
)

question = "Who is the richest person in the world?"
result = llm.invoke(question)

# Extract and format the answer
content = result.content

if isinstance(content, list):
    answer = "\n".join(
        block["text"]
        for block in content
        if isinstance(block, dict) and block.get("type") == "text"
    )
else:
    answer = content

print("\n" + "=" * 60)
print("QUESTION")
print("=" * 60)
print(question)

print("\n" + "=" * 60)
print("ANSWER")
print("=" * 60)
print(answer)

print("\n" + "=" * 60)

