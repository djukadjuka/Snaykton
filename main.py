import sys
import PyQt5.QtWidgets as wigs

# -- My imports
import Components.MainWindow as MainWindow

if __name__ == '__main__':
    app = wigs.QApplication(sys.argv)

    main_window = MainWindow.MainWindow()

    app.exec_()
