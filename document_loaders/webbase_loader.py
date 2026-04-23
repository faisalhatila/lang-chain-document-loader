from langchain_community.document_loaders import WebBaseLoader
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template='Answer the following question \{question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

# url='https://www.flipkart.com/apple-macbook-pro-m4-24-gb-1-tb-ssd-macos-sequoia-mx2j3hn-a/p/itmcd041a34ee857?pid=COMH64PYTA4MYWAV&lid=LSTCOMH64PYTA4MYWAVAE2OWK&marketplace=FLIPKART&q=maccbook+m4+pro&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=c074ed17-d4ca-4ce4-84f9-6edf1a453539.COMH64PYTA4MYWAV.SEARCH&ppt=None&ppn=None&ssid=jgzffkntuo0000001776961904206&qH=297243dade866982&ov_redirect=true'
url='https://www.amazon.com/Apple-2026-MacBook-Laptop-10-core/dp/B0GR1FWR38/ref=sr_1_1?crid=3V9SCV6X3J4LR&dib=eyJ2IjoiMSJ9.L42835qEeIgeOy5XtEzJzeq6Zj7IqcwBZjNCfX5HKz-sUqmURWfpwhJe5oowjsrmkZt3I6aDD6G4GGkqjYd3Oc7GhkKS0nwhNUS_TM6GKtTm2m8Jr0fjd_qrRCf9QIluGHDGTy0WEoBIpSggnS83cV5K7C00IBSN6m3A85D0IX8sozaB_FSkN6MP2QNu2bA8lnJ760vgrDBBryry-NVuGGozbsh6whf2rqtgH-WVpFU.QxJgUfeM7hSbyrli4gofFfkNTok6NDhKnQGOroCTkGY&dib_tag=se&keywords=macbook+pro+m5&qid=1776963662&sprefix=macbook+pro+m%2Caps%2C708&sr=8-1'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'What is the product we are talking about?','text':docs[0].page_content})

print(result)