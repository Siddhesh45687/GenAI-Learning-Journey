from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)
model2 = ChatGoogleGenerativeAI(model='gemini-3.6-flash',temperature=0.5)

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a 5 points summary of following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model1 | parser | prompt2 | model2 | parser

result = chain.invoke({'topic':'High Demanding Jobs  In India'})

print(result)

chain.get_graph().print_ascii()