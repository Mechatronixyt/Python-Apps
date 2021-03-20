# creator: @Mechatronix
# date: 20.03.2021
# lisencs: MIT
# contact: mechatronix@mail.de

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint

import sys

class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        top = 400
        left = 400
        width = 800
        height = 600

        self.setWindowTitle("Painter")

        self.setGeometry(top, left, width, height)

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.drawing = False

        self.brush_size = 2

        self.brush_color = Qt.black

        self.last_point = QPoint

        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("File")

        brush_menu = main_menu.addMenu("Brush Size")

        color_menu = main_menu.addMenu("Brush Color")

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save)

        clear_action = QAction("Clear", self)
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        one_px_action = QAction("1 px", self)
        one_px_action.setShortcut("Ctrl+1")
        brush_menu.addAction(one_px_action)
        one_px_action.triggered.connect(self.one_px)

        two_px_action = QAction("2 px", self)
        two_px_action.setShortcut("Ctrl+2")
        brush_menu.addAction(two_px_action)
        two_px_action.triggered.connect(self.two_px)

        three_px_action = QAction("3 px", self)
        three_px_action.setShortcut("Ctrl+3")
        brush_menu.addAction(three_px_action)
        three_px_action.triggered.connect(self.three_px)

        four_px_action = QAction("4 px", self)
        four_px_action.setShortcut("Ctrl+4")
        brush_menu.addAction(four_px_action)
        four_px_action.triggered.connect(self.four_px)

        five_px_action = QAction("5 px", self)
        five_px_action.setShortcut("Ctrl+5")
        brush_menu.addAction(five_px_action)
        five_px_action.triggered.connect(self.five_px)

        six_px_action = QAction("6 px", self)
        six_px_action.setShortcut("Ctrl+6")
        brush_menu.addAction(six_px_action)
        six_px_action.triggered.connect(self.six_px)

        seven_px_action = QAction("7 px", self)
        seven_px_action.setShortcut("Ctrl+7")
        brush_menu.addAction(seven_px_action)
        seven_px_action.triggered.connect(self.seven_px)

        eight_px_action = QAction("8 px", self)
        eight_px_action.setShortcut("Ctrl+8")
        brush_menu.addAction(eight_px_action)
        eight_px_action.triggered.connect(self.eight_px)

        nine_px_action = QAction("9 px", self)
        nine_px_action.setShortcut("Ctrl+9")
        brush_menu.addAction(nine_px_action)
        nine_px_action.triggered.connect(self.nine_px)

        black_color_action = QAction("Black", self)
        black_color_action.setShortcut("Ctrl+Shift+B")
        color_menu.addAction(black_color_action)
        black_color_action.triggered.connect(self.color_black)

        white_color_action = QAction("White", self)
        white_color_action.setShortcut("Ctrl+Shift+W")
        color_menu.addAction(white_color_action)
        white_color_action.triggered.connect(self.color_white)

        red_color_action = QAction("Red", self)
        red_color_action.setShortcut("Ctrl+R")
        color_menu.addAction(red_color_action)
        red_color_action.triggered.connect(self.color_red)

        green_color_action = QAction("Green", self)
        green_color_action.setShortcut("Ctrl+G")
        color_menu.addAction(green_color_action)
        green_color_action.triggered.connect(self.color_green)

        blue_color_action = QAction("Blue", self)
        blue_color_action.setShortcut("Ctrl+B")
        color_menu.addAction(blue_color_action)
        blue_color_action.triggered.connect(self.color_blue)

        cyan_color_action = QAction("Cyan", self)
        cyan_color_action.setShortcut("Ctrl+C")
        color_menu.addAction(cyan_color_action)
        cyan_color_action.triggered.connect(self.color_cyan)

        yellow_color_action = QAction("Yellow", self)
        yellow_color_action.setShortcut("Ctrl+Y")
        color_menu.addAction(yellow_color_action)
        yellow_color_action.triggered.connect(self.color_yellow)

        purple_color_action = QAction("Purple", self)
        purple_color_action.setShortcut("Ctrl+P")
        color_menu.addAction(purple_color_action)
        purple_color_action.triggered.connect(self.color_purple)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.drawing = True

            self.last_point = event.pos()

    def mouseMoveEvent(self, event):

        if (event.buttons() & Qt.LeftButton) & self.drawing:

                painter = QPainter(self.image)

                painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

                painter.drawLine(self.last_point, event.pos())

                self.last_point = event.pos()

                self.update()

    def mouseReleaseEvent(self, event):

        if event.button == Qt.LeftButton:

            self.drawing = False

    def paintEvent(self, event):

        canvas_painter = QPainter(self)

        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):

        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;ALL Files(*.*)")

        if file_path == "":

            return

        self.image.save(file_path)

    def clear(self):

        self.image.fill(Qt.white)
        self.update()

    def one_px(self):

        self.brush_size = 1

    def two_px(self):

        self.brush_size = 2

    def three_px(self):

        self.brush_size = 3

    def four_px(self):

        self.brush_size = 4

    def five_px(self):

        self.brush_size = 5

    def six_px(self):

        self.brush_size = 6

    def seven_px(self):

        self.brush_size = 7

    def eight_px(self):

        self.brush_size = 8

    def nine_px(self):

        self.brush_size = 9

    def color_black(self):

        self.brush_color = Qt.black

    def color_white(self):

        self.brush_color = Qt.white

    def color_red(self):

        self.brush_color = Qt.red

    def color_green(self):

        self.brush_color = Qt.green

    def color_blue(self):

        self.brush_color = Qt.blue

    def color_yellow(self):

        self.brush_color = Qt.yellow

    def color_cyan(self):

        self.brush_color = Qt.cyan

    def color_purple(self):

        self.brush_color = Qt.magenta

if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    app.exec()