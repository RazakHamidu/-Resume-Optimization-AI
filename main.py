import pdfplumber
import streamlit as st



def Uploader_Pdf_Exstrat_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:  
        for page in pdf.pages:   
            return page.extract_text()

uploaded_file = st.file_uploader("Carica un file PDF", type="pdf")
