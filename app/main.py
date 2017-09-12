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

    filename = "default.png.csv"
    csv = request.form['csv'].strip()
    # If the textbox is filled
    if csv != '':
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w+")
        f.write(csv)
        f.close()
    # if user does not select file, browser submits an empty part without filename
    else:
        file = request.files['file']
        if file.filename == '':
            flash('Please select a CSV file to Upload!', 'error')
            return redirect(url_for('index'))
        else:
            filename = file.filename

    # If a PNG is uploaded, push it to the folder
    if request.files['image'].filename != '':
        image = request.files['image']
        imgname = image.filename
        if '.' in imgname and imgname.rsplit('.', 1)[1] == 'png':
            imgname = filename.rsplit('.', 1)[0]
            imgname = secure_filename(imgname)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], imgname))
        else:
            flash('Please select a PNG image to Upload!', 'error')
            return redirect(url_for('index'))

    # If the csv file is uploaded
    if '.' in filename and filename.rsplit('.', 1)[1] == 'csv':
        filename = secure_filename(filename)
        if filename != "default.png.csv":
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        generate_badges()
        flash(filename, 'success')
        return redirect(url_for('index'))
    else:
        flash('Only CSV file is accepted!', 'error')
        return redirect(url_for('index'))


@app.errorhandler(404)
def Not_Found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
