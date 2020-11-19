import os

from flask import Flask, flash, request, abort, redirect, url_for, jsonify
from flask import make_response
from werkzeug.utils import secure_filename

import utils

from ocr_service import convert_to_searchable_pdf_service
from environment import UPLOAD_FOLDER, CONVERTIDO_FOLDER, NOME_ARQUIVO_FINAL, QRCODE_FOLDER, CODE128_FOLDER
from pyzbar_functions import decode_code128, decode_qrcode

app = Flask('weeocr-app')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['QRCODE_FOLDER'] = QRCODE_FOLDER
app.config['CODE128_FOLDER'] = CODE128_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def hello_weeocr():
    return 'Hello, WeeOCR user!!!'

@app.route('/convert_to_searchable_pdf', methods=['GET', 'POST'])
def convert_to_searchable_pdf():
    document = request.files['document']
    document.save(os.path.join(app.config['UPLOAD_FOLDER'], 
                           secure_filename(document.filename)))
    
    convert_to_searchable_pdf_service(document)

    bytes = utils.get_bytes(CONVERTIDO_FOLDER + NOME_ARQUIVO_FINAL + '.pdf')    

    response = make_response(bytes)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachement', filename=document.filename)
    
    return response

@app.route('/get_data_from_qrcode', methods=['GET', 'POST'])
def get_data_from_qrcode():
    document = request.files['document']
    document.save(os.path.join(app.config['QRCODE_FOLDER'],
                               secure_filename(document.filename)))
    
    return decode_qrcode(document.filename)

@app.route('/get_data_from_code128', methods=['GET', 'POST'])
def get_data_from_code128():
    document = request.files['document']
    document.save(os.path.join(app.config['CODE128_FOLDER'],
                               secure_filename(document.filename)))
    
    return decode_code128(document.filename)

if __name__ == '__main__':
    app.run(debug=True)