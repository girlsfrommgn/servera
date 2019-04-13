from flask import Flask, url_for, render_template, redirect
from registry_form import RegistryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'its_a_girl_power'


@app.route('/')
@app.route('/first_page')
def main_page():
    return render_template('first_page.html')


@app.route('/registry', methods=['GET', 'POST'])
def registry():
    form = RegistryForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
