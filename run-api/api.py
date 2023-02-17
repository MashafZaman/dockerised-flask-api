from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/api/get', methods=['GET'])
def get_data():
    return jsonify({'status': 'Working'})

@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()
    orientation = data['orientation']
    steps_moved = data['steps_moved']
    message = f'You\'ve moved ${steps_moved} steps, and are facing ${orientation}'
    response = {'message': message}
    return jsonify(response)

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port 
    app.run(host='0.0.0.0', port=os.getenv('PORT'))