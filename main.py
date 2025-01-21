import pdfplumber
import streamlit as st
import google.generativeai as genai
import os
from reportlab.pdfgen import canvas

def Creatpdf(text):
    # Creazione di un file PDF
    c = canvas.Canvas("output.pdf")

    # Specifica un font con supporto Unicode
    c.setFont("Helvetica", 12)

    c.drawString(100, 750, text)

    c.save()
    print("PDF creato con successo!")





def PromptSy(md_resume, job_desciption):
    prompt = f"""
    I have a resume formatted in Markdown and a job description. \
    Please adapt my resume to better align with the job requirements while \
    maintaining a professional tone. Tailor my skills, experiences, and \
    achievements to highlight the most relevant points for the position. \
    Ensure that my resume still reflects my unique qualifications and strengths \
    but emphasizes the skills and experiences that match the job description.

    ### Here is my resume in Markdown:
    {md_resume}

    ### Here is the job description:
    {job_desciption}

    Please modify the resume to:
    - Use keywords and phrases from the job description.
    - Adjust the bullet points under each role to emphasize relevant skills and achievements.
    - Make sure my experiences are presented in a way that matches the required qualifications.
    - Maintain clarity, conciseness, and professionalism throughout.

    Return the updated resume in Markdown format.

    """
    return prompt

def Gemini_model(prompt):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def Uploader_Pdf_Exstrat_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:  
        for page in pdf.pages:   
            return page.extract_text()

with st.form("my_form"):
    uploaded_file_Resume = st.file_uploader("Carica un file PDF", type="pdf")
    job_description = st.text_area("Job_description")

    button = st.form_submit_button('Carica')
    
    if button:
        if job_description is not None and  uploaded_file_Resume is not None: #Se la descrizione e pdf sono caricati continua se no mostra alert
            text_pdf_resume = Uploader_Pdf_Exstrat_text(uploaded_file_Resume)
            New_pdf_resume_Oz = Gemini_model(PromptSy(md_resume=text_pdf_resume, job_desciption=job_description))
            Creatpdf(New_pdf_resume_Oz)  
            
        else:
            st.warning("Non hai caricato niete")