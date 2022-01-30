import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')
def summ(text):
    sw = set(stopwords.words('english'))
    words = word_tokenize(text)
    ft = dict()
    for word in words:
        word=word.lower()
        if word in sw:
            continue
        if word in ft:
            ft[word]+=1
        else:
            ft[word]=1

    senten=sent_tokenize(text)
    sentenval=dict()
    for sentence in senten: 
        for word, freq in ft.items(): 
            if word in sentence.lower(): 
                if sentence in sentenval: 
                    sentenval[sentence] += freq 
                else: 
                    sentenval[sentence] = freq         

    sumval=0
    for sentence in sentenval:
        sumval+=sentenval[sentence]

    avg=int(sumval/len(sentenval))
    summary = list()
    for sentence in senten:
        if(sentence in sentenval) and (sentenval[sentence]>(1.2*avg)):
            summary.append(sentence)
    return summary
def tsm():
    st.title('Text Summarizer App')
    text = st.text_area('Enter text to be summarized',value = '',placeholder='TEXT INPUT')

    if text != '':
        suma = summ(text)
        st.write('Summarized Text:\n', suma)
    else:
        st.write("Enter Text")
