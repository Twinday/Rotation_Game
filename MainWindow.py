from GameLogics import Level
import colors as c
from Game_interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox



class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.g = Level()
        self.rect = self.g.getRect()
        self.score = self.g.get_score()
        self.level = 1

        self.time = 50
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_tick)

        self.StartButton.clicked.connect(self.start)

    def keyPressEvent(self, event):
        dict = {
            QtCore.Qt.Key_W: self.up,
            QtCore.Qt.Key_S: self.down,
            QtCore.Qt.Key_A: self.left,
            QtCore.Qt.Key_D: self.right,
            QtCore.Qt.Key_F: self.rotate
        }
        try:
            dict[event.key()]()
        except:
            pass

    def show_matrix_in_table(self):
        for row in range(self.g.GameHeight):
            for col in range(self.g.GameWidth):
                item = self.g[row, col]
                cellinfo = QTableWidgetItem(' ')
                if (row >= self.rect[0][0] and row <= self.rect[0][0] + self.rect[2] - 1) and \
                        (col >= self.rect[0][1] and col <= self.rect[0][1] + self.rect[1] - 1):
                    cellinfo = QTableWidgetItem('o')
                # Только для чтения
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                cellinfo.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                cellinfo.setFont(QtGui.QFont('SansSerif', 60))
                self.tableWidget.setItem(row, col, cellinfo)
                color = c.my_color[item]
                self.tableWidget.item(row, col).setBackground(QtGui.QColor(color[0], color[1], color[2]))

        self.score = self.g.get_score()
        self.labelScore.setText("Score: " + str(self.score))
        self.labelLevel.setText("Level " + str(self.level))
        self.labelScore.setFont(QtGui.QFont('SansSerif', 16))
        self.labelLevel.setFont(QtGui.QFont('SansSerif', 16))


    def decor_update_view(func):
        def wrapped(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.show_matrix_in_table(*args, **kwargs)
        return wrapped

    # Описываем функции
    @decor_update_view
    def rotate(self):
        self.g.update()
        self.check_new_level()


    @decor_update_view
    def up(self):
        self.g.move_border('up')
        self.rect = self.g.getRect()


    @decor_update_view
    def down(self):
        self.g.move_border('down')
        self.rect = self.g.getRect()


    @decor_update_view
    def left(self):
        self.g.move_border('left')
        self.rect = self.g.getRect()


    @decor_update_view
    def right(self):
        self.g.move_border('right')
        self.rect = self.g.getRect()


    def start(self):
        self.g = Level()
        self.timer.stop()
        self.time = 50
        self.level = 1
        self.g.create_level()
        self.rect = self.g.getRect()
        self.show_matrix_in_table()
        self.label_timer.setText("Time: " + str(self.time))
        self.label_timer.setFont(QtGui.QFont('SansSerif', 16))
        self.timer.start(1000)

    def check_new_level(self):
        self.score = self.g.get_score()
        if self.score >= 4000:
            self.new_level()
            self.timer.stop()
            self.time = 50
            self.timer.start(1000)

    def new_level(self):
        self.level += 1
        self.g = Level()
        self.g.create_level()
        self.score = self.g.get_score()
        self.rect = self.g.getRect()

    @decor_update_view
    def timer_tick(self):
        self.time -= 1
        self.label_timer.setText("Time: " + str(self.time))
        self.label_timer.setFont(QtGui.QFont('SansSerif', 16))
        if self.time <= 0:
            self.timer.stop()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Game Over!")
            msg.setInformativeText("Level " + str(self.level))
            msg.setWindowTitle("Game")
            msg.addButton('Новая игра', QMessageBox.AcceptRole)
            msg.exec()
            self.start()
