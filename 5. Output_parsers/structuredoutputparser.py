from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

schema = [
    ResponseSchema(name='fact_1',description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2',description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Write a 3 Facts about the {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'Physics Wallah'})

print(result)