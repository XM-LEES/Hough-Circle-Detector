import cv2


class Hough_Detector(object):
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = cv2.imread(image_path)
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    
    def detect_circles(self, bilateral_diameter=15, sigma_color=15, sigma_space=50,
                       dp=1, minDist=10, param1=120, param2=60, minRadius=40, maxRadius=60):
        # 进行双边滤波
        bilateral = cv2.bilateralFilter(self.img_gray, bilateral_diameter, sigma_color, sigma_space)
        # hough圆变换
        cimg = cv2.cvtColor(self.img_gray, cv2.COLOR_GRAY2BGR)
        circles = cv2.HoughCircles(image=bilateral, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, 
                                    param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
        return circles
    
    def display_circles(self, circles):
        if circles is not None:
            cimg = cv2.cvtColor(self.img_gray, cv2.COLOR_GRAY2BGR)
            circles = circles[0, :].astype(int)
            for i in circles:
                # draw the outer circle
                cv2.circle(img=cimg, center=(i[0], i[1]), radius=i[2], color=(0, 255, 0), thickness=2)
                # draw the center of the circle
                cv2.circle(img=cimg, center=(i[0], i[1]), radius=2, color=(0, 0, 255), thickness=3)
            cv2.imshow('Circles Detected', cimg)
            cv2.waitKey(0)
        else:
            print("No circles detected.")


# 使用示例
detector = Hough_Detector(".\\image\\Image0.jpg")
circles = detector.detect_circles(bilateral_diameter=15, sigma_color=15, sigma_space=100,
                                   dp=1, minDist=10, param1=120, param2=60, minRadius=40, maxRadius=60)
detector.display_circles(circles)
