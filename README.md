#Face Detection with python and opencv
Simple python program that get an face **image** and show **detected** face. program can detect **face**, **smile**, **eyes**.

##Table Of contents
* Requirements
* Example
* How to config this program for your purpose

##Requirements
1. opencv
2. python 2

you need to have installed opencv and python 2 in your Linux.

##Examples
* Download project.
* Run this command on terminal. ( in project directory )
~~~bash
   $ python2 detect_face.py pics/girl_2.jpg
~~~

Input Image (boy-2.jpg):

<a href="https://github.com/mlibre/face_detection/blob/master/pics/boy-2.jpg" target="_blank"><img src="https://github.com/mlibre/face_detection/blob/master/pics/boy-2.jpg"/></a>

Output Image:

<a href="https://github.com/mlibre/face_detection/blob/master/pics/boy-2-recognized.png" target="_blank"><img src="https://github.com/mlibre/face_detection/blob/master/pics/boy-2-recognized.png"/></a>

##How to config this program for what you want
I designed this program specify for **mobiles front camera's images**.
If you want to detect **better/more** face, eyes or smile, change **detectmuiltiscale** function **parameters** values.
