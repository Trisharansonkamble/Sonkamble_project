import streamlit as st
import pandas as pd

name = st.text_input("Enter Your Name : ")
fname = st.text_input("entre Your Father Name : ")
adr = st.text_area("Entre Your Text :")
classdata = st.selectbox("Entre Your Class :",(10,11,12))

button = st.button("Done")
if button :
    st.markdown(f"""
Name : {name}
Father Name : {fname}
address :{adr}
class : {classdata}""")