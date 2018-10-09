from flask import Flask

app = Flask(__name___)  #'__main__'

@app.route('/')
def hello_world():
    return "Hello, World"

if __name_ == '__main__':
    app.run()