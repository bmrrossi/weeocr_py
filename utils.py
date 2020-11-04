import os, shutil

from environment import UPLOAD_FOLDER, CONVERTIDO_FOLDER
from pdf2image import convert_from_path, convert_from_bytes

def clean_folders():
    try:
        shutil.rmtree(UPLOAD_FOLDER)
        shutil_rmtree(CONVERTIDO_FOLDER)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (UPLOAD_FOLDER, e))
        
def convert_pdf_to_image(document):
    image = convert_from_bytes(open(
        UPLOAD_FOLDER + document.filename, 'rb').read())
    
    return image

def getBytes(path):
    open_file = open(path, 'rb')
    bytes = open_file.read()
    open_file.close()
    
    return bytes
    