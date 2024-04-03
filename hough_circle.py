import cv2
import numpy as np

def detect_circles(image_path, bilateral_diameter=15, sigma_color=15, sigma_space=50,
                    dp=1, minDist=10, param1=120, param2=60, minRadius=40, maxRadius=60):

    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 进行双边滤波
    bilateral = cv2.bilateralFilter(img_gray, bilateral_diameter, sigma_color, sigma_space)
    # hough圆变换
    circles = cv2.HoughCircles(image=bilateral, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, 
                                param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    if circles is None:
        # circles
        cnt = 0
        while (circles is None) and (cnt < 5):
            param2 -= 2
            cnt += 1
            circles = cv2.HoughCircles(image=bilateral, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, 
                                param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
            print(f"cnt:{cnt}")

    if circles is None:
        return None
    elif len(circles) >= 1:
        # print(circles)
        # print(np.mean(circles, axis=1, keepdims=True))
        np.set_printoptions(precision=1)
        return np.mean(circles, axis=1, keepdims=True)

def display_circles(image_path, circles):
    if circles is None:
        return
    cimg = cv2.imread(image_path)
    circles = circles[0, :].astype(int)
    for i in circles:
        cv2.circle(img=cimg, center=(i[0], i[1]), radius=i[2], color=(0, 255, 0), thickness=2)
        cv2.circle(img=cimg, center=(i[0], i[1]), radius=2, color=(0, 0, 255), thickness=3)
    return cimg