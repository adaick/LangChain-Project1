from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set default values for the environment variables if they are not found
openai_api_key = os.getenv("OPENAI_API_KEY", "default_openai_api_key")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY", "default_langchain_api_key")
langchain_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2", "true")

# Set the environment variables
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
# LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = langchain_tracing_v2

## prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the queries!!"),
        ("user","Question:{question}")
    ]
)

## stramlit framework
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Search the topic you want.....")

## OpenAI LLMs 
llm = ChatOpenAI(model = "gpt-3.5-turbo")
out_parser = StrOutputParser()
chain = prompt|llm|out_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))