from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a linkedIn post on {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-4-argon',temperature=0.5)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedIn':RunnableSequence(prompt1,model,parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result)