# import spacy
# from spacytextblob.spacytextblob import SpacyTextBlob
from fastapi import FastAPI


app = FastAPI()

def fonction_nlp(user_input):
    # nlp = spacy.load('en_core_web_sm')
    text = 'Today is an amazing day!'
    # spacy_text_blob = SpacyTextBlob("Text", text)

    # nlp.add_pipe('spacytextblob')
    # doc = nlp(user_input)

    # return {'Polarity:': round(doc._.polarity, 2), 'Subjectivity:': round(doc._.subjectivity, 2)}
    return {'Polarity:': 'positif', 'Subjectivity:': 'concret'}

@app.get("/{user_input}")
async def root(user_input):
    return fonction_nlp(user_input)

