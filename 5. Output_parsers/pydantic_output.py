from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate

load_dotenv()

class Person(BaseModel):

    name: str=Field(description='Name of the Person')
    age: int=Field(gt=18,description='Age of the Person')
    place: str=Field(description='Place of the Person')


model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name , age of fictional {place} of person \n {format_instruction},',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place':'Indian'})

print(result)