import calc
import streamlit as st
import ts
from multipage import MultiPage

st.title("Multi Apps")
#st.write("aa")
app = MultiPage()

app.add_page("Calculator App", calc.ca)
app.add_page("Text Summarizer App", ts.tsm)

app.run()