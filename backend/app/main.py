from flask import Flask, render_template, request, jsonify
from flask_compress import Compress
from werkzeug.utils import secure_filename
import os
import json
import shutil
import traceback
from svg_to_png import do_svg2png

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


@app.route('/')
def index():
    """
    An  index.html file which specifies that it's badgeyay's backend
    """
    return render_template('index.html')


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
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception:
            traceback.print_exc()


def output(response_type, message, download_link):
    if download_link == '':
        response = [
            {
                'type': response_type,
                'message': message
            }
        ]
    else:
        response = [
            {
                'type': response_type,
                'message': message,
                'download_link': download_link
            }
        ]
    return jsonify({'response': response})


@app.route('/api/v1.0/generate_badges', methods=['POST'])
def main_task():
    """
    Function to recive the input data from the user, process and send ouput
    """
    empty_directory()
    csv = request.form.get('csv', '').strip()
    img = request.form.get('img-default', '')
    custom_font = request.form.get('custfont', '')

    if 'file' in request.files:
        file = request.files['file']

    # img-default is specified
    if img != '':
        if (img == 'user_defined.png'):
            bg_color = request.form.get('bg_color', '')
            if bg_color == '':
                return output('error', 'background color or image not specified', 0)
            do_svg2png(img, 1, bg_color)
        filename = img + '.csv'

    # custom font is specified
    if custom_font != '':
        json_str = json.dumps({
            'font': custom_font
        })
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'fonts.json'), "w+")
        f.write(json_str)
        f.close()

    if img == '':
        if 'image' not in request.files:
            return output('error', 'image and image-default are both empty or contains illegal data', '')
        else:
            img = request.files['image'].filename
            filename = request.files['image'].filename + ".csv"

    if csv != '':
        # CSV data was provided as plain text
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
            return output('error', 'CSV data was given in incorrect format', '')
    else:
        if 'file' not in request.files:
            return output('error', 'No proper CSV file was uploaded via POST nor a proper csv data as plain text was given', '')

    if 'image' in request.files:
        image = request.files['image']
        imgname = image.filename
        if '.' in imgname:
            imgname = filename.rsplit('.', 1)[0]
            imgname = secure_filename(imgname)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        else:
            return output('error', 'No background was specified', '')

    if filename.find("png.csv") == -1:
        if img == '':
            return output('error', 'Image not in PNG format', '')

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
            url = "backend/app/static/badges/" + filename.replace('.', '-') + "-badges.pdf"
            os.rename(os.path.join(BADGES_FOLDER + "/" + filename + ".badges.pdf"),
                      os.path.join(BADGES_FOLDER + "/" + filename.replace('.', '-') + "-badges.pdf"))
            return output('success', 'pdf generation completed successfully', url)
        else:
            # Other unexpected error
            return output('error', 'Internal error', '')


@app.route('/api/v1.0/generate_badges', methods=['GET'])
def illiegal_request_type():
    """
    Only POST request is allowed, post error on GET request
    """
    return output('error', 'Invalid method, only POST is allowed', '')


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
    app.run(host='0.0.0.0',debug=True)
