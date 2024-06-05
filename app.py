from PyQt6.QtWidgets import QApplication
from game import field
import sys

def setup():
    app = QApplication(sys.argv)

    game_field = field.GameField()
    game_field.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing game...')

if __name__ == '__main__':
    setup()