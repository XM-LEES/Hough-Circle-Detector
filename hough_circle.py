import cv2



# def detect_circles(image_path, bilateral_diameter=15, sigma_color=15, sigma_space=50,
#                     dp=1, minDist=10, param1=120, param2=60, minRadius=40, maxRadius=60):

#     image_path = image_path
#     img = cv2.imread(image_path)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # 进行双边滤波
#     bilateral = cv2.bilateralFilter(img_gray, bilateral_diameter, sigma_color, sigma_space)
#     # hough圆变换
#     cimg = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
#     circles = cv2.HoughCircles(image=bilateral, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, 
#                                 param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
#     return circles

# def display_circles(image_path, circles):
#     image_path = image_path
#     img = cv2.imread(image_path)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     if circles is not None:
#         cimg = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
#         circles = circles[0, :].astype(int)
#         for i in circles:
#             cv2.circle(img=cimg, center=(i[0], i[1]), radius=i[2], color=(0, 255, 0), thickness=2)
#             cv2.circle(img=cimg, center=(i[0], i[1]), radius=2, color=(0, 0, 255), thickness=3)
        
#         return cimg
#         # cv2.imshow('Circles Detected', cimg)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#     else:
#         print("No circles detected.")




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
        circles = cv2.HoughCircles(image=bilateral, method=cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, 
                                    param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
    
        if circles is not None:
            cimg = cv2.cvtColor(self.img_gray, cv2.COLOR_GRAY2BGR)
            circles = circles[0, :].astype(int)
            for i in circles:
                cv2.circle(img=cimg, center=(i[0], i[1]), radius=i[2], color=(0, 255, 0), thickness=2)
                cv2.circle(img=cimg, center=(i[0], i[1]), radius=2, color=(0, 0, 255), thickness=3)
            return circles, cimg

        # else:
        #     print("No circles detected.")
        #     return None