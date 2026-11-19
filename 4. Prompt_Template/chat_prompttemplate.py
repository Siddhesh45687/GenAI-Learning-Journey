from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

messages = [
    SystemMessage(content='You are a helpful assitant'),
    HumanMessage(content='Tell me about Maharashtra')
]

result = llm.invoke(messages)

print("".join(b["text"] for b in result.content if b["type"] == "text" ))