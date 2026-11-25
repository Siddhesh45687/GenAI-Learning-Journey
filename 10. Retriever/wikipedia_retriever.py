
import wikipedia

# Set a descriptive User-Agent BEFORE using LangChain
wikipedia.set_user_agent(
    "GenAIPractice/1.0 (your-email@example.com)"
)

from langchain_community.retrievers import WikipediaRetriever
from dotenv import load_dotenv

load_dotenv()

retriever = WikipediaRetriever(
    top_k_results=2,
    lang="en"
)

query = "The Operation Sindoor"

try:
    result = retriever.invoke(query)

    for i, doc in enumerate(result):
        print(f"\n--- Result {i+1} ---")
        print(f"Content:\n{doc.page_content}")

except Exception as e:
    print("Error:", repr(e))


 