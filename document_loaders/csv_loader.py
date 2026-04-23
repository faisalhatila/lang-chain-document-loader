from langchain_community.document_loaders import CSVLoader
from pathlib import Path


file_path = Path(__file__).parent.parent / "resources/Social_Network_Ads.csv"
loader = CSVLoader(file_path=file_path)

data = loader.load()

print(data[0])