import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QHBoxLayout, QSlider
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
# from hough_circle import detect_circles, display_circles
from hough_circle import Hough_Detector

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.Hough_Detector = None


    def initUI(self):
        # 设置窗口参数
        self.setWindowTitle('图像浏览器')
        self.setGeometry(100, 100, 900, 700)
        self.current_image_index = 0
        self.images = []

        # 应用样式表
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f7;
            }
            QLabel {
                border: 4px solid #c0c0c0;
                background-color: white;
            }
            QPushButton {
                background-color: #a9a9a9;
                border: none;
                border-radius: 15px;
                padding: 10px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #bcbcbc;
            }
            QPushButton:pressed {
                background-color: #dcdcdc;
                border-style: inset;
            }
        """)

        # 布局和控件
        layout = QVBoxLayout()

        # # 滑块
        # self.slider = QSlider(Qt.Horizontal)
        # self.slider.setMinimum(0)
        # self.slider.setMaximum(2)  # 三个固定位置
        # self.slider.setTickInterval(1)
        # self.slider.setSingleStep(1)  # 设置单步步长为1
        # self.slider.setPageStep(1)    # 设置页步长为1，用于拖动时的增量
        # self.slider.setTickPosition(QSlider.TicksBelow)
        # self.slider.valueChanged.connect(self.on_slider_value_changed)
        # self.slider.setFixedSize(200, 30)
        # # self.slider.setTickLabels(["Position A", "Position B", "Position C"])  # 设置刻度的文本标签
        # # self.slider.value()
        
        # 添加 QLabel 控件用于显示图片
        image_layout = QHBoxLayout()
        self.original_image_label = QLabel(self)
        self.original_image_label.setAlignment(Qt.AlignCenter)
        self.original_image_label.setFixedSize(600, 450)  # 设置固定大小
        self.detected_image_label = QLabel(self)
        self.detected_image_label.setAlignment(Qt.AlignCenter)
        self.detected_image_label.setFixedSize(600, 450)  # 设置固定大小
        
        # 添加 QLabel 控件用于显示提示信息
        message_layout = QHBoxLayout()
        self.message_label1 = QLabel(self)
        self.message_label1.setAlignment(Qt.AlignCenter)
        self.message_label2 = QLabel(self)
        self.message_label2.setAlignment(Qt.AlignCenter)
        self.message_label3 = QLabel(self)
        self.message_label3.setAlignment(Qt.AlignCenter)

        # 添加按钮
        button_layout = QHBoxLayout()
        self.btn_previous = QPushButton('前一张', self)
        self.btn_next = QPushButton('后一张', self)
        self.btn_process = QPushButton('处理图像', self)
        self.btn_auto_process = QPushButton('自动批量处理', self)
        self.btn_open_folder = QPushButton('选择文件夹', self)
        # 事件绑定
        self.btn_previous.clicked.connect(self.show_previous_image)
        self.btn_next.clicked.connect(self.show_next_image)
        self.btn_process.clicked.connect(self.process_image)
        self.btn_auto_process.clicked.connect(self.auto_process_image)
        self.btn_open_folder.clicked.connect(self.open_folder)
        
        # 将控件添加到布局
        image_layout.addWidget(self.original_image_label)
        image_layout.addWidget(self.detected_image_label)
        message_layout.addWidget(self.message_label1)
        message_layout.addWidget(self.message_label2)
        button_layout.addWidget(self.btn_previous)
        button_layout.addWidget(self.btn_next)
        button_layout.addWidget(self.btn_process)
        button_layout.addWidget(self.btn_auto_process)

        layout.addLayout(image_layout)
        layout.addLayout(message_layout)
        layout.addWidget(self.message_label3)
        layout.addWidget(self.btn_open_folder)
        layout.addLayout(button_layout)
        # layout.addWidget(self.slider)
        layout.setAlignment(Qt.AlignCenter)  # 居中布局

        self.setLayout(layout)


    # def on_slider_value_changed(self, value):
    #     if value == 0:
    #         self.show_message1("Slider value changed to A")
    #     elif value == 1:
    #         self.show_message1("Slider value changed to B")
    #     elif value == 2:
    #         self.show_message1("Slider value changed to C")


    def show_message1(self, message):
        self.message_label1.setText(message)

    def show_message2(self, message):
        self.message_label2.setText(message)

    def show_message3(self, message):
        self.message_label3.setText(message)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            self.images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
            self.modified = [None for _ in range(len(self.images))]
            self.current_image_index = 0
            self.show_message3(f"当前文件夹：{folder_path}")
            self.show_image()

    def show_image(self):
        if self.images:
            pixmap = QPixmap(self.images[self.current_image_index])
            self.original_image_label.setPixmap(pixmap.scaled(self.original_image_label.width(), self.original_image_label.height(), Qt.KeepAspectRatio))
            self.show_message1("当前图片：" + self.images[self.current_image_index])
            self.show_message3(f"{self.current_image_index + 1} / {len(self.images)}")
        else:
            self.show_message1("文件夹下无图片")

    def show_previous_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()

    def process_image(self):
        if self.images:

            if self.modified[self.current_image_index] != None:
                return

            # self.modified[self.current_image_index] = True

            image_path = self.images[self.current_image_index]

            self.Hough_Detector = Hough_Detector(image_path)
            circles, processed_image = self.Hough_Detector.detect_circles()

            # circles = detect_circles(image_path=image_path)
            # processed_image = display_circles(image_path, circles)


            # 将 OpenCV 图像转换为 QImage
            height, width, _ = processed_image.shape
            bytes_per_line = 3 * width
            q_image = QImage(processed_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            # 将 QImage 转换为 QPixmap
            pixmap = QPixmap.fromImage(q_image)
            # 显示处理后的图像
            self.detected_image_label.setPixmap(pixmap.scaled(self.detected_image_label.width(), self.detected_image_label.height(), Qt.KeepAspectRatio))

            print("处理图像: " + image_path)


    def auto_process_image(self):
        if self.images:
            for i in range(len(self.images)):
                self.show_image()
                self.process_image()
                self.current_image_index = (self.current_image_index + 1) % len(self.images)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageViewer()
    ex.show()
    sys.exit(app.exec_())





























    