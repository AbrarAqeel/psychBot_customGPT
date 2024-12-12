import streamlit as st
from huggingface_hub import InferenceClient

# Your Hugging Face API key (replace this with your actual key)
api_key = "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"

# Initialize the Inference Client with the API key
client = InferenceClient(token=api_key)

# Streamlit App
st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        color: #666;
        margin-bottom: 20px;
    }
    .text-area {
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 10px;
    }
    .send-button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
        font-size: 1em;
    }
    .send-button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">Psych Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Guiding you towards inner peace and clarity.</div>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("Configuration")
st.sidebar.image("https://imgur.com/fUXkJLy", use_container_width=True, caption="Psych Bot Logo")
st.sidebar.markdown("Choose settings below:")

# Check if the selected model is stored in session state
if "selected_model" not in st.session_state:
    st.session_state.selected_model = "meta-llama/Llama-3.2-1B-Instruct"
    st.session_state.messages = []

# Model selection with reset logic
model_choice = st.sidebar.selectbox(
    "Select Model",
    options=[
        "meta-llama/Llama-3.2-1B-Instruct",
        "tiiuae/falcon-7b-instruct",
        "google/gemma-1.1-2b-it"
    ],
    index=0,
    help="Choose between different models for chat."
)

# Reset conversation if the model is changed
if model_choice != st.session_state.selected_model:
    st.session_state.selected_model = model_choice
    st.session_state.messages = []

# Input Box
user_input = st.text_area("Enter your message:", placeholder="Your query please", height=150, label_visibility="collapsed")

if st.button("Send", key="send_button", use_container_width=True):
    if user_input.strip():
        # Append user input to conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate response from the selected model
        try:
            response = client.chat.completions.create(
                model=model_choice,
                messages=st.session_state.messages,
                max_tokens=500
            )
            # Extract model's response
            model_reply = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": model_reply, "model": model_choice})
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display Chat History
st.subheader("Conversation")
chat_history_styles = """
<style>
.chat-container {
    background-color: #f9f9f9;
    border-radius: 12px;
    padding: 20px;
    margin-top: 20px;
}
.chat-bubble {
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 10px;
    max-width: 80%;
}

.user-bubble {
    background-color: #e8f0fe;
    color: #202124;
    text-align: left;
    align-self: flex-start;
}

.assistant-bubble {
    background-color: #d2e3fc;
    color: #202124;
    text-align: left;
    align-self: flex-end;
}
</style>
"""

st.markdown(chat_history_styles, unsafe_allow_html=True)
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f'<div class="chat-bubble user-bubble"><strong>You:</strong> {message["content"]}</div>',
            unsafe_allow_html=True
        )
    elif message["role"] == "assistant":
        st.markdown(
            f'<div class="chat-bubble assistant-bubble"><strong>Assistant:</strong> {message["content"]}</div>',
            unsafe_allow_html=True
        )
st.markdown('</div>', unsafe_allow_html=True)
