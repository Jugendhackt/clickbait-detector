from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/echo/<text>')
def echo(text):
	return text

@app.route('/add/<int:number1>/<int:number2>')
def addition(number1 ,number2):
	return (str) (number1+number2)


if __name__ == '__main__':
	app.run(host = '0.0.0.0')
