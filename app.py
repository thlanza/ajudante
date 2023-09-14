import streamlit as st
from st_pages import Page, add_page_title, show_pages

add_page_title()  

show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("pages/resumo.py", "Resumo", ":books:"),
        Page("pages/traducao.py", "Traducao", ":page_facing_up:"),
    ]
)


st.image("https://www.viajenaviagem.com/wp-content/uploads/2020/02/belo-horizonte-pampulha.jpg.webp", caption='Autoria de Thiago Lanza. Todos os direitos reservados')
st.header("Esse é o ajudante!")
st.subheader("Escolha no menu ao lado entre traduzir um texto do português para o inglês ou resumir um texto.")