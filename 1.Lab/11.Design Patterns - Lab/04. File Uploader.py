import os
from flask import Flask, request, render_template_string, redirect, url_for, flash
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'json'}
app.secret_key = 'your_secret_key'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File uploaded successfully', 'success')

            # Print file info to console
            file_ext = filename.split('.')[-1]
            if file_ext == 'csv':
                data = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                data = pd.read_json(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(data.head())

        else:
            flash('Invalid content type for import', 'error')

        return redirect(url_for('upload_file'))

    return render_template_string('''
        <!doctype html>
        <html>
          <head>
            <title>File Upload</title>
          </head>
          <body>
            {% with messages = get_flashed_messages(with_categories=true) %}
              {% if messages %}
                <ul>
                  {% for category, message in messages %}
                    <li{% if category %} class="{{ category }}"{% endif %}>{{ message }}</li>
                  {% endfor %}
                </ul>
              {% endif %}
            {% endwith %}
            <h1>File Upload</h1>
            <form method="POST" enctype="multipart/form-data">
              <input type="file" name="file" required>
              <input type="submit" value="Upload">
            </form>
          </body>
        </html>
        ''')


if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)

