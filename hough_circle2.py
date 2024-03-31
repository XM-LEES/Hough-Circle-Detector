import cv2
import numpy as np

def detect_circles(image_path):
    src = cv2.imread(image_path)
    if src is None:
        print("Error loading image")
        return None

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ed = cv2.ximgproc.createEdgeDrawing()

    EDParams = cv2.ximgproc_EdgeDrawing_Params()
    EDParams.MinPathLength = 500
    EDParams.PFmode = False
    EDParams.MinLineLength = 20
    EDParams.NFAValidation = True

    ed.setParams(EDParams)

    ed.detectEdges(gray)
    ellipses = ed.detectEllipses()
    # return ellipses
    # 筛选出圆形
    if ellipses is not None:
        i = len(ellipses) - 1
        while i >= 0:
            if int(ellipses[i][0][3]) != 0 or int(ellipses[i][0][4]) != 0 or int(ellipses[i][0][5]) != 0:
                ellipses = np.delete(ellipses, i, axis=0)
                print(np.shape(ellipses))
            i = i - 1
    return ellipses


def display_circles(image_path, ellipses):
    if ellipses is None:
        return
    cimg = cv2.imread(image_path)

    
    if ellipses is not None:
        for i in range(len(ellipses)):
            center = (int(ellipses[i][0][0]), int(ellipses[i][0][1]))
            axes = (int(ellipses[i][0][2]) + int(ellipses[i][0][3]), int(ellipses[i][0][2]) + int(ellipses[i][0][4]))
            angle = ellipses[i][0][5]
            color = (0, 0, 255)
            if ellipses[i][0][2] == 0:
                color = (0, 255, 0)
            cv2.ellipse(cimg, center, axes, angle, 0, 360, color, 2, cv2.LINE_AA)
        return cimg




# image_path = 'a/test.jpg'
# circles = detect_circles(image_path)
# print(circles)
# result_image = display_circles(image_path, circles)
# cv2.imshow("detected circles", result_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()