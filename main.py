import pdfplumber
import streamlit as st
import google.generativeai as genai
import os
import markdown
import pdfkit


def markdown_to_pdf(markdown_text, output_pdf_name):
    # Converti il Markdown in HTML
    html = markdown.markdown(markdown_text)
    
    # Converti l'HTML in PDF
    pdfkit.from_string(html, output_pdf_name)

def DownloadNewResume(namefile):
    with open(f"{namefile}", "rb") as file:
        btn = st.download_button(
            label="Download Resume",
            data=file,
            file_name="New Reusme.pdf",
            mime="pdf",
        )


def PromptSy(md_resume, job_desciption):
    prompt = f"""
    Ho un curriculum formattato in Markdown e una descrizione del lavoro. \
    Per favore, adatta il mio curriculum per allinearlo meglio ai requisiti del lavoro mantenendo \
    un tono professionale. Personalizza le mie competenze, esperienze e \
    risultati per evidenziare i punti più rilevanti per la posizione. \
    Assicurati che il mio curriculum rifletta ancora le mie qualifiche e punti di forza unici, \
    ma enfatizza le competenze e le esperienze che corrispondono alla descrizione del lavoro.

    ### Ecco il mio curriculum in Markdown:
    {md_resume}

    ### Ecco la descrizione del lavoro:
    {job_desciption}

    Per favore, modifica il curriculum in modo da:
    - Utilizzare parole chiave e frasi dalla descrizione del lavoro.
    - Adattare i punti elenco sotto ciascun ruolo per enfatizzare competenze e risultati rilevanti.
    - Assicurarsi che le mie esperienze siano presentate in un modo che corrisponda alle qualifiche richieste.
    - Mantenere chiarezza, concisione e professionalità in tutto il documento.

    Restituisci il curriculum aggiornato in formato Markdown."""

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
st.title("Resume Optimization 📄💼")
with st.form("my_form"):
    uploaded_file_Resume = st.file_uploader("Carica un file PDF", type="pdf")
    job_description = st.text_area("Inserisci la descrizione del Job")

    button = st.form_submit_button('Carica')
    
if button:
    if job_description is not None and  uploaded_file_Resume is not None:
        text_pdf_resume = Uploader_Pdf_Exstrat_text(uploaded_file_Resume)
        New_pdf_resume_Oz = Gemini_model(PromptSy(md_resume=text_pdf_resume, job_desciption=job_description))
        markdown_to_pdf(New_pdf_resume_Oz, "New Reusme.pdf")
        with st.container(border=True):
                st.markdown(New_pdf_resume_Oz)
                DownloadNewResume("New Reusme.pdf")

    else:
        st.warning("Non hai caricato niete")

