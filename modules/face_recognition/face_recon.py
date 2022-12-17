import requests
import io
from PIL import Image
import numpy as np
import cv2

def contains_face(image_url):
  # Téléchargement de l'image à partir de l'URL
  response = requests.get(image_url)
  image = response.content

  # Conversion de l'image en format PIL
  image = Image.open(io.BytesIO(image))

  # Conversion de l'image en format NumPy
  image_np = np.asarray(image)

  # Chargement du classifieur de visage LBP
  face_cascade = cv2.CascadeClassifier(r'modules\face_recognition\lbpcascade_frontalface.xml')

  # Conversion de l'image en format gris
  gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

  # Détection des visages dans l'image
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

  # Renvoie True si au moins un visage a été détecté, False sinon
  return len(faces) > 0


def check(image_url): 
  if contains_face(image_url):
    return True
  else:
    return None
