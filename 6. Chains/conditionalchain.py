from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field,BaseModel
from langchain_core.prompts import PromptTemplate
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.6-flash',temperature=0.5)

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template='Classify the following sentiment of the feedback into positive and negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = prompt | model | parser

result = chain.invoke({'feedback':'This Mobile Battery is Fantastic'}).sentiment

print(result)