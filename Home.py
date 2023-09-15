import streamlit as st
from huggingface_hub import hf_hub_download

st.set_page_config(
    page_title="Ajudante"
)

st.success("Modelos carregados.")

st.sidebar.success("Selecione uma página abaixo")

st.image("https://www.viajenaviagem.com/wp-content/uploads/2020/02/belo-horizonte-pampulha.jpg.webp", caption='Autoria de Thiago Lanza. Todos os direitos reservados')
st.header("Esse é o ajudante!")
st.subheader("Escolha no menu ao lado entre traduzir um texto do português para o inglês ou resumir um texto.")