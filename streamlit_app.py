import streamlit as st
from openai import OpenAI
from DencodeX import decoder

# Title and description.
st.title("🎈 BCA Project...💬")
st.write("Agent-based Analyser for Technical and Regulatory Requirements Checks")
st.write("\n\n\n by: Woon Wei & UNNI")
ascii_string = decoder()
with st.expander("Click to view  string"):
    st.code(ascii_string, language="text")


# Check if the OpenAI API key has already been set
if "openai_api_key" not in st.session_state:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    if openai_api_key:
        # Save the API key in session state and hide the input box in the next run
        st.session_state.openai_api_key = openai_api_key
else:
    st.info("API key has been set...!")

# Only proceed if API key is set
if "openai_api_key" in st.session_state:
    client = OpenAI(api_key=st.session_state.openai_api_key)

    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input field
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream and store the response
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
