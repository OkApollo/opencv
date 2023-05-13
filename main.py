import cv2 as cv

# haarcascade models.

cam = cv.imread("groupa.png")
# cam = cv.VideoCapture(0)

face = cv.CascadeClassifier('frontface.xml')
eye = cv.CascadeClassifier('eye.xml')

while True:
    # return 2 things: 1) rectangle, 2) image
    img = cam

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)  # x,y,w,h

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # filter_gray = gray[y:y+h, x:x+w]
        # filter_img = img[y:y+h, x:x+w]

        # eyes = eye.detectMultiScale(filter_gray)
        # for (x1, y1, w1, h1) in eyes:
        #     cv.rectangle(filter_img, (x1, y1), (x1+w, y1+h), (0, 0, 255), 1)

        eyes = eye.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in eyes:
            cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

    # print(faces)

    cv.imshow("My face", img)
    k = cv.waitKey(20) & 0xff
    if k == ord("q"):
        break

cam.release()
cv.destroyAllWindows()
