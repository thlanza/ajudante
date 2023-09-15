import streamlit as st
from langchain.llms import HuggingFaceHub
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


model_name = st.session_state['traducao_model']
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
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