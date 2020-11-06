try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import utils
from environment import CONVERTIDO_FOLDER, NOME_ARQUIVO_FINAL

def convert_to_searchable_pdf_service(document):
    image = utils.convert_pdf_to_image(document)
    pdf = pytesseract.image_to_pdf_or_hocr(image[0], extension='pdf')
    
    with open(CONVERTIDO_FOLDER + NOME_ARQUIVO_FINAL + '.pdf', 'w+b') as file:
        file.write(pdf)
        
def convert_to_text_service(document):
    image = utils.convert_pdf_to_image(document)
    text = pytesseract.image_to_string(image[0])
    
    return text

