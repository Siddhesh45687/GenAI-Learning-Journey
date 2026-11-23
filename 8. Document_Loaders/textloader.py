from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

doc = TextLoader('8. Document_Loaders/Chhatrapati_Sambhaji_Maharaj_Information.txt',encoding='utf-8')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write 5 lines of paragraph from the following {text}',
    input_variables=['text']
)

txt = doc.load()

chain = prompt | model | parser

result = chain.invoke({'text':txt[0].page_content})

print(result)