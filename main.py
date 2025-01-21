import pdfplumber

# Percorso del file PDF 
pdf_path = "Luca Rossi.pdf"
# Apertura del PDF con pdfplumber
def Uploader_Pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:  
        for page in pdf.pages:   
            print(page.extract_text())

Uploader_Pdf(pdf_path   )