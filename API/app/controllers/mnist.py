from flask import Blueprint, request,jsonify,redirect
import app.modules.mnist as mnistModule

mnistCtrl = Blueprint('mnist',__name__)
  

@mnistCtrl.route('', methods=['GET','POST'])
def getResult():
  if request.method=='GET':
    return mnistModule.getResult()
  else:
    insertValues = request.get_json()
    base64Image=insertValues['image']
    return jsonify({'result':str(mnistModule.getResult(base64Image)),'image':base64Image})
  
