from flask import Flask
from databaseread import databaseread
from flask import request
import time
from flask import json



app = Flask(__name__)

@app.route('/value')
def getValue():
    dbread =databaseread()
    key = request.args.get('word')
    start = time.time()
    value = dbread.read_current_value(key)
    done = time.time()
    elapsed = done - start
    print(value)
    returnJson = {}
    returnJson['value'] = value
    returnJson['elapsed'] = elapsed
    
    return json.dumps(returnJson)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)