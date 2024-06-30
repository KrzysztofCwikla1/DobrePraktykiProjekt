from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ksiega/<int:ksiega_nr>')
def ksiega(ksiega_nr):
    if 1 <= ksiega_nr <= 12:
        return render_template(f'k{ksiega_nr}.html')
    else:
        return "Nie znaleziono księgi", 404

if __name__ == '__main__':
    app.run(debug=True)