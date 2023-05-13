import cv2 as cv
import pandas as pd
import argparse

index = ["color", "color_name", "hex", "R", "G", "B"]
colorcodes = pd.read_csv("colors.csv", names=index, header=None)
# print(colorcodes)
# print(colorcodes.iloc[:, 3])
File = "group.jpg"


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path: ")
args = vars(ap.parse_args())

img_path = args['image']


def coloridentifier(R, G, B):
    m = 10000
    for i in range(len(colorcodes)):
        d = abs(R - colorcodes.loc[i, "R"]) + abs(G -
                                                  colorcodes.loc[i, "G"]) + abs(B - colorcodes.loc[i, "B"])
        if d <= m:
            m = d
            cname = colorcodes.loc[i, "color_name"]
    return cname


Clicked = False

r, g, b = 0, 0, 0
xpos, ypos = 0, 0


def colorDrawer(event, x, y, flags, param):
    global r, g, b, xpos, ypos, Clicked
    # print("HERE")
    if event == cv.EVENT_RBUTTONUP:
        Clicked = True
        # print(x, y)
        r, g, b = img[y, x]
        xpos = x
        ypos = y


cv.namedWindow("image")
cv.setMouseCallback("image", colorDrawer)

img = cv.imread(img_path)


while True:

    cv.imshow("image", img)
    if Clicked:
        cv.rectangle(img, (20, 20), (350, 70), (255, 0, 0), -1)
        text = coloridentifier(r, g, b)
        cv.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv.LINE_AA)
        Clicked = False
    wk = cv.waitKey(2)
    if wk == ord("q"):
        break


cv.destroyAllWindows()


# print(coloridentifier(25, 25, 20))


# cv.destroyAllWindows()
