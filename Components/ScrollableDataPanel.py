import sys
import PyQt5.QtWidgets as wigs
import Controls.HighScoreControls as HighScoreControls
import Components.HighScoreEntryWidget as HighScoreEntryWidget
import os


class ScrollableDataPanel(wigs.QScrollArea):
    def __init__(self, *args, **kwargs):
        super(ScrollableDataPanel, self).__init__(*args, **kwargs)

        self.housekeeping()

        self.init_components()

    def housekeeping(self):
        self.min_width = 250
        self.min_height = 250
        self.highscores = HighScoreControls.load_high_scores_from_file()

    def init_components(self):
        self.setMinimumWidth(self.min_width)
        self.setMinimumHeight(self.min_height)

        list_widget = wigs.QListWidget()
        # -- Populate list widget
        for idx, item in enumerate(self.highscores):
            list_item_widget = wigs.QListWidgetItem(list_widget)
            highscore = HighScoreEntryWidget.HighScoreEntryWidget(idx + 1, item[0], item[1])
            list_item_widget.setSizeHint(highscore.sizeHint())
            list_widget.addItem(list_item_widget)
            list_widget.setItemWidget(list_item_widget, highscore)

        # -- Configure layouts and add widget
        vbox_layout = wigs.QVBoxLayout()
        vbox_layout.addWidget(list_widget)

        hbox_layout = wigs.QHBoxLayout()
        hbox_layout.addLayout(vbox_layout)

        self.setLayout(hbox_layout)