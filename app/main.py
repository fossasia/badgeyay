from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os, shutil
import traceback
import generate_csv_eventyay

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
BADGES_FOLDER = os.path.join(APP_ROOT, 'static/badges')
SCRIPT = os.path.join(APP_ROOT, 'merge_badges.sh')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
	default_background = []
	for file in os.listdir(UPLOAD_FOLDER):
		if file.rsplit('.', 1)[1] == 'png':
			default_background.append(file)
	return render_template('index.html', default_background = default_background)


def generate_badges():
	os.system(SCRIPT)


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

	# If default background is selected
	if img != '':
		filename = img + '.csv'
	# If the textbox is filled
	elif csv != '':
		filename = "default.png.csv"
		f = open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "w+")
		f.write(csv)
		f.close()
	# if user does not select file, browser submits an empty part without filename

	elif eventyay_url !='':
		filename='speaker.png.csv'
		generate_csv_eventyay.tocsv(eventyay_url,filename)

	else:
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
		generate_badges()

		# Remove the uploaded files after job in done
		os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		try:
			if 'imgname' in locals():
				os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], imgname))
		except Exception:
			traceback.print_exc()

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
