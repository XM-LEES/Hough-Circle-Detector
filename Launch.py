
# 在这个版本中，图像标签的尺寸被固定，这避免了图框大小随图像变化的问题。
# 同时，界面的整体布局和样式也进行了调整，以达到更加美观和一致的效果。
# 确保你有一个名为 icon.png 的图标文件在应用的目录中，用于设置窗口图标，
# 这会使应用看起来更专业。如果没有图标文件，可以从这行代码中移除 setWindowIcon 相关的部分。
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 设置窗口参数
        self.setWindowTitle('图像浏览器')
        # self.setWindowIcon(QIcon('icon.png'))  # 设置窗口图标，确保当前目录下有icon.png文件
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
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(800, 600)  # 设置固定大小

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
        button_layout.addWidget(self.btn_previous)
        button_layout.addWidget(self.btn_next)
        button_layout.addWidget(self.btn_process)
        button_layout.addWidget(self.btn_auto_process)
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_open_folder)
        layout.addLayout(button_layout)
        # layout.addWidget(self.btn_open_folder)
        layout.setAlignment(Qt.AlignCenter)  # 居中布局

        self.setLayout(layout)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            self.images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
            self.modified = [False for _ in range(len(self.images))]
            self.current_image_index = 0
            self.show_image()

    def show_image(self):
        if self.images:
            pixmap = QPixmap(self.images[self.current_image_index])
            self.image_label.setPixmap(pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))

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
            # 在此添加图像处理逻辑
            if self.modified[self.current_image_index]:
                return

            self.modified[self.current_image_index] = True
            print("处理图像: " + self.images[self.current_image_index])

    def auto_process_image(self):
        if self.images:
            # 在此添加图像处理逻辑
            for i in range(len(self.images)):
                self.show_image()
                self.process_image()
                self.current_image_index = (self.current_image_index + 1) % len(self.images)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageViewer()
    ex.show()
    sys.exit(app.exec_())





























    