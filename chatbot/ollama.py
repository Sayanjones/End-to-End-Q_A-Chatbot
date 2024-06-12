from langchain_openai import ChatOpenAI                   ## ChatOpenAI will be helpful in interacting with LLM models
from langchain_core.prompts import ChatPromptTemplate     ## if we want to write a custom promt then ChatPromptTemplate will provide tempalte
from langchain_core.output_parsers import StrOutputParser ## whatever output or response would come from llm model that this library will show us
from langchain_community.llms import Ollama
import streamlit as st
import os                                                 ## will call all environment variables
from dotenv import load_dotenv                            ## will load all environment variables

load_dotenv()

## Langmith tracking  (monitoring, debugging, tracing)
os.environ["LANGCHAIN_TRACING_V2"]="true"                 ## we need to initialize another parameter(set true for tracing the project name that have created "Tutorial")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## creating chatbot

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With LLama2 API')
input_text=st.text_input("Search the topic u want")

## openAI LLmM call
llm=Ollama(model="llama2")
output_parser=StrOutputParser()

## chain
chain=prompt|llm|output_parser                                           ## making chain so that we can get multiple option like 'or' ..

if input_text:
    st.write(chain.invoke({'question':input_text}))               