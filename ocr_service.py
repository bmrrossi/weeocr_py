try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import utils
from environment import UPLOAD_FOLDER

def convert_to_searchable_pdf_service(document):
    image = utils.convert_pdf_to_image(document)
    print(pytesseract.image_to_string(Image.open(image)))
    
def convert_to_unsearchable_pdf_service(document):
    print(document)