import streamlit as st

st.title('Página Danger OI s')

from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


if st.button("Gerar Texto"):
    with st.spinner("Gerando texto...", show_time=True): 
        response = client.responses.create(
            model="gpt-4o-mini",
            input="Conte uma historia de conto do vigário"
            stream=True
        )


        st.write_stream(response)