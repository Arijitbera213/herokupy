from flask import Flask, jsonify, request,render_template
from werkzeug.wrappers import Request, Response
from flask_restful import Api, Resource
import os, json

app = Flask(__name__,template_folder='.')

@app.route("/")
def hello():
    return render_template('index.html')
@app.route('/test')
def run_script():
    file = open(r'script1.py', 'r').read()
    return exec(file)
@app.route('/start')
def run_script1():
    file = open(r'script1.py', 'r').read()
    exec(file)
    return render_template('index.html')
@app.route('/run')
def run_script2():
    file = open(r'script2.py', 'r').read()
    exec(file)
    return render_template('index.html')



            
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    port = int(os.environ.get('PORT', 6000))
    run_simple('0.0.0.0', port, app)