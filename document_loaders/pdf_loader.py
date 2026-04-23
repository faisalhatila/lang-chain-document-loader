from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

file_path = Path(__file__).parent / "dl-curriculum.pdf"

loader = PyPDFLoader(file_path=file_path)

docs = loader.load()

print(len(docs))
print(docs[0].metadata)
print(docs[0].page_content)