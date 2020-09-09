from flask import Flask, jsonify, request, json
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from models.Database import Database
from models import User
from config import app_config

# initialize flask app
app = Flask(__name__)
cors = CORS(app)
config = app_config.config(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = Database('config/db_config')


@app.route('/api/db/connection', methods=['GET'])
def db_conn():
    if db.is_connected():
        return 'success'
    return 'failed'

# TODO: ajax request to server
# TODO: user comments
# @app.route('/comments', methods=['GET'])
# def all_course():
#     return jsonify({'status': 'Success',
#                     'comments': COMMENTS})

@app.route('/api/user/register', methods=['POST'])
def user_sign_up():
    http_status_code = 500
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')

    # Check duplicate user
    sql_result, is_success = User.find_user(db, email)

    if not sql_result and is_success:
        pass
    elif sql_result and is_success:
        response = jsonify({'msg': 'User already exists, please try login',
                            'status': 'failed'})
        http_status_code = 409
        return response, http_status_code
    else:
        response = jsonify({'msg': sql_result,
                            'status': 'failed'})
        return response, http_status_code

    # Create a new user account
    sql_result, is_success = User.create_user(db, email, password, first_name, last_name)
    if is_success:
        response = jsonify({'msg': sql_result,
                            'status': 'success'})
        http_status_code = 200
    else:
        # http_status is 500 by default
        response = jsonify({'msg': sql_result,
                            'status': 'failed'})
    return response, http_status_code


# @app.route('/api/user/info/name', methods=['PUT'])
# def user_info_update():
#     return
#
#
@app.route('/api/user/login', methods=['POST'])
def user_login():
    http_status = 500
    email = request.get_json()['email']
    password = request.get_json()['password']

    query_result, is_success = User.find_user(db, email)
    if not is_success:
        response = jsonify({'msg': query_result,
                            'status': 'failed'})
        return response, http_status
    if query_result:
        if bcrypt.check_password_hash(query_result[1], password):
            token = create_access_token({'Last_Name': query_result[2],
                                         'First_Name': query_result[3],
                                         'Email': query_result[0]})
            response = jsonify({'token': token,
                                'msg': 'login success',
                                'status': 'success'})
            http_status = 200
            return response, http_status
    response = jsonify({'msg': 'Invalid email or wrong password',
                        'status': 'failed'})
    http_status = 401
    return response, http_status


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port='5000', ssl_context=('cert.cert', 'cert.key'), debug=True)
    # TODO: Turn off ssl for development purpose
    app.run(host='0.0.0.0', port='5000', debug=True)
