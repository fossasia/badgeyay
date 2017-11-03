from flask import Flask, render_template, request, redirect, url_for, flash
from flask_compress import Compress
from werkzeug.utils import secure_filename
import os
import shutil
import uuid
import traceback
import generate_csv_eventyay
from svg_to_png import do_svg2png

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
BADGES_FOLDER = os.path.join(APP_ROOT, 'static/badges')

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'secret'
COMPRESS_MIMETYPES = ['text/html', 'text/css', 'application/json']
COMPRESS_LEVEL = 6
COMPRESS_MIN_SIZE = 500
Compress(app)


@app.route('/')
def index():
    default_background = []
    for file in os.listdir(UPLOAD_FOLDER):
        if file.rsplit('.', 1)[1] == 'png':
            default_background.append(file)
    return render_template('index.html', default_background=default_background)


def generate_badges(_zip=False, _pdf=False):
    if _zip and _pdf:
        os.system('python3 ' + APP_ROOT + '/merge_badges.py -z -p')
    elif _zip == True and _pdf == False:
        os.system('python3 ' + APP_ROOT + '/merge_badges.py -z')
    else:
        os.system('python3 ' + APP_ROOT + '/merge_badges.py -p')


def empty_directory():
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
    empty_directory()
    csv = request.form['csv'].strip()
    img = request.form['img-default']
    eventyay_url = request.form['eventyay_url'].strip()
    file = request.files['file']
    _pdf = True if request.form.get('pdf') == 'on' else False
    _zip = True if request.form.get('zip') == 'on' else False

    if not _pdf and not _zip:
        flash('Please select a download filetype!', 'error')
        return redirect(url_for('index'))
    if file.filename == '' and csv == '':
            flash('Please select a CSV file to Upload!', 'error')
            return redirect(url_for('index'))

    # If default background is selected
    if img != '':
        if(img == 'user_defined.png'):
            bg_color = request.form['bg_color']
            text_on_image = request.form['text_on_image']
            do_svg2png(img, 1, bg_color, text_on_image)
        filename = img + '.csv'
    # If the textbox is filled
    elif csv != '':
        check_csv = csv.splitlines()
        count_line = 0
        for check in check_csv:
            line = check.split(',')
            if len(line) == 4:
                count_line = count_line + 1
        if count_line == len(check_csv):
            filename = "default.png.csv"
            f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w+")
            f.write(csv)
            f.close()
        else:
            flash('Write Data in Correct format!', 'error')
            return redirect(url_for('index'))
    # if user does not select file, browser submits an empty part without filename
    elif eventyay_url != '':
        filename = 'speaker.png.csv'
        generate_csv_eventyay.tocsv(eventyay_url, filename)
    else:
        filename = str(uuid.uuid4()) + '.png.csv'

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
    else:
        if filename.find("png.csv") != -1:
            if img == '':
                flash('Please upload an image in \'PNG\' format!', 'error')
                return redirect(url_for('index'))
        else:
            flash('Please upload a file in \'CSV\' format! Each line is a badge and the lines on the badge are \
            separated by commas. Try it out!', 'error')
            return redirect(url_for('index'))
    # if config file is uploaded
    config_json = request.files['config']
    if config_json.filename != '':
        if '.' in config_json.filename and config_json.filename.rsplit('.', 1)[1] == 'json':
            config_json.save(os.path.join(app.config['UPLOAD_FOLDER'], config_json.filename))
        else:
            flash('Only JSON file is accepted!', 'error')
            return redirect(url_for('index'))

    # If the csv file is uploaded
    if '.' in filename and filename.rsplit('.', 1)[1] == 'csv':
        filename = secure_filename(filename)
        if filename != "default.png.csv" and eventyay_url == '':
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        generate_badges(_zip, _pdf)

        # Remove the uploaded files after job in done
        os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        try:
            if 'imgname' in locals():
                os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], imgname))
        except Exception:
            traceback.print_exc()

        if _zip and _pdf:
            flash(filename.replace('.', '-'), 'success')
        elif _zip and not _pdf:
            flash(filename.replace('.', '-'), 'success-zip')
        elif not _zip and _pdf:
            flash(filename.replace('.', '-'), 'success-pdf')

        return redirect(url_for('index'))


@app.route('/guide')
def guide():
    return render_template('guide.html')


@app.errorhandler(404)
def Not_Found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def Internal_Server_Error(e):
    trace = traceback.format_exc()
    return render_template('500.html', exception=trace), 500


if __name__ == '__main__':
    app.run()
