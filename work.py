import sys
print('hi')
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton,QWidget,QSlider
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.filePath , filterType = QFileDialog.getOpenFileNames()
        self.setWindowTitle('控制界面')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)


        self.Function_ui = QHBoxLayout()
        self.Function_ui1 = QHBoxLayout()
        self.Function_ui2 = QHBoxLayout()
        self.Function_ui3 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.ui()
        self.ui1()
        self.ui2()
        self.ui3()
        self.vbox.addLayout(self.Function_ui)
        self.vbox.addLayout(self.Function_ui1)
        self.vbox.addLayout(self.Function_ui2)
        self.vbox.addLayout(self.Function_ui3)
        self.central_widget.setLayout(self.vbox)

    def ui(self):
        self.button_select_file = QPushButton("切換檔案", self)
        self.label = QLabel()
        self.label.setText("完整路進與名稱: "+str(self.filePath[0]))
        self.button_select_file.clicked.connect(self.ch_fil)
        self.Function_ui.addWidget(self.label)
        self.Function_ui.addWidget(self.button_select_file)
    def ui1(self):
        button1 = QPushButton("點擊", self)
        button2 = QPushButton("點擊2", self)
        self.Function_ui1.addWidget(button1)
        self.Function_ui1.addWidget(button2)
    def ui2(self):
        button1 = QPushButton("點擊", self)
        button2 = QPushButton("點擊2", self)
        self.Function_ui2.addWidget(button1)
        self.Function_ui2.addWidget(button2)
    def ui3(self):
        slider =QSlider()
        slider.setOrientation(1)
        self.Function_ui3.addWidget(slider)
    def ch_fil(self):
        self.filePath , filterType = QFileDialog.getOpenFileNames()
        self.label.setText("完整路進與名稱: "+str(self.filePath[0]))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
