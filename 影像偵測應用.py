import cv2
#dst1 = cv2.CascadeClassifier('type')#建立偵測部位
#dst2 = detectMulitScale(img,1.3,5)
def face(img):
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')#偵測的檔案
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    Iw = int(img.shape[1]*1)
    Ih = int(img.shape[0]*1)
    img1 = cv2.resize(img,(Iw,Ih))
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

    faces = eye_cascade.detectMultiScale(gray,1.3,18)
    faces1 = face_cascade.detectMultiScale(gray,1.3,18)
    for (x,y,w,h) in faces:
        cv2.rectangle(img1,(x-10,y-10),(x+w+10,y+h+10),(0,0,255),2)
    for (x,y,w,h) in faces1:
        cv2.rectangle(img1,(x-10,y-10),(x+w+10,y+h+10),(0,0,255),2)
    return img1
def mouse(event, x, y, flags, param):
    global frame
    if event == 1:
        print('kkk')
        cv2.imwrite('output.jpg',frame)


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()            # 讀取影片的每一幀
    frame = face(frame)
    if not ret:
        print("Cannot receive frame")   # 如果讀取錯誤，印出訊息
        break
    
    cv2.imshow('oxxostudio', frame)     # 如果讀取成功，顯示該幀的畫面
    cv2.setMouseCallback('oxxostudio', mouse)
    if cv2.waitKey(1) == ord('q'):      # 每一毫秒更新一次，直到按下 q 結束
        break
cv2.destroyAllWindows()