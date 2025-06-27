# import ollama llm 
import os
import sys      
from dotenv import load_dotenv
from langchain_ollama import OllamaLLM    
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever


# Load environment variables from .env file
load_dotenv()   
# Get the Ollama model name from environment variables
ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2:latest")
                         
# Initialize the Ollama model
model = OllamaLLM(model=ollama_model)

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("human", """You are an expert in answering questions about a pizza restaurant.
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}""")
])
chain = prompt_template | model


# Main loop to ask questions


while  True:
    # Print a separator for clarity
    print("\n\n-------------------------------")
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    # Simulate a retriever response for reviews
    # In a real application, you would replace this with actual retrieval logic
    docs = retriever.invoke(question)
    reviews = "\n".join([doc.page_content for doc in docs])

    # Invoke the chain with the reviews and question
    result = chain.invoke({"reviews": reviews, "question":  question})

    print(result)

