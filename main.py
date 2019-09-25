# -- My imports
import sys
import PyQt5.QtWidgets as wigs
import Components.HighScoreEntryWidget as HighScoreEntryWidget

from Components.HighScorePanel import HighScorePanel
from Components.ScrollableDataPanel import ScrollableDataPanel

if __name__ == '__main__':

    app = wigs.QApplication(sys.argv)

    # main_window = MainWindow.MainWindow()

    hs_panel = HighScorePanel()
    hs_panel.show()

    # sdp = ScrollableDataPanel()

    app.exec_()
