# Face & Eye detection using OpenCV 

Here we work with face detection using Haar-Cascade classifier with OpenCV.
OpenCV comes with many pre-trained classifiers like face, eye, smile etc. Those XML files (pre-trained models) are stored in opencv/data/haarcascades/ folder. You can also add those classifiers if you want, but here I am going to use only two classifiers i.e. one for face and another for eye.

In this project, we are going to use default camera of our system/laptop to take input as live video. Then we capture frames in video and processes each captured frame for face and eye detection.

## Steps to run:
1. clone this repo using
> git clone https://github.com/Sonkaryasshu/Face_Detection.git
2. Run python file (after going to desired directory)
> cd Face_Detection

> python cv.py
