from langchain_community.document_loaders import TextLoader,WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash',temperature=0.5)

url = "https://www.amazon.com/Acer-Processor-GeForce-Keyboard-ANV16-I31-54PT/dp/B0CJCNL315/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.9d197147-11a6-45c5-8993-7d0f4d56abb2&dib=eyJ2IjoiMSJ9.r0igiUh86qiKGPGNnwjjObq4DNM5-gnP8kKgnelRmNs8fCcW4eoCJn9-J9CL8v_C_iT147KRSBNDxf7LgUA2xwLnpc_bS8bKRrXYRl2YSOTnlxNSBi3WYPU51ZQx5nSGkwdDh24lgbbpxcRvbFe6sFqiMc_UYfAOos5mU9Rte3l4IDeuY8QCLyN7Pb6P8uBmhXiAILcIlU66etbAlAHd325HCWmPtWUin4tkSW6LGSE.bs8ouz-u5_2wUjmc25onbem9jlHLCvAt5leILXQAdJg&dib_tag=se&keywords=laptops&pd_rd_r=1584c1f4-96db-4854-945c-01eb22c34bcc&pd_rd_w=3Jwaj&pd_rd_wg=xQGDB&qid=1793983780&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

loader = WebBaseLoader(url)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the text \n {text}',
    input_variables=['text','question']
)

web = loader.load()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'question':'What is the price and features in this laptop ?','text':web[0].page_content})

print(result)