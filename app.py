import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
def gen_resp(query):
    response=model.generate_content(query)
    return response.text
st.set_page_config("Chatbot")
st.subheader("QA Chatbot")
query=st.text_input("Ask a question:")
button=st.button("Submit")
if button:
    result=gen_resp(query)
   # st.write(st.markdown(result))
    st.markdown(result)