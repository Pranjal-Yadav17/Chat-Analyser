import streamlit as st
import preprocess
import re
import stats
import matplotlib.pyplot as plt
import numpy as np

st.sidebar.title("Chat Analyser")

#uploading file
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
 bytes_data= uploaded_file.getvalue() #getvalue will get the value of the text file

 #converting byte code to text file
 data= bytes_data.decode("utf-8")
 df= preprocess.preprocess(data)
 
