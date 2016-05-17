import cv2
import sys

face_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eye_left_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_lefteye_2splits.xml')
eye_right_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_righteye_2splits.xml')

smile_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_smile.xml')

img_real = cv2.imread ( sys.argv[1] )
img_gray = cv2.cvtColor(img_real , cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray , 1.3 , 5 , 0 , minSize=(100,100))
for (x , y , w , h) in faces:
    cv2.rectangle( img_real , (x , y) , (x+w , y+h) , (120 , 120 , 120) , 2)

    img_gray_face_selected = img_gray[y:y+h ,  x:x+w]
    img_real_face_selected = img_real[y:y+h ,  x:x+w]

    left_eyes = eye_left_cascade.detectMultiScale(img_gray_face_selected , 1.1 , 5)
    for (tx , ty , tw , th) in left_eyes:
         cv2.rectangle( img_real_face_selected , (tx , ty) , (tx+tw , ty+th) , (0 , 255 , 0) , 2)

    right_eyes = eye_right_cascade.detectMultiScale(img_gray_face_selected , 1.1 , 5)
    for (tx , ty , tw , th) in right_eyes:
        cv2.rectangle( img_real_face_selected , (tx , ty) , (tx+tw , ty+th) , (255 , 0 , 0) , 2)

    smiles = smile_cascade.detectMultiScale(img_gray_face_selected , 1.7 , 40 )
    for (tx , ty , tw , th) in smiles:
        cv2.rectangle( img_real_face_selected , (tx , ty) , (tx+tw , ty+th) , (0 , 0 , 255) , 2)

cv2.imshow('hi world' , img_real)
cv2.waitKey(0)
cv2.destroyAllWindows()

