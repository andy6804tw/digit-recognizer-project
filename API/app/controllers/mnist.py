from flask import Blueprint, request,jsonify,redirect
import app.modules.mnist as mnistModule

mnistCtrl = Blueprint('mnist',__name__)
  

@mnistCtrl.route('', methods=['GET'])
def getResult():
    return mnistModule.getResult()
  
