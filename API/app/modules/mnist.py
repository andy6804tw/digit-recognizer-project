from flask import jsonify
import pickle
import numpy as np
import cv2
import math
import base64 
import gzip
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# PROJECT_DIR = os.path.join(PROJECT_ROOT,'../../')
PROJECT_DIR=''
with gzip.open(PROJECT_DIR+'API/app/modules/MNIST/resource/xgb(regression)-42-12000-scale-all.pgz', 'rb') as f:
    xgbRModel = pickle.load(f)
    print(xgbRModel)
with gzip.open(PROJECT_DIR+'API/app/modules/MNIST/resource/xgb(classfication)-42-12000-scale-all.pgz', 'rb') as f:
    xgbCModel = pickle.load(f)



def base64_cv2(base64_str):
    """
    base64 to cv2
    Args:
          base64_str: Image base64 encoder string
    Return:
          cv2 format(ndarray) image
    """
    imgString = base64.b64decode(base64_str)
    nparr = np.fromstring(imgString,np.uint8)  
    image = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    return image

def tsnePredict(image):
  """
  Digit Recognizer using t-SNE+XGBoost(regression+classfication)
  Args: 
        image(ndarray): image decode from base64_cv2(base64_str)
  Return:
        predict(int):  predict number result
  """
  reshapImg=image.reshape(-1)
  # XGBoost Regression (784D->2D)
  tsneImg=xgbRModel.predict([reshapImg])
  # XGboost Classfication
  predict=xgbCModel.predict(tsneImg)[0]
  print(tsneImg,predict)
  return predict

def kerasPredict(image):
  reshapImg = np.array(image)
  reshapImg = reshapImg.reshape(1,28,28,1)
  y_pred = kerasModel.predict([reshapImg])
  # pred =  np.argmax(y_pred, axis=1)
  return 'pred'

def getResult(base64Image=''):
  """
  Digit Recognizer interface
  Args:
        base64Image(string): Image base64 encoder string
  Return:
        response predict result
  """
  if base64Image=='':
    image = cv2.imread(PROJECT_DIR+"API/app/modules/MNIST/data/4.png")[:,:,::-1]
  else:
    image=base64_cv2(base64Image)

  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image=cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)/255
  
  pred=tsnePredict(image)
  return str(pred)
