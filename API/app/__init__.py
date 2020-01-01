import config
from flask import Flask,request,render_template
from flask_cors import CORS
from app.controllers.mnist import mnistCtrl 
from flask_uploads import configure_uploads
from app.modules.upload import upFile


app=Flask(__name__)
CORS(app)
app.config.from_object(config) # 由config.py管理環境變數
configure_uploads(app, upFile)

app.register_blueprint(mnistCtrl, url_prefix='/mnist')