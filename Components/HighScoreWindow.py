import sys
import PyQt5.QtWidgets as wigs
import PyQt5.QtGui as qtgui
import PyQt5.QtCore as qtcore
import Controls.HighScoreControls as HighScoreControls
from Components.ScrollableDataPanel import ScrollableDataPanel


class HighScoreWindow(wigs.QDialog):

    def __init__(self, *args, **kwargs):
        super(HighScoreWindow, self).__init__(*args, **kwargs)

        self.min_width = 320
        self.min_height = 360

        self.setMinimumHeight(self.min_height)
        self.setMinimumWidth(self.min_width)
        self.header_text = '$ High Scores $'

        # -- Setup layouts / components / ..
        self.init_components()


    def init_components(self):
        # -- Configure Header
        header_label = wigs.QLabel(self)
        header_label.setText(self.header_text)
        header_label_font = qtgui.QFont('Courier', 16, qtgui.QFont.Bold)
        header_label.setAlignment(qtcore.Qt.AlignHCenter)
        header_label.setFont(header_label_font)
        header_label.setStyleSheet('border: 2px dashed black')

        # -- Configure Scrollable data panel
        scrollable_data_panel = ScrollableDataPanel()

        # -- Configure Back Button
        back_button = wigs.QPushButton()
        back_button.setText('Back')
        back_button.clicked.connect(self.__back_button_clicked)

        # -- Configure Layout for components
        vbox_layout = wigs.QVBoxLayout()
        # vbox_layout.addStretch(1)
        vbox_layout.setSpacing(20)
        vbox_layout.addWidget(header_label)
        vbox_layout.addWidget(scrollable_data_panel)
        vbox_layout.addWidget(back_button)
        # vbox_layout.addStretch(1)

        # -- After every vertical widg is set, add
        # add the vertical layout to the horizontal layout to put everything in the center
        hbox_layout = wigs.QHBoxLayout()
        hbox_layout.addLayout(vbox_layout)
        hbox_layout.setContentsMargins(20, 10, 20, 10)

        self.setLayout(hbox_layout)
        self.setModal(True)
        self.show()

    def __back_button_clicked(self):
        self.close()

    def __move_window_to_center(self):
        center_point = wigs.QDesktopWidget().availableGeometry().center()
        main_rectangle = self.frameGeometry()
        main_rectangle.moveCenter(center_point)
