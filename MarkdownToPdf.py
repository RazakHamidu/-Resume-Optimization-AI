import markdown
import pdfkit

# Funzione per convertire Markdown in PDF
def markdown_to_pdf(markdown_text, output_pdf_name):
    # Converti il Markdown in HTML
    html = markdown.markdown(markdown_text)
    
    # Converti l'HTML in PDF
    pdfkit.from_string(html, output_pdf_name)
