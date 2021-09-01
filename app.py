# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:04:12 2021

@author: chandan Kumar Sahoo
"""

import streamlit as st
import spacy_streamlit
import spacy
nlp = spacy.load("en_core_web_sm")
from bs4 import BeautifulSoup
from urllib.request import urlopen
def get_text(raw_url):
    page=urlopen(raw_url)
    soup=BeautifulSoup(page)
    featured_text=" ".join(map(lambda p:p.text,soup.find_all('p')))
    return featured_text
def main():
    st.title('Name Entity Recognition')
    menu=['NER','NER for URL']
    choice=st.sidebar.radio("pick a choice",menu)
    if choice=="NER":
        raw_text=st.text_area('Enter Text',"")
        if raw_text != "":
            doxc=nlp(raw_text)
            spacy_streamlit.visualize_ner(doxc,labels=nlp.get_pipe('ner').labels)
    elif choice=="NER for URL":
        raw_url=st.text_input('Enter URL',"")
        text_length=st.slider("Length to preview", 50,200)
        if raw_url != "":
            result=get_text(raw_url)
            len_of_full_text=len(result)
            len_of_short_text=round(len(result)/text_length)
            st.subheader('Text to be analyzed: ')
            st.write(result[:len_of_short_text])
            preview_docx=nlp(result[:len_of_short_text])
            spacy_streamlit.visualize_ner(preview_docx,labels=nlp.get_pipe('ner').labels)
if __name__=='__main__':
    main()        
    