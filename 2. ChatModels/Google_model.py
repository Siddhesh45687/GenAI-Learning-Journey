from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

result = llm.invoke('What is the capital of Maharashtra')

print("".join(b["text"] for b in result.content if b["type"] == "text"))
