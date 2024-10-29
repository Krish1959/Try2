import streamlit as st
from openai import OpenAI
from Dencoder import decoder

# Title and description.
st.title("🎈 BCA Project...💬")
st.write( "Agent-based Analyser for Technical and Regulatory Requirements Checks" )
st.write( "\n\n\n by: Woon Wei & UNNI" )
# Dynamically generated OpenAI API key paid by UNNI (Paid)- for Testing

xxx = decoder()
with st.expander("Click to view ASCII string"):
    st.code(xxx, language="text")
    
    
'''
# Later can openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Preset OpenAI API key NOT OK ....Cannot continue.") #Change when Test is Over
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=NeoWise)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
'''
