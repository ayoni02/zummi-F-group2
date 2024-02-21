from transformers  import pipeline
import streamlit as st

st.write("welcome")
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
res = classifier("i am a good boy", ["POSITIVE", "NEGATIVE", "NEUTRAL"])
st.write(res)

def main():
    text = st.text_input("Enter the text to classify: ") #input("Enter the text to classify: ")
    #labels = ["POSITIVE", "NEGATIVE", "NEUTRAL"]
    if text:
        #results = classifier(text)
        st.write("great")
    else:
        st.write("Please enter some text to classify")
    
main()