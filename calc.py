import streamlit as st

def ca():
    st.title("Calculator App")
    try:
        x = st.number_input("Enter number 1",min_value=1)
        y = st.number_input("Enter number 2",min_value=1)
        op = {'Add':(x+y),'Subtract':(x-y),'Multiply':(x*y),'Divide':(x/y)}
        opt = st.selectbox("Choose one",(op.keys()))
        st.write("Result:",op.get(opt))
    except:
        st.write("Enter numbers for results")
