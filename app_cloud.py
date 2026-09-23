import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load the API key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="Pixel AI", page_icon="💠")

# Title
st.title("💠 Pixel AI")
st.caption("Your smart little AI companion, always here to help")

# Avatars
USER_AVATAR = "🧑"
BOT_AVATAR = "💠"

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    avatar = USER_AVATAR if msg["role"] == "user" else BOT_AVATAR
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.write(user_input)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "system", "content": "You are Pixel AI, a smart and helpful AI assistant."},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})