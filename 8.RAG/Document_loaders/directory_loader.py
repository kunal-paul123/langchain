from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="./Books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

# print(len(docs))

# print(docs[30].page_content)
# print(docs[30].metadata)

for doc in docs:
    print(doc.metadata)

