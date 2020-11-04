import os

from flask import Flask, flash, request, abort, redirect, url_for
from werkzeug.utils import secure_filename

from ocr_service import convert_to_searchable_pdf_service, convert_to_unsearchable_pdf_service
from environment import UPLOAD_FOLDER

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def hello_weeocr():
    return 'Hello, WeeOCR user!!!'

@app.route('/convert_to_searchable_pdf', methods=['GET', 'POST'])
def convert_to_searchable_pdf():
    docs = request.files['document']
    docs.save(os.path.join(app.config['UPLOAD_FOLDER'], 
                           secure_filename(docs.filename)))
    
    convert_to_searchable_pdf_service(docs)
    
@app.route('/convert_to_unsearchable_pdf', methods=['GET', 'POST'])
def convert_to_unsearchable_pdf():
    docs = request.files['document']
    docs.save(os.path.join(app.config['UPLOAD_FOLDER'],
                           secure_filename(docs.filename)))
    
    convert_to_unsearchable_pdf_service(docs)
    
if __name__ == '__main__':
    app.run(debug=True)