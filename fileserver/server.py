import os
from flask import Flask, render_template_string, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_port():
    return os.environ.get("PORT_FS") or 8090


def get_files_path():
    return os.path.normpath(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), '..',
                     'wasmfiles'))


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory(get_files_path(), filename)


@app.route('/')
def upload_form():
    return render_template_string(f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Upload a file</title>
  </head>
  <body>
    <form
      action="http://localhost:{get_port()}/file"
      method="POST"
      enctype="multipart/form-data"
    >
      <input type="file" name="file" />
      <input type="submit" />
    </form>
  </body>
</html>
    """)


@app.route('/file', methods=['POST'])
def upload_file():
    if request.method != 'POST':
        return "please use POST"

    f = request.files['file']
    f.save(get_files_path() + f.filename)
    return "it's okay"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=get_port())