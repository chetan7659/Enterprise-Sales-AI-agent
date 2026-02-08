import streamlit as st
import sys
import os
import base64

# Add backend to path so imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, '..'))
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

from agent.nl_sql_agent import NLSQLAgent

st.set_page_config(page_title="Sales Assistant AI", layout="centered", initial_sidebar_state="collapsed")

# --- Custom CSS for Chat Layout ---
def set_custom_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: transparent;
        }
        /* Chat container styling */
        .stChatMessage {
            background-color: transparent;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
            color: white;
            text-shadow: 1px 1px 2px black;
        }
        .stChatMessage[data-testid="stChatMessageUser"] {
             background-color: transparent;
             border: 1px solid rgba(255, 255, 255, 0.2);
        }
        /* Sticky footer input */
        .stChatInput {
            position: fixed;
            bottom: 0px;
            padding-bottom: 20px;
            z-index: 1000;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Background Image Logic ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_from_file(file_path):
    if os.path.exists(file_path):
        bin_str = get_base64_of_bin_file(file_path)
        ext = file_path.split('.')[-1]
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/{ext};base64,{bin_str}");
                background-attachment: fixed;
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Apply styles
set_custom_css()
bg_file = os.path.join(current_dir, 'background.jpg')
set_bg_from_file(bg_file)

st.markdown("""
<div style="background-color: rgba(0, 0, 0, 0.6); padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
    <h1 style="color: white; margin: 0;">📊 Sales Assistant AI</h1>
    <div style="color: #ddd; font-size: 1.2em; margin-top: 10px;">NL-to-SQL • Gemini 2.5 • Snowflake</div>
</div>
""", unsafe_allow_html=True)

# Initialize agent
if "agent" not in st.session_state:
    st.session_state.agent = NLSQLAgent()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input (Chat Interface)
if prompt := st.chat_input("Ask a sales question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.answer(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
