import streamlit as st

st.title("Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Rule-based replies
    if "python" in prompt.lower():
        reply = "Python is a popular language for AI and data science."

    elif "streamlit" in prompt.lower():
        reply = "Streamlit is a Python framework for building interactive web apps."

    else:
        reply = f"You said: '{prompt}'. I'm a demo chatbot!"

    # Store and display assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    with st.chat_message("assistant"):
        st.write(reply)

# Clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()