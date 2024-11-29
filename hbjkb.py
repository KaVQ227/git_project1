import random
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)  # Загружаем дизайн
        print('8')
        self.flag = False
        self.pushButton.clicked.connect(self.draw)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def draw(self):
        print('9')
        self.size = random.randint(10, 100)
        self.color = 'yellow'
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(self.color))
            qp.setBrush(QColor(self.color))
            self.x, self.y = random.randint(100, 800 - 100), random.randint(100, 900 - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())