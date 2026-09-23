import streamlit as st
from ollama import chat

# Page title
st.title("My Local AI Chatbot")

# Keep chat history saved between messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages on screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box at the bottom for user to type
user_input = st.chat_input("Type your message here...")

if user_input:
    # Save and show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from local Ollama model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(
                model="llama3.2:1b",
                messages=st.session_state.messages
            )
            reply = response.message.content
            st.write(reply)

    # Save AI's reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})