import cv2

video = cv2.VideoCapture(0)
a = 1
while True:
    a = a+1
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    check, frame = video.read()
    print(frame)

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("live_image", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()