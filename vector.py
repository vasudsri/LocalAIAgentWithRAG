from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

print("Current working directory:", os.getcwd())
csv_path = os.path.join(os.path.dirname(__file__), "realistic_restaurant_reviews.csv")
df = pd.read_csv(csv_path)


embedding = OllamaEmbeddings(model="mxbai-embed-large:latest") 

db_location = "./chrome_langchain_db"
add_docs = not os.path.exists(db_location)

if add_docs:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
           page_content=row["Title"] + " " + row["Review"],
           metadata={
               "rating": row["Rating"],
               "date": row["Date"]
           },
           id=str(i)
        )   
        ids.append(str(i))

        documents.append(document)

# Always create or load the vector store
vector_store = Chroma(
    collection_name="restaurant_reviews",
    embedding_function=embedding,
    persist_directory=db_location
)

if add_docs:
    vector_store.add_documents(documents, ids=ids)
    print(f"Adding {len(documents)} documents to the vector store.")

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}  # Number of documents to retrieve
)