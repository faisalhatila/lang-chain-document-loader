from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from pathlib import Path

path = Path(__file__).parent.parent / "books"

loader = DirectoryLoader(
    path=path,
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

# print(len(docs))
# print(docs[0].metadata)
print(docs[2].page_content)