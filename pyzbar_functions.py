from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
from environment import QRCODE_FOLDER, CODE128_FOLDER
from utils import clean_folders

image_properties = {
    'text': None,
    'type': None,
}

def decode_code128(filename):
    ''' Decodifica imagem em Code128 '''
    result = decode(Image.open(CODE128_FOLDER + filename))
    text = treat_data(result)
    clean_folders()
    
    return text
    
def decode_qrcode(filename):
    ''' Decodifica imagem em qr code '''
    result = decode(Image.open(QRCODE_FOLDER + filename), symbols=[ZBarSymbol.QRCODE])
    text = treat_data(result)
    clean_folders()  
    
    return text  
    
def treat_data(data):
    ''' Trata os dados extraídos da imagem '''
    
    image_properties['text'] = str(data[0][0])
    image_properties['type'] = str(data[0][1])
    
    return data[0][0]