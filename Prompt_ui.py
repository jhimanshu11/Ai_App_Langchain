from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

st.header("Research Tool")

# Initialize the model (you need to define this)
@st.cache_resource
def load_model():
    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # or your preferred model
        huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        temperature=0.7,
        max_new_tokens=512
    )
    model = ChatHuggingFace(llm=llm)
    return model

model = load_model()

# Use text_input instead of text
user_input = st.text_input("Enter your Prompt")

if st.button("Summarize"):
    if user_input:  # Check if input is not empty
        with st.spinner("Generating response..."):
            result = model.invoke(user_input)
            st.write(result.content)
    else:
        st.warning("Please enter a prompt first!")
