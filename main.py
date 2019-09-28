# -- My imports
import sys
import PyQt5.QtWidgets as wigs
from Components.MainWindow import MainWindow


if __name__ == '__main__':
    app = wigs.QApplication(sys.argv)

    main_window = MainWindow()

    app.exec_()
