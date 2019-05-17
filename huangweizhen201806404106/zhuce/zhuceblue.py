from flask import Blueprint, request ,jsonify

zhuce_bp = Blueprint('zhuce_bp',__name__)
class User(object):
    def __init__(self,username,password):
        self.usermame = username
        self.password = password
users = {}

@zhuce_bp.route('/zhuce',methods = ['POST'])
def zhuce():
    if not request.is_json:
        return jsonify({"提示":"没有JSON请求"}),400
    username = request.json.get('username',None)
    password = request.json.get('password',None)
    if (not username) or (not password):
        return jsonify({"提示":"缺少用户名或密码"}),400
    if username in users:
        return jsonify({"提示":"该用户名已被注册"}),201
    users[username] = User(username,password)
    return jsonify({"提示":"注册成功"}),200
