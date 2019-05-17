from flask import Flask, request ,jsonify
from flask_jwt_extended import JWTManager, create_access_token
import b.bblue as huang
import zhuce.zhuceblue as wei
import denglu.denglublue as zhen


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)



app.register_blueprint(huang.b_bp)
app.register_blueprint(wei.zhuce_bp)
app.register_blueprint(zhen.denglu_bp)

if __name__ == '__main__':
    app.run()