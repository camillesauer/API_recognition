import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import requests
from fastapi import FastAPI


app = FastAPI()

def fonction_nlp(user_input):
    nlp = spacy.load('en_core_web_sm')
    text = 'Today is an amazing day!'
    spacy_text_blob = SpacyTextBlob("Text", text)

    nlp.add_pipe('spacytextblob')
    doc = nlp(user_input)

    return {'Polarity:': round(doc._.polarity, 2), 'Subjectivity:': round(doc._.subjectivity, 2)}


@app.get("/test")
async def root():
    return {"message": fonction_nlp()}

