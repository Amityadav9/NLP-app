# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 11:51:28 2020

@author: Magdalena
"""

import streamlit as st
## NLP packages

import spacy
from textblob import TextBlob
from gensim.summarization import summarize
import speech_recognition as sr

#from spacy import displacy
#from collections import Counter
import en_core_web_sm

## Sumy Pkgs
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(docs):
    parser = PlaintextParser.from_string(docs,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result
    



def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(my_text)
    
    #tokens= [token.text for token in doc]
    alldata= [('Tokens: {}  Lemma: {}'.format(token.text,token.lemma_))for token in doc]
    return alldata
    
    
def entity_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(my_text)
    #entities = [(entity.text,entity.label_)for entity in doc.ents] 
    #tokens= [token.text for token in doc]
    entities= [('Tokens: {}  Label: {}'.format(entity.text,entity.label_))for entity in doc.ents]
    return entities


def speechRec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.text('Say something ....')
        audio = r.listen(source,timeout=5)
        try:
            text = r.recognize_google(audio)
            tb = TextBlob(text)
            st.subheader('You said.... {}'.format(tb))
        except:
            st.text('cannot hear you..')
            
    return tb




def main():
    """ NLP App with streamlit"""
    st.title("NLP App")
    st.subheader("Natural Language Processing")
    
    
    # Tokenization
    
    if st.checkbox("Convert to Tokens and Lemma"):
        st.subheader("Tokenizes the text")
        message = st.text_area("Enter your text")
        if st.button("Analyse"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)
    
    
    # Named Entity 
    
    
    if st.checkbox("Extract entities"):
        st.subheader("Extracts the entities from the text")
        message = st.text_area("Enter your text")
        if st.button("Extract"):
            nlp_result = entity_analyzer(message)
            st.json(nlp_result)
    
    
    
    # Sentiment Analysis
    if st.checkbox("Check Sentiments"):
        st.subheader("Finds Sentiments of the text")
        message = st.text_area("Enter your text")
        if st.button("Sentiment"):
             blob = TextBlob(message)
             result_sentiments = blob.sentiment
             st.success(result_sentiments)
    
    
    
    # Text Summarization
    
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize your text")
        message = st.text_area("Enter your text")
        summary_option = st.selectbox("Chose Your Summarizer",("genism","sumy"))
        if st.button("Summarize"):
            if summary_option == 'genism':
                st.text("Using genism")
                summary_result = summarize(message)
            elif summary_option == 'sumy':
                st.text("Using sumy")
                summary_result = sumy_summarizer(message)
            else:
                st.warning('Using default Summarizer')
                st.text("Using gensim")
                summary_result = summarize(message)
                
            st.success(summary_result)
       
        
        
    if st.checkbox("Detector"):
        st.subheader("Detects the language")
        message = st.text_area("Enter the text")
        if st.button("Detect"):
            blob = TextBlob(message)
            result_detect = blob.detect_language()
            if result_detect == 'en':
                (st.subheader("English"))
            elif result_detect == 'es':
                (st.text("Spanish"))
            elif result_detect == 'hi':
                (st.text("Hindi"))
            elif result_detect == 'fr':
                (st.text("French"))
            elif result_detect == 'de':
                (st.text("German"))
            elif result_detect == 'sk':
                (st.text("Slovak"))
            else:
                st.success(result_detect)
        
        
        

     ## Translator 
    if st.checkbox("Translator"):
        st.subheader("Tranlates the text")
        message = st.text_area("Enter the text")
        activities = ["English","German","Spanish","Slovak","Hindi","French"]
        select_options = st.selectbox("Select the language",activities)
        if st.button("Translate"):
            if select_options == 'English':
                st.text("Translates to English")
                blob = TextBlob(message)
                trans = blob.translate(to='en')
            
            elif select_options == 'German':
                st.text("Translates to German")
                blob = TextBlob(message)
                trans = blob.translate(to='de')
                
            elif select_options == 'French':
                st.text("Translates to French")
                blob = TextBlob(message)
                trans = blob.translate(to='fr')
                
            elif select_options == 'Spanish':
                st.text("Translates to Spanish")
                blob = TextBlob(message)
                trans = blob.translate(to='es')
                
            elif select_options == 'Slovak':
                st.text("Translates to Slovak")
                blob = TextBlob(message)
                trans = blob.translate(to='sk')
                
            elif select_options == 'Hindi':
                st.text("Translates to Hindi")
                blob = TextBlob(message)
                trans = blob.translate(to='hi')
            
                
                
            else:
                st.warning('Using deault translator')
                trans = blob.translate(to='en')
                
                
            st.success(trans)
            
      
    if st.checkbox("Speech Recognition"):
        st.subheader("Tranlates the speech into text")
        activities = ["English","German","Spanish","Slovak","Hindi","French"]
        select_options = st.selectbox("Select the language",activities)
        if st.button("Speech"):
            if select_options == "Slovak":
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    st.text('Say something ....')
                    audio = r.listen(source,timeout=3)
                    try:
                        text = r.recognize_google(audio)
                        tb = TextBlob(text)
                        st.subheader('You said.... {}'.format(tb))
                        tranlate = tb.translate(to='sk')
                        st.header('You said :--  {}'.format(tranlate))
                    except:
                        st.text('cannot hear you..')
                        
                        
                        
            elif select_options == "German":
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    st.text('Say something ....')
                    audio = r.listen(source,timeout=3)
                    try:
                        text = r.recognize_google(audio)
                        tb = TextBlob(text)
                        st.subheader('You said.... {}'.format(tb))
                        tranlate = tb.translate(to='de')
                        st.header('You said :--  {}'.format(tranlate))
                    except:
                        st.text('cannot hear you..')
             
                
                
            elif select_options == "Spanish":
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    st.text('Say something ....')
                    audio = r.listen(source,timeout=3)
                    try:
                        text = r.recognize_google(audio)
                        tb = TextBlob(text)
                        st.subheader('You said.... {}'.format(tb))
                        tranlate = tb.translate(to='es')
                        st.header('You said :--  {}'.format(tranlate))
                    except:
                        st.text('cannot hear you..')
                        
            elif select_options == "French":
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    st.text('Say something ....')
                    audio = r.listen(source,timeout=3)
                    try:
                        text = r.recognize_google(audio)
                        tb = TextBlob(text)
                        st.subheader('You said.... {}'.format(tb))
                        tranlate = tb.translate(to='fr')
                        st.header('You said :--  {}'.format(tranlate))
                    except:
                        st.text('cannot hear you..')
                        
                        
            elif select_options == "Hindi":
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    st.text('Say something in English....')
                    audio = r.listen(source,timeout=3)
                    try:
                        text = r.recognize_google(audio)
                        tb = TextBlob(text)
                        st.subheader('You said.... {}'.format(tb))
                        tranlate = tb.translate(to='hi')
                        st.header('You said :--  {}'.format(tranlate))
                    except:
                        st.text('cannot hear you..')
                        
                        
            else:
                speechRec()
                        
            
                        
                        
            
        
        
        
        
    
            
    
                
    st.sidebar.subheader("About the App")
    st.sidebar.text("Nlp app with streamlit")
    
    
    
    st.subheader(' ------------------------Created By :  AMIT YADAV ---------------------- :sunglasses:')
            
             
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()