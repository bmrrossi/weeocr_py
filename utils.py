import os, shutil

from environment import UPLOAD_FOLDER, CONVERTIDO_FOLDER, QRCODE_FOLDER, CODE128_FOLDER
from pdf2image import convert_from_path, convert_from_bytes

def clean_folders():
    try:
        shutil.rmtree(UPLOAD_FOLDER)
        shutil_rmtree(CONVERTIDO_FOLDER)
        shutil_rmtree(QRCODE_FOLDER)
        shutil_rmtree(CODE128_FOLDER)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (UPLOAD_FOLDER, e))
        
def convert_pdf_to_image(document):
    image = convert_from_bytes(open(
        UPLOAD_FOLDER + document.filename, 'rb').read())
    
    return image

def get_bytes(path):
    open_file = open(path, 'rb')
    bytes = open_file.read()
    open_file.close()
    
    return bytes
    