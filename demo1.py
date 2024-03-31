import numpy as np
import cv2 as cv
import random as rng


rng.seed(12345)

def detect_edges_lines_ellipses(image_path):
    # 读取输入的图像
    src = cv.imread(image_path)
    if src is None:
        print("Error loading image")
        return

    # 将图像转换为灰度图
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    # 创建EdgeDrawing对象
    ed = cv.ximgproc.createEdgeDrawing()

    # 设置EdgeDrawing的参数
    EDParams = cv.ximgproc_EdgeDrawing_Params()
    EDParams.MinPathLength = 50
    EDParams.PFmode = False
    EDParams.MinLineLength = 20
    EDParams.NFAValidation = True

    ed.setParams(EDParams)

    # 检测边缘
    ed.detectEdges(gray)

    # 获取边缘线段、直线和椭圆
    segments = ed.getSegments()
    lines = ed.detectLines()
    ellipses = ed.detectEllipses()

    # 绘制检测到的边缘线段
    ssrc = src.copy() * 0
    for i in range(len(segments)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv.polylines(ssrc, [segments[i]], False, color, 1, cv.LINE_8)

    # 绘制检测到的直线
    lsrc = src.copy()
    if lines is not None:
        lines = np.uint16(np.around(lines))
        for i in range(len(lines)):
            cv.line(lsrc, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 1, cv.LINE_AA)

    # 绘制检测到的椭圆
    esrc = src.copy()
    if ellipses is not None:
        for i in range(len(ellipses)):
            center = (int(ellipses[i][0][0]), int(ellipses[i][0][1]))
            axes = (int(ellipses[i][0][2]) + int(ellipses[i][0][3]), int(ellipses[i][0][2]) + int(ellipses[i][0][4]))
            angle = ellipses[i][0][5]
            color = (0, 0, 255)
            if ellipses[i][0][2] == 0:
                color = (0, 255, 0)
            cv.ellipse(esrc, center, axes, angle, 0, 360, color, 2, cv.LINE_AA)

    # 显示结果
    cv.imshow("detected edge segments", ssrc)
    cv.imshow("detected lines", lsrc)
    cv.imshow("detected circles and ellipses", esrc)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 调用函数并展示结果
image_path = '00.png'  # 默认图片路径
detect_edges_lines_ellipses(image_path)
