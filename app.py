import os
import json
from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from scanner import warp_image
from transformtopdf import convert_jpg_to_pdf, convert_office_to_pdf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # limit to 16MB

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scanner')
def scanner():
    return render_template('scanner.html')

@app.route('/api/scan', methods=['POST'])
def api_scan():
    if 'file' not in request.files:
        return "No file", 400
    
    file = request.files['file']
    points_str = request.form.get('points')
    points = json.loads(points_str)
    
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    output_filename = "scanned_" + filename
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    
    file.save(input_path)
    
    if warp_image(input_path, output_path, points):
        return jsonify({'result_url': '/' + output_path})
    return "Error processing image", 500

@app.route('/convert/<file_type>')
def convert_page(file_type):
    return render_template('convert.html', file_type=file_type)

@app.route('/api/convert/<file_type>', methods=['POST'])
def api_convert(file_type):
    if 'file' not in request.files:
        return "No file", 400
        
    file = request.files['file']
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)
    
    base_name = os.path.splitext(filename)[0]
    output_filename = base_name + '.pdf'
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
    
    success = False
    if file_type == 'jpg':
        success = convert_jpg_to_pdf(input_path, output_path)
    else:
        success = convert_office_to_pdf(input_path, app.config['UPLOAD_FOLDER'])
        
    if success:
        return jsonify({'result_url': '/' + output_path})
    return "Conversion failed", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)