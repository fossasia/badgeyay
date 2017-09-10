from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form
from werkzeug.utils import secure_filename
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
	return render_template('index.html')

def generate_badges():
    os.system(os.path.join(app.config['UPLOAD_FOLDER'], 'merge_badges.sh'))

@app.route('/upload', methods=['POST'])
def upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('Please select a CSV file to Upload!', 'error')
        return redirect(url_for('index'))

    file = request.files['file']
    filename = file.filename
    # if user does not select file, browser submits an empty part without filename
    if filename == '':
        flash('Please select a CSV file to Upload!', 'error')
        return redirect(url_for('index'))

    if '.' in filename and filename.rsplit('.', 1)[1] == 'csv':
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        generate_badges()
        flash('Your Badge has been successfully created!', 'success')
        return redirect(url_for('index'))
    else:
    	flash('Only CSV files is accepted!', 'error')
    	return redirect(url_for('index'))

@app.errorhandler(404)
def Not_Found(e):
	return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()