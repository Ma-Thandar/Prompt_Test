#pip install langchain-groq
#pip install langchain
import streamlit as st
#import chromadb
from langchain_groq import ChatGroq
import os
st.write("Current Working Directory:", os.getcwd())

llm = ChatGroq(    
    temperature=0,
    groq_api_key='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',    
    model_name='llama-3.1-8b-instant'  
)
response = llm.invoke("the man who walked on the moon first")
st.write(response.content)
#groq_api_key='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',
#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


#chroma_client = chromadb.Client()
#collection = chroma_client.create_collection(name="my_collection")
