import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return 'form.html'

@app.route('/fo')
def form():
  return render_template('form.html')

@app.route('/form', methods=['POST'])
def quiz_answers():
    q1 = request.form['q1']
    q2 = request.form['q2']
    q4 = request.form['q1']
    q5 = request.form['q2']
    response = requests.get('http://jsonip.com')
    return [response.status_code, response.text, q1, q2, q4, q5]
  
if __name__ == "__main__":
    home()
    app.run(host="0.0.0.0", port=8080)
