import cv2
import numpy as np

src = cv2.imread(".\\image\\Image0.jpg")
img = src.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img_gray', img_gray)
cv2.waitKey(0)





# # 进行中值滤波 去除椒盐噪声
# # ksize = 3， 5， 7
# median = cv2.medianBlur(src=img_gray, ksize=5)
# # median = img_gray
# cv2.imshow('median', median)
# cv2.waitKey(0)


# gauss = cv2.GaussianBlur(img_gray,(5,5),0)
# cv2.imshow('gauss', gauss)
# cv2.waitKey(0)



# # 进行双边滤波 保持图像边缘的平滑方法
bilateral = cv2.bilateralFilter(img_gray, 15, 15, 50, 100)
# bilateral = cv2.bilateralFilter(img_gray, d=15, sigmaColor=15, sigmaSpace=50)

# d > 10
cv2.imshow('bilateral', bilateral)
cv2.waitKey(0)






filtered = bilateral

'''hough圆变换'''
cimg = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)  # 转换成彩色图
circles = cv2.HoughCircles(image=filtered, method=cv2.HOUGH_GRADIENT, dp=1, minDist=10, 
                           param1=120, param2=60, minRadius=40, maxRadius=60)  # Hough圆检测





# 非常准确的内圆
# bilateral = cv2.bilateralFilter(img_gray, 15, 20, 50, 100)
# circles = cv2.HoughCircles(image=filtered, method=cv2.HOUGH_GRADIENT, dp=1, minDist=10, 
#                            param1=120, param2=60, minRadius=40, maxRadius=60)  # Hough圆检测
# 130 65 也可以

# 内外圆分开 效果不好
# bilateral = cv2.bilateralFilter(img_gray, 15, 20, 50, 100)
# circles = cv2.HoughCircles(image=filtered, method=cv2.HOUGH_GRADIENT, dp=1, minDist=1, 
#                            param1=160, param2=80, minRadius=40, maxRadius=80)  # Hough圆检测



# image	原始图像
# method	目前只支持cv2.HOUGH_GRADIENT
# dp	图像解析的反向比例。1为原始大小，2为原始大小的一半
# minDist	圆心之间的最小距离。过小会增加圆的误判，过大会丢失存在的圆
# param1	Canny检测器的高阈值
# param2	检测阶段圆心的累加器阈值。越小的话，会增加不存在的圆；越大的话，则检测到的圆就更加接近完美的圆形
# minRadius	检测的最小圆的半径
# maxRadius	检测的最大圆的半径

# //第一个参数是输出被检测图片
# //第二个参数表示存储数组，其中存储被检测的圆的圆心的坐标和圆的半径。
# //第三个参数是检测圆的方法（霍夫梯度法）
# //第四个参数可以设置为1就行--默认参数
# //第五个参数是圆心与圆心之间的距离，这是一个经验值。这个大了，那么多个圆就是被认为一个圆。
# //第六个参数 就设为默认值就OK
# //第七个参数这个根据你的图像中的圆  大小设置，如果圆越小，则设置越小
# //第八个和第九个参数 是你检测圆 最小半径和最大半径是多少  这个是经验值


circles = circles.astype(int)
print(circles)


for i in circles[0, :]:    # 遍历circles，i为列表，i中包含多个列表，列表为[x,y,r]圆心坐标和半径
    # draw the outer circle
    cv2.circle(img=cimg, center=(i[0],i[1]), radius=i[2], color=(0,255,0), thickness=2)
    # (img, center, radius, color[, thickness[, lineType[, shift]]])
    # draw the center of the circle
    cv2.circle(img=cimg, center=(i[0],i[1]), radius=2, color=(0,0,255), thickness=3)

cv2.imshow('cimg',cimg)
cv2.waitKey(0)




# https://blog.csdn.net/qq_44631615/article/details/134445747


# 原理
# https://blog.csdn.net/great_yzl/article/details/119645423

# # 进行均值滤波 去随机噪声 效果不好
# blur = cv2.blur(img_gray, (1, 15))

# # 进行高斯滤波 适合处理高斯噪声 效果不明显
# gauss = cv2.GaussianBlur(img_gray, (5, 5), sigmaX=1)
# cv2.imshow('gauss', gauss)
# cv2.waitKey(0)


# 高通过滤/滤波（边缘检测/高反差保留）
# 使用的函数有：cv2.Sobel() , cv2.Schar() , cv2.Laplacian()
# Sobel,scharr其实是求一阶或者二阶导数。scharr是对Sobel的优化。
# Laplacian是求二阶导数。
# https://blog.csdn.net/wsp_1138886114/article/details/82872838









# https://www.cnblogs.com/xyf327/p/14848402.html


# 同心圆检测
# https://cloud.tencent.com/developer/ask/sof/106455334
# import numpy as np
# import cv2
# image = cv2.imread("GoldenSpike.png",0)

# output = cv2.imread("GoldenSpike.png",1)
# cv2.imshow("Original image", image)
# cv2.waitKey()

# blurred = cv2.GaussianBlur(image,(11,11),0)

# cv2.imshow("Blurred image", blurred)
# cv2.waitKey()
# setItem=set()
# previous=0;
# minR=4
# for maxR in range(9,300,9):
#     # Finds circles in a grayscale image using the Hough transform
#     circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,
#                              param1=100,param2=100,minRadius=minR,maxRadius=maxR)
#     minR+=4
#     # cv2.HoughCircles function has a lot of parameters, so you can find more about it in documentation
#     # or you can use cv2.HoughCircles? in jupyter nootebook to get that 

#     # Check to see if there is any detection
#     if circles is not None:
#         # If there are some detections, convert radius and x,y(center) coordinates to integer
#         circles = np.round(circles[0, :]).astype("int")

#         for (x, y, r) in circles:
#             # Draw the circle in the output image
#             cv2.circle(output, (x, y), r, (0,255,0), 1)
#             # Draw a rectangle(center) in the output image
#             cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0,255,0), -1)
#             setItem.add(r)

# lst=sorted(setItem)
# print("Length of List =", len(lst))
# for item in lst:
#     print(item)

# cv2.imshow("Detections",output)
# cv2.imwrite("CirclesDetection.jpg",output)
# cv2.waitKey()