from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/first_page')
def login():
    return render_template('first_page.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')