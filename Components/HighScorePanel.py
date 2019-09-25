import sys
import PyQt5.QtWidgets as wigs
import PyQt5.QtGui as qtgui
import Controls.HighScoreControls as HighScoreControls
from Components.ScrollableDataPanel import ScrollableDataPanel


class HighScorePanel(wigs.QWidget):

    def __init__(self, *args, **kwargs):
        super(HighScorePanel, self).__init__(*args, **kwargs)

        self.window_width = 420
        self.window_height = 640

        # -- Setup methods
        self.__housekeeping()

        # -- Setup layouts / components / ..
        self.init_components()

        self.show()

    def __housekeeping(self):
        self.setFixedHeight(self.window_height)
        self.setFixedWidth(self.window_width)
        self.header_text = '$ High Scores $'

    def init_components(self):
        # -- Configure Header
        header_label = wigs.QLabel(self)
        header_label.setText(self.header_text)
        header_label_font = qtgui.QFont('Courier', 16, qtgui.QFont.Bold)
        header_label.setFont(header_label_font)
        header_label.setStyleSheet('border: 2px dashed black')

        # -- Configure Scrollable data panel
        scrollable_data_panel = ScrollableDataPanel()

        # -- Configure Back Button

        # -- Configure Layout for components
        vbox_layout = wigs.QVBoxLayout()
        vbox_layout.addStretch(1)
        vbox_layout.addWidget(header_label)
        vbox_layout.addWidget(scrollable_data_panel)

        vbox_layout.addStretch(1)

        # -- After every vertical widg is set, add
        # add the vertical layout to the horizontal layout to put everything in the center
        hbox_layout = wigs.QHBoxLayout()
        hbox_layout.addStretch(1)
        hbox_layout.addLayout(vbox_layout)
        hbox_layout.addStretch(1)
        self.setLayout(hbox_layout)

    def __move_window_to_center(self):
        center_point = wigs.QDesktopWidget().availableGeometry().center()
        main_rectangle = self.frameGeometry()
        main_rectangle.moveCenter(center_point)
