from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./dl-curriculum.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10,
    separator=''
)

texts = splitter.split_documents(docs)

print(texts[1])
 