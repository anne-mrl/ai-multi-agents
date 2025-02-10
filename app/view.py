import streamlit as st
import requests

# Define FastAPI URLs
API_URL = "http://127.0.0.1:5000/ask/"
HISTORY_URL = "http://127.0.0.1:5000/history/"

# Streamlit page config
st.set_page_config(page_title="AI Assistant", page_icon="🤖")

# App title
st.title("Welcome to AI Assistant web page")

# User prompt
question = st.text_input("Ask your question :", "")

# To send question
if st.button("Send"):
    if question:
        with st.spinner("Searching..."):
            response = requests.get(API_URL, params={"question": question})
            if response.status_code == 200:
                result = response.json()["response"]
                st.success("I found something for you!")
                st.write(result)
            else:
                st.error("AI request error.")
    else:
        st.warning("Please enter a question.")

# Get hystory
st.subheader("Requests history")
history_response = requests.get(HISTORY_URL)
if history_response.status_code == 200:
    history_data = history_response.json()["history"]
    if history_data:
        for entry in history_data:
            with st.expander(f"{entry['question']} ({entry['timestamp']})"):
                st.write(f"Response : {entry['response']}")
    else:
        st.info("No request saved.")
else:
    st.error("Unable to get history.")
