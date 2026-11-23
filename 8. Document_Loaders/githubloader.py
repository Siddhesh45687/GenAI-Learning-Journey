from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_community.document_loaders import GitLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash',
    temperature=0.5
)

repo_url = 'https://github.com/Siddhesh45687/Mental-Health-Prediction.git'

loader = GitLoader(
    clone_url=repo_url,
    repo_path="./mental_health_repo",
    branch='main'
)

prompt = PromptTemplate(
    template='Answer {question} from {text}. Include the metadata and page content. do not ignore metadata at any how',
    input_variables=['question', 'text']
)

docs = loader.load()

text = "\n\n".join(
    f"Page_content: {doc.page_content}\n"
    f"Metadata : {doc.metadata}"
    for doc in docs
    
)

docs = loader.load()


parser = StrOutputParser()


chain = prompt | model | parser

result = chain.invoke({'question':'Summarize the Readme in 10 lines paragraph',
                       'text':text,})

print(result)
