import pickle
import streamlit as st
from os import path
import numpy as np

st.title("Phishing Website Detection System")

filename="kn.pk"
with open(path.join(filename),'rb') as f:
    lr=pickle.load(f)
    
Have_At=st.number_input("Have At")
URL_Length=st.number_input("URL Length")
URL_Depth=st.number_input("URL Depth")
TinyURL=st.number_input("TinyURL")
Prefix_Suffix=st.number_input("Prefix/Suffix")
DNS_Record=st.number_input("DNS Record")
Web_Traffic=st.number_input("Web Traffic")
Domain_Age=st.number_input("Domain Age")
Domain_End=st.number_input("Domain End")
iFrame=st.number_input("iFrame")
Web_Forwards=st.number_input("Web Forwards")
if st.button("predict") :
    pred=lr.predict(np.array([[Have_At,URL_Length,URL_Depth,TinyURL,Prefix_Suffix,DNS_Record,Web_Traffic,Domain_Age,Domain_End,iFrame,Web_Forwards]]))
    if pred==1:
        st.write("the website is phishing")
    else :
        st.write("the website is legitimate")
