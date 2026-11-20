from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

LLM = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

parser  = JsonOutputParser()

template = PromptTemplate(
    template= 'Give me the name , age ,profession, net worth and species of {topic} \n format_instructions',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions}
)

chain = template | LLM | parser

result = chain.invoke({'topic':'Virat Kohli'})

print(result)