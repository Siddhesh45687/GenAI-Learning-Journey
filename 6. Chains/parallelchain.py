from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash',
    temperature=0.5
)

model2 = ChatGoogleGenerativeAI(
    model='gemini-3.6-flash',
    temperature=0.5)


prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate the 5 questions answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and {quiz}',
    input_variables=['quiz','notes']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

chain = prompt3 | model2 | parser

merge_chain = parallel_chain | chain 

text="""
Shivaji I (Shivaji Shahaji Bhonsale, Marathi pronunciation: [ʃiˈʋaːdʑiː ˈbʱos(ə)le]; c. 19 February 1630 – 3 April 1680)[6] was an Indian ruler and a member of the Bhonsle dynasty.[7] Shivaji inherited a fiefdom (Marathi: jagir) from his father who served as a retainer for the Sultanate of Bijapur, which later formed the genesis of the Maratha Kingdom. In 1674, he was formally crowned the Chhatrapati of his realm at Raigad Fort.[8]

Shivaji offered passage and his service to the Mughal emperor Aurangzeb to invade the declining Sultanate of Bijapur. After Aurangzeb's departure for the north due to a war of succession, Shivaji conquered territories ceded by Bijapur in the name of the Mughals.[9]: 63  Following his defeat at the hands of Jai Singh I in the Battle of Purandar, Shivaji entered into vassalage with the Mughal empire, assuming the role of a Mughal chief. During this time Shivaji also wrote a series of letters apologising to Mughal emperor Aurangzeb for his actions and requested additional honors for his services. He was later conferred with the title of Raja by the emperor.[10] He undertook military expeditions on behalf of the Mughal Empire for a brief duration.[11]

In 1674, Shivaji was crowned as the king despite opposition from local Brahmins.[9]: 87 [12] Shivaji employed people of all castes and religions, including Muslims[13] and Europeans, in his administration and armed forces.[14] Over the course of his life, Shivaji engaged in both alliances and hostilities with the Mughal Empire, the Sultanate of Golconda, the Sultanate of Bijapur and the European colonial powers. Shivaji's military forces expanded the Maratha sphere of influence, capturing and building forts, and forming a Maratha navy.

Shivaji's legacy was revived by Jyotirao Phule about two centuries after his death. Later on, he came to be glorified by Indian nationalists such as Bal Gangadhar Tilak, and appropriated by Hindutva activists.
"""

result = merge_chain.invoke({'text':text})
print(result)
