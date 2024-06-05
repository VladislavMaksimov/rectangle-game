from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 640, 480)
    win.setWindowTitle('Rectangle game')

    win.show()
    sys.exit(app.exec())

window()