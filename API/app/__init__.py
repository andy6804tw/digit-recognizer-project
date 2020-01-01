import config
from flask import Flask,request,render_template
from flask_cors import CORS
from app.controllers.mnist import mnistCtrl 


app=Flask(__name__)
CORS(app)
app.config.from_object(config) # 由config.py管理環境變數

app.register_blueprint(mnistCtrl, url_prefix='/mnist')