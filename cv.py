import cv2, time
new_path = 'C:\\ProgramData\\Anaconda3\\Library\\etc\\haarcascades\\'
eye = cv2.CascadeClassifier(new_path + 'haarcascade_eye.xml')
face =cv2.CascadeClassifier(new_path + 'haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
a = 1
while True:
    a=a+1
    check, frame = video.read()
    # gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("First", gray)
    detected = face.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 5)
    detected1 = eye.detectMultiScale(frame)
    for x,y,w,h in detected :
        frame = cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0), 3)
    for x,y,w,h in detected1 :
        frame = cv2.rectangle(frame,(x,y), (x+w,y+h), (0,255,0), 3)
    cv2.imshow("second", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()