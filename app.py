from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page='interview')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html', page='dashboard')

@app.route('/interview')
def interview():
    return render_template('index.html', page='interview')

@app.route('/insight')
def insight():
    return render_template('index.html', page='insight')

@app.route('/talent')
def talent():
    return render_template('index.html', page='talent')

@app.route('/profile')
def profile():
    return render_template('index.html', page='profile')

if __name__ == '__main__':
    app.run(debug=True)