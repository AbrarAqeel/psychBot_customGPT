# Psych Bot (Custom GPT)

A simple Streamlit chat application that lets users converse with open-source language models through the Hugging Face Inference API. The app is styled as "Psych Bot," a conversational assistant framed around guiding users toward inner peace and clarity, with a selectable model backend.

## Features

- Clean, styled chat interface built with Streamlit
- Model selector in the sidebar, supporting:
  - `meta-llama/Llama-3.2-1B-Instruct`
  - `tiiuae/falcon-7b-instruct`
  - `google/gemma-1.1-2b-it`
- Conversation history maintained in session state
- Automatically resets the conversation when a different model is selected
- Custom chat bubble styling for user and assistant messages

## Tech Stack

- Python
- [Streamlit](https://streamlit.io/) — front-end and app framework
- [huggingface_hub](https://huggingface.co/docs/huggingface_hub) — `InferenceClient` for calling hosted models

## Project Structure

```
psychBot_customGPT/
├── PsychBot_CustomGPT.py   # Main Streamlit application
├── requirements.txt        # Python dependencies
└── hf_token.txt             # Hugging Face API token (see Security Notes below)
```

## Prerequisites

- Python 3.9+
- A Hugging Face account and an [access token](https://huggingface.co/settings/tokens) with Inference API permissions

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AbrarAqeel/psychBot_customGPT.git
   cd psychBot_customGPT
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Hugging Face API key. The app expects a plain text file containing only your token, referenced by an absolute path (`/hf_key.txt`) in the source code. You have two options:
   - Create a file named `hf_key.txt` at the root of your filesystem (matching the path in the code), **or**
   - Update the `file_path` variable in `PsychBot_CustomGPT.py` to point to a local file, e.g. `hf_key.txt` in the project directory.

4. Run the app:
   ```bash
   streamlit run PsychBot_CustomGPT.py
   ```

5. Open the local URL Streamlit prints in your terminal (typically `http://localhost:8501`).

## Usage

1. Choose a model from the sidebar dropdown.
2. Type a message in the text box.
3. Click **Send** to get a response.
4. Switching models mid-conversation will reset the chat history.

## Security Notes

- This repository currently contains a file named `hf_token.txt`. **Never commit API keys or tokens to a public repository.** If a real token was ever pushed, treat it as compromised: revoke it immediately from your [Hugging Face settings](https://huggingface.co/settings/tokens) and generate a new one.
- Going forward, keep credentials out of version control by:
  - Adding `hf_key.txt` / `hf_token.txt` to `.gitignore`
  - Loading the token from an environment variable instead of a file, e.g.:
    ```python
    import os
    api_key = os.environ["HF_API_TOKEN"]
    ```
  - Using Streamlit's built-in [secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management) if deploying on Streamlit Community Cloud.

## Known Limitations

- The file path for the API key (`/hf_key.txt`) is hardcoded and OS-specific; it will need to be adjusted for most local setups.
- No error handling for missing or invalid API keys beyond the try/except around the inference call.
- Model responses depend on third-party model availability on the Hugging Face Inference API.

## Credits

Built by Affan & Abrar.
