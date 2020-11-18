from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image

image_properties = {
    'text': None,
    'type': None,
    'width': None,
    'height': None
}

def decode_code128(image_path):
    result = decode(Image.open(image_path))
    treat_data(result)
    
def decode_qrcode(image_path):
    result = decode(Image.open(image_path), symbols=[ZBarSymbol.QRCODE])
    treat_data(result)
    
def treat_data(data):
    ''' Trata os dados extraídos da imagem '''
    pass