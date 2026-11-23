from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

loader = PyPDFLoader('8. Document_Loaders/Siddhesh_Mange_Resume_Updated.pdf')

prompt = PromptTemplate(
    template='How much score you recommend for this candidate profile and performance {document}',
    input_variables=['document']
)

parser = StrOutputParser()

chain = prompt | model | parser

pdf = loader.load()

result = chain.invoke({'document':pdf})

print(result)