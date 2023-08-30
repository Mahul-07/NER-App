import streamlit as st
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
st.subheader("New NER")
user_input = st.text_area("Input Text", "")
if st.button("Ner"):
    if user_input:
        doc = nlp(user_input)
        # Create a custom visualization where only the entities are highlighted
        spans = [
            {
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_,
            }
            for ent in doc.ents
        ]
        html = displacy.render(
            {"text": user_input, "ents": spans},
            style="ent",
            manual=True,
            page=False,
        )
        st.write(html, unsafe_allow_html=True)
