from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/say/<name>')
def say(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    output = ''
    
    for i in range(0, num):
        output += f'<p>{word}</p>'
        
    return output

@app.route('/Bojo')
def Bojo():
    return 'Dojo'


if __name__=="__main__":
    app.run(debug=True)
