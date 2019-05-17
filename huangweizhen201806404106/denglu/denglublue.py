from flask import Blueprint,request ,jsonify
from flask_jwt_extended import JWTManager, create_access_token
import zhuce.zhuceblue as kkk

denglu_bp = Blueprint('denglu_bp',__name__)

@denglu_bp.route('/denglu',methods =['POST'])
def denglu():
    if not request.is_json:
        return jsonify({"提示":"没有JSON请求"}),400
    username = request.json.get('username',None)
    password = request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({"提示":"缺少用户名或密码"}),400
    dengluuser = kkk.users.get(username, None)
    if not dengluuser:
        return jsonify({"提示": "用户名不存在"}), 401
    if dengluuser and dengluuser.password == password:
        return jsonify(access_token=create_access_token(identity=username)), 200
    else:
        return jsonify({"提示": "用户名或密码错误"}), 401
