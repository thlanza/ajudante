import streamlit as st
from langchain.llms import HuggingFaceHub
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from huggingface_hub import hf_hub_download

with st.spinner('Carregando modelos...'):
    traducao_model_name = 'unicamp-dl/translation-pt-en-t5'
    tokenizer = AutoTokenizer.from_pretrained(traducao_model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(traducao_model_name)
    pten_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer)


#Function to return the response
def load_answer(question):
    return pten_pipeline(question)[0]["generated_text"]

#Gets the user input
def get_text():
    input_text = st.text_input("Sua frase em português: ", key="input")
    return input_text

user_input=get_text()
response = load_answer(user_input)

submit = st.button('Traduzir para inglês')



if submit:

    st.subheader("Answer:")
    st.write(response)