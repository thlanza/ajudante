import streamlit as st
from huggingface_hub import hf_hub_download
import joblib

st.set_page_config(
    page_title="Ajudante"
)

# d; downloaded_model_path = hf_hub_download(
#                                                           repo_id="CompVis/stable-diffusion-v-1-4-original",
#                                                           filename="sd-v1-4.ckpt",
#                                                           use_auth_token=True
#                                                          ); print(downloaded_model_path)'


resumo_model_name = 'phpaiola/ptt5-base-summ-xlsum'
resumo_model_filename = "pytorch_model.bin"
traducao_model_name = 'unicamp-dl/translation-pt-en-t5'
traducao_model_filename = "pytorch_model.bin"

def initialLoad():
    resumo_model = joblib.load(
        hf_hub_download(repo_id=resumo_model_name, filename=resumo_model_filename)
    )
    traducao_model = joblib.load(
        hf_hub_download(repo_id=traducao_model_name, filename=traducao_model_filename)
    )

    if 'resumo_model' not in st.session_state:
        st.session_state['resumo_model'] = resumo_model
    if 'traducao_model' not in st.session_state:
        st.session_state['traducao_model'] = traducao_model

with st.spinner('Carregando modelos...'):
    initialLoad()

st.success("Modelos carregados.")

st.sidebar.success("Selecione uma página abaixo")

st.image("https://www.viajenaviagem.com/wp-content/uploads/2020/02/belo-horizonte-pampulha.jpg.webp", caption='Autoria de Thiago Lanza. Todos os direitos reservados')
st.header("Esse é o ajudante!")
st.subheader("Escolha no menu ao lado entre traduzir um texto do português para o inglês ou resumir um texto.")