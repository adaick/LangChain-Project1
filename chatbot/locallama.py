from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Set default values for the environment variables if they are not found
langchain_api_key = os.getenv("LANGCHAIN_API_KEY", "default_langchain_api_key")
langchain_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2", "true")

# Set the environment variables
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
# LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = langchain_tracing_v2

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)
## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Search the topic u want")

# ollama LLAma2 LLm 
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))