# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()


#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

MODEL_NAMES_GROQ = ["qwen-qwq-32b", "llama-3.3-70b-versatile"]

provider=st.radio("Select Provider:", ("Groq"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "llm_id": selected_model,
            "user_query": [user_query],
            "allow_search": allow_web_search
        }

        response=requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")


