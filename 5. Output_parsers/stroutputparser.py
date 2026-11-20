from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash',temperature=1.0)

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

template2 = PromptTemplate(
    template='Write 5 points summary on following text ./n report on {text}',
    input_variables=['text']
)

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'Manya Surve'})

print(result)