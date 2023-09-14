import streamlit as st
from langchain.llms import HuggingFaceHub
from transformers import T5Tokenizer
from transformers import T5Model, T5ForConditionalGeneration  



#Function to return the response
def load_answer(question):
    token_name = 'unicamp-dl/ptt5-base-portuguese-vocab'
    model_name = 'phpaiola/ptt5-base-summ-xlsum'
    tokenizer = T5Tokenizer.from_pretrained(token_name )
    model_pt = T5ForConditionalGeneration.from_pretrained(model_name)
    inputs = tokenizer.encode(question, max_length=512, truncation=True, return_tensors='pt')
    summary_ids = model_pt.generate(inputs, max_length=256, min_length=32, num_beams=5, no_repeat_ngram_size=3, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0])
    return summary

#App UI starts here
st.image("https://www.viajenaviagem.com/wp-content/uploads/2020/02/belo-horizonte-pampulha.jpg.webp", caption='Autoria de Thiago Lanza. Todos os direitos reservados')
st.header("Resumo de frases")
st.subheader("Digite uma frase para que seja resumida")

#Gets the user input
def get_text():
    input_text = st.text_input("Sua frase em português: ", key="input")
    return input_text

user_input=get_text()
response = load_answer(user_input)

submit = st.button('Resumir')

if submit:

    st.subheader("Resumo:")
    st.write(response)