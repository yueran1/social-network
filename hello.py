from flask import Flask
app = Flask(__name__)

#direct the page with the path end with '/' to hello world
@app.route('/')
def index():
    return '<h1>hello World!</h1>'

#Direct the page with the path end with /user/<name> to hello user_name
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name

if __name__ == '__main__':
    app.run(debug=True)

