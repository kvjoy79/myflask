from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to my first Flask Application!'

if __name__ == '__main__':
    app.run(debug=True)
