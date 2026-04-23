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
    template='Write a 5 line summary for the following poen \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

file_path = Path(__file__).parent / "cricket.txt"

loader = TextLoader(file_path=file_path, encoding='utf-8')

docs = loader.load()

# print(type(docs))
# print(len(docs))
# print(type(docs[0]))
# print(docs[0])

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})
print(result)