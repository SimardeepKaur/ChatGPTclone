import os
from langchain.llms import OpenAI

# from openai import OpenAI

from dotenv import load_dotenv
import streamlit as st

# loading env variables from .env
load_dotenv()

# method to call OpenAI api
def get_openai_response(question):
    llm = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), temperature=0.6)
    response = llm.predict(question)
    return response


# starting streamlit UI
st.set_page_config(page_title="Simar's ChatBot",
                   page_icon="🧚‍♀️",
                   layout="wide"
                   )
st.header("Simar's Wisecrack Genie")

input = st.text_input("Drop your curiosity bomb here!", key='input')
submit = st.button("Tap this magic button for wisdom!")

# if clicked
if submit:
    st.subheader('Response: ')
    response = get_openai_response(input)
    st.write(response)
                         


