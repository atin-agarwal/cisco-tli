#!flask/bin/python
from flask import Flask,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1/tryit', methods=['GET'])
def try_it():
    api_id = request.args.get('apiId')
    param1 = request.args.get('inp1')
    param2 = request.args.get('inp2')
    param3 = request.args.get('inp3')
    print('API requested for :: ' + api_id)
    print('Input Set is :: ', param1, param2, param3)
    
    cmd = 'python3 <PATH_TO_PY_MODEL_SCRIPT> ' + param1 + ' ' + param2 + ' ' + param3
    print('Model running :: ', cmd)
    os.system(cmd)
    return ("Done...Please check console for output...")
   

if __name__ == '__main__':
    app.run(debug=True)
