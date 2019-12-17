import pickle
import numpy as np
import cv2
import math
import base64 

#讀取Model
with open('app/modules/MNIST/resource/knn-35-4000-scale-all.pickle', 'rb') as f:
    model = pickle.load(f)

# base64 to cv2
def base64_cv2(base64_str):
    imgString = base64.b64decode(base64_str)
    nparr = np.fromstring(imgString,np.uint8)  
    image = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    return image

def predict(predImg):
  allCenter=np.array([[ 17.89351408,  40.3974383 ],
       [ 22.34058947, -29.7401498 ],
       [ 40.84367465,  -0.17747073],
       [ 15.63485097,  10.01957641],
       [-40.03946422,  -6.24115686],
       [-15.07509393,  15.77437033],
       [-11.89785358,  40.31856031],
       [ -5.35167924, -34.25424154],
       [ -0.28426326,  -4.06609265],
       [-23.64774371, -17.08729935]])
  data=np.array(predImg)
  arr=np.array([])
  for i in range(10):
      dist=math.pow(math.pow(allCenter[i][0]-data[0],2)+math.pow(allCenter[i][1]-data[1],2),0.5)
      arr=np.append(arr,dist)
      print(i, dist)
  return np.argmin(arr)

def getResult(base64Image=''):
  if base64Image=='':
    image = cv2.imread("app/modules/MNIST/data/6.png")[:,:,::-1]
  else:
    image=base64_cv2(base64Image)

  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image=cv2.resize(image, (28,28), interpolation = cv2.INTER_AREA)/255
  reshapImg=image.reshape(-1)

  predImg=model.predict([reshapImg])[0]
  return str(predict(predImg))