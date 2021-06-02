import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st
import requests

response = requests.get("http://127.0.0.1:8000/test")
print(response)

def fonction_nlp():
    nlp = spacy.load('en_core_web_sm')
    text = 'Today is an amazing day!'
    spacy_text_blob = SpacyTextBlob("Text", text)

    nlp.add_pipe('spacytextblob')
    st.title('Sentiment app')
    user_input = st.text_input("Text", text)
    doc = nlp(user_input)

    st.write('Polarity:', round(doc._.polarity, 2))
    st.write('Subjectivity:', round(doc._.subjectivity, 2))
    return "ok"

def square(mp):
    return mp*mp
