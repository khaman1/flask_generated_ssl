from flask import Flask

app = Flask(__name__)

@app.route('/.well-known/pki-validation/<filename>')
def view_ssl_file(filename):
    with open("misc/"+filename) as f:
        file_content = f.read()

    return file_content 