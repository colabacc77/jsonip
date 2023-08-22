import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
  response = requests.get('http://jsonip.com')
  return response.status_code, response.text

if __name__ == "__main__":
    home()
    app.run(host="0.0.0.0", port=80)
