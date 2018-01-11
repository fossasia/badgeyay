from flask import Flask, render_template, request, redirect, url_for, flash
from flask_compress import Compress
from werkzeug.utils import secure_filename
import os
import json
import shutil
import traceback
from svg_to_png import do_svg2png
# from argparse import ArgumentParser

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
BADGES_FOLDER = os.path.join(APP_ROOT, 'static/badges')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'secret'
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'application/json']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)

# parser = ArgumentParser()
# parser.add_argument("--dev",
#                     help="Start the server in development mode with debug=True",
#                     action="store_true")
# args = parser.parse_args()
CUSTOM_FONTS = ['monospace', 'sans-serif', 'sans', 'Courier 10 Pitch', 'Source Code Pro']


@app.route('/')
def index():
    """
    Entry point to the app
    """
    default_background = []
    for file in os.listdir(UPLOAD_FOLDER):
        if file.rsplit('.', 1)[1] == 'png' and file != 'user_defined.png':
            default_background.append(file)
    return render_template('index.html', default_background=default_background, custom_fonts=CUSTOM_FONTS)


def generate_badges(_pdf=True):
    os.system('python3 ' + APP_ROOT + '/merge_badges.py -p')


def empty_directory():
    """
    Function to check for empty directory existence
    """
    # Creates 'badges' directory if not exists
    if not os.path.exists(BADGES_FOLDER):
        os.mkdir(BADGES_FOLDER)

    # emptying previous files and folders inside the badges folder
    for file in os.listdir(BADGES_FOLDER):
        file_path = os.path.join(BADGES_FOLDER, file)
        try:
            if os.path.isfile(file_path):
                # removes the file
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # removes the directory
                shutil.rmtree(file_path)
        except Exception:
            traceback.print_exc()


@app.route('/upload', methods=['POST'])
def upload():
    """
    Function to upload the form data from the webpage
    """
    empty_directory()
    csv = request.form['csv'].strip()
    img = request.form['img-default']
    custom_font = request.form['custfont']
    file = request.files['file']

    # If default background is selected
    if img != '':
        if (img == 'user_defined.png'):
            bg_color = request.form['bg_color']
            do_svg2png(img, 1, bg_color)
        filename = img + '.csv'

    # Custom font is selected for the text
    if custom_font != '':
        json_str = json.dumps({
            'font': custom_font
        })
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'fonts.json'), "w+")
        f.write(json_str)
        f.close()

    # If the textbox is filled
    if img == '':
        img = request.files['image'].filename
        filename = request.files['image'].filename + ".csv"

    if csv != '':
        check_csv = csv.splitlines()
        count_line = 0
        for check in check_csv:
            line = check.split(',')
            if len(line) == 4:
                count_line = count_line + 1
        if count_line == len(check_csv):
            filename = img + ".csv"
            f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w+")
            f.write(csv)
            f.close()
        else:
            flash('Write Data in Correct format!', 'error')
            return redirect(url_for('index'))
    # if user does not select file, browser submits an empty part without filename
    else:
        if file.filename == '':
            flash('Please select a CSV file to Upload!', 'error')
            return redirect(url_for('index'))

    # if user does not select file, browser submits an empty part without filename
    if request.files['image'].filename != '':
        image = request.files['image']
        imgname = image.filename
        if '.' in imgname:
            imgname = filename.rsplit('.', 1)[0]
            imgname = secure_filename(imgname)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        else:
            flash('Please select a PNG image to Upload!', 'error')
            return redirect(url_for('index'))

    # If a PNG is uploaded, push it to the folder
    if filename.find("png.csv") == -1:
        if img == '':
            flash('Please upload an image in \'PNG\' format!', 'error')
            return redirect(url_for('index'))

    # If the csv file is uploaded
    if '.' in filename and filename.rsplit('.', 1)[1] == 'csv':
        filename = secure_filename(filename)
        if csv == '' and filename == img + ".csv":
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        generate_badges()

        # Remove the uploaded files after job in done
        os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], 'fonts.json')):
            os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], 'fonts.json'))
        try:
            if 'imgname' in locals():
                os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], imgname))
        except Exception:
            traceback.print_exc()

        if True:
            flash(filename.replace('.', '-'), 'success-pdf')
            os.rename(os.path.join(BADGES_FOLDER + "/" + filename + ".badges.pdf"),
                      os.path.join(BADGES_FOLDER + "/" + filename.replace('.', '-') + "-badges.pdf"))

        return redirect(url_for('download'))


@app.route('/download')
def download():
    return render_template("download.html")


@app.route('/guide')
def guide():
    """
    Entry point for guide webpage
    """
    return render_template('guide.html')


@app.errorhandler(404)
def Not_Found(e):
    """
    Function for invalid page / Page not existence
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def Internal_Server_Error(e):
    """
    Function for Internal_Server_Error
    """
    trace = traceback.format_exc()
    return render_template('500.html', exception=trace), 500


if __name__ == '__main__':
    # app.run(debug=args.dev)
    app.run(debug=True)
