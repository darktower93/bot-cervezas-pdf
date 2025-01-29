import os
import json
import pdfplumber
import re
from unidecode import unidecode

def normalizar_texto(texto):
    texto = unidecode(texto).lower()
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    return re.sub(r'\s+', ' ', texto).strip()

def procesar_pdf(pdf_path, json_path):
    cervezas = []
    patron = re.compile(
        r'^(?:[A-Z]{2,}\d+[-/]?\d*\s+)?(.+?)\s+(\d{1,3}(?:[.,]\d{1,2})?)\s*€.*$',
        re.IGNORECASE | re.VERBOSE
    )
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split('\n'):
                    match = patron.match(line.strip())
                    if match:
                        nombre = normalizar_texto(match.group(1)).title()
                        precio = f"{match.group(2).replace(',', '.')} €"
                        cervezas.append({"nombre": nombre, "precio": precio})
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(cervezas, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    procesar_pdf(
        os.path.join('pdfs', 'cervezas.pdf'), 
        os.path.join('..', 'cervezas.json')
    )
