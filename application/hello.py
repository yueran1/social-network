from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
boostrap= Bootstrap(app)

#direct the page with the path end with '/' to hello world
@app.route('/')
def index():
    #return '<h1>hello World!</h1>'
    return render_template('index.html')

#Direct the page with the path end with /user/<name> to hello user_name
@app.route('/user/<name>')
def user(name):
    #return '<h1>Hello, %s!</h1>' %name
    return render_template('user2.html',name=name)

if __name__ == '__main__':
    app.run(debug=True)

