from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

Embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001',output_dimensionality=42)

result = Embedding.embed_query("Who is the God of Bodybuilding")

print(str(result))
