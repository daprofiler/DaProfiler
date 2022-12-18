import requests
import io
from PIL import Image
import numpy as np
import cv2

def contains_face(image_url):
  response = requests.get(image_url)
  image = response.content

  image = Image.open(io.BytesIO(image))

  image_np = np.asarray(image)

  face_cascade = cv2.CascadeClassifier(r'modules\face_recognition\lbpcascade_frontalface.xml')

  gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  return len(faces) > 0

def check(image_url): 
  if contains_face(image_url):
    return True
  else:
    return None
