import pickle
import streamlit as st
from os import path
import numpy as np

st.title("phishing website detection app")

filename="kn.pk"
with open(path.join("model",filename),'rb') as f:
    lr=pickle.load(f)
    

Have_At=st.number_input("e")
URL_Length=st.number_input("ee")
URL_Depth=st.number_input("r")
TinyURL=st.number_input("yyy")
Prefix_Suffix=st.number_input("h")
DNS_Record=st.number_input("s")
Web_Traffic=st.number_input("f")
Domain_Age=st.number_input("ff")
Domain_End=st.number_input("v")
iFrame=st.number_input("vv")
Web_Forwards=st.number_input("fuck")
if st.button("predict")
    pred=lr.predict(np.array([[Have_At,URL_Length,URL_Depth,TinyURL,Prefix_Suffix,DNS_Record,Web_Traffic,Domain_Age,Domain_End,iFrame,Web_Forwards]]))
    if pred==1:
        st.write("the website is phishing")
    else :
        st.write("the website is not phishing")