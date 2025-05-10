import streamlit as st

st.title('Página Danger OI')

from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


if st.button("Gerar Texto"):

    response = client.responses.create(
        model="gpt-4o-mini",
        input="Conte uma historia de conto do vigário"
    )


    st.write(response.output_text)