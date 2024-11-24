from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .model.auth_model import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User.objects(username=data['username']).first()
    if user and user.username:
        return jsonify({"msg": "Your have an acount. Please sign in."}), 401
    else:
        new_user = User(username=data['username'], password=data['password'], email=data["email"], name=data["name"])  # Hash the password in production!
        new_user.save()
        return jsonify({"msg": new_user}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects(username=data['username']).first()
    
    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
