from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/postreport', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return 'Success'


app.run(host='0.0.0.0', port=8090)
