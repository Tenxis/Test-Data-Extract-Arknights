from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton('button!',self)
        btn.setGeometry(0,0,200,100)
        btn.setToolTip('hint')
        btn.setText('reseted')
        lb = QLabel('lable here',self)

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()