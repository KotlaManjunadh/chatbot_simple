from langchain import HuggingFaceHub
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
#import os

#calling api
def get_response_ai(question=''):
    llm = HuggingFaceHub(repo_id='google/flan-t5-large', model_kwargs={'temperature':0})
    response = llm.predict(question)
    return response
# app creation

st.set_page_config(page_title= 'Chatbot')
st.header('Ask some Question')
input = st.text_input('Enter Your query',key = 'input')
output = get_response_ai(str(input))
submit = st.button('Ask')
if submit:
    output = get_response_ai(str(input))
    st.header('Answer is:')
    st.write(output)