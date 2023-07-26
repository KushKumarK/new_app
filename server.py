from flask import Flask, send_file

app = Flask(__name__)

@app.route('/<file>')
def home(file):
    return send_file(file)

if __name__ == '__main__':
    app.run(debug=True)