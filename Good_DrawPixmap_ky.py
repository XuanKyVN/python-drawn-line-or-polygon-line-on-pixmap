import sys,cv2
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPixmap, QPainter,QImage,QPen
from PyQt5 import QtCore, QtGui, QtWidgets
from labelscreen import *
from PyQt5.QtWidgets import  QApplication,QMainWindow,QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()

        self.uic.setupUi(self)
        img = cv2.imread(r'C:/Users\Admin\PythonLession\CarPlate\images\BSXe_tested/0144_00471_b.jpg')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pix = QPixmap.fromImage(QImg)
        self.uic.label_img.setPixmap(QtGui.QPixmap.fromImage(QImg))

        self.begin, self.destination = QPoint(), QPoint()


    def paintEvent(self, event):
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(255, 0, 0))
        #painter = QPainter(self)
        painter = QtGui.QPainter(self.uic.label_img.pixmap())

        painter.drawPixmap(QPoint(), self.pix)
        painter.setPen(pen)

        if not self.begin.isNull() and not self.destination.isNull():
            rect = QRect(self.begin, self.destination)
            painter.drawRect(rect.normalized())
            #painter.drawLine(self.begin.x(),self.begin.y(), self.destination.x(),self.destination.y())



    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            print('Point 1')
            self.begin = event.pos()
            self.destination = self.begin
            self.update()


    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            print('Point 2')
            self.destination = event.pos()
            self.update()


    def mouseReleaseEvent(self, event):
        print('Point 3')
        if event.button() & Qt.LeftButton:
            rect = QRect(self.begin, self.destination)
            painter = QPainter(self.pix)

            pen = QtGui.QPen()
            pen.setWidth(3)
            pen.setColor(QtGui.QColor(255, 0, 0))

            painter.drawPixmap(QPoint(), self.pix)
            painter.setPen(pen)
            painter.drawRect(rect.normalized())
            #painter.drawLine(self.begin.x(),self.begin.y(), self.destination.x(),self.destination.y())

            self.begin, self.destination = QPoint(), QPoint()
            self.update()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
'''
class MyApp(QWidget,object):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 1200, 800
        self.setMinimumSize(self.window_width, self.window_height)


        layout = QVBoxLayout()
        self.setLayout(layout)

        #self.pix = QPixmap(self.rect().size())
        #self.pix.fill(Qt.white)


        img = cv2.imread(r'C:/Users\Admin\PythonLession\CarPlate\images\BSXe_tested/0144_00471_b.jpg')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pix = QPixmap.fromImage(QImg)




        self.begin, self.destination = QPoint(), QPoint()

    def paintEvent(self, event):
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(255, 0, 0))
        painter = QPainter(self)

        painter.drawPixmap(QPoint(), self.pix)
        painter.setPen(pen)

        if not self.begin.isNull() and not self.destination.isNull():
            rect = QRect(self.begin, self.destination)
            painter.drawRect(rect.normalized())


    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            print('Point 1')
            self.begin = event.pos()
            self.destination = self.begin
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            print('Point 2')
            self.destination = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        print('Point 3')
        if event.button() & Qt.LeftButton:


            rect = QRect(self.begin, self.destination)
            painter = QPainter(self.pix)

            pen = QtGui.QPen()
            pen.setWidth(3)
            pen.setColor(QtGui.QColor(255, 0, 0))


            painter.drawPixmap(QPoint(), self.pix)
            painter.setPen(pen)
            painter.drawRect(rect.normalized())

            self.begin, self.destination = QPoint(), QPoint()
            self.update()


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
'''