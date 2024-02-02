from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the home page!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}! (submitted via POST)'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
