import sys
import PyQt5.QtWidgets as wigs
import Controls.HighScoreControls as HighScoreControls
import Components.HighScoreEntryWidget as HighScoreEntryWidget
import os


class ScrollableDataPanel(wigs.QScrollArea):
    def __init__(self, *args, **kwargs):
        super(ScrollableDataPanel, self).__init__(*args, **kwargs)

        self.min_width = 250
        self.min_height = 250
        self.high_scores = HighScoreControls.load_high_scores_from_file()

        self.init_components()

    def init_components(self):
        self.setMinimumWidth(self.min_width)
        self.setMinimumHeight(self.min_height)

        list_widget = wigs.QListWidget()
        # -- Populate list widget
        for idx, item in enumerate(self.high_scores):
            list_item_widget = wigs.QListWidgetItem(list_widget)
            high_score = HighScoreEntryWidget.HighScoreEntryWidget(idx + 1, item[0], item[1])
            list_item_widget.setSizeHint(high_score.sizeHint())
            list_widget.addItem(list_item_widget)
            list_widget.setItemWidget(list_item_widget, high_score)

        # -- Configure layouts and add widget
        v_box_layout = wigs.QVBoxLayout()
        v_box_layout.addWidget(list_widget)

        h_box_layout = wigs.QHBoxLayout()
        h_box_layout.addLayout(v_box_layout)

        self.setLayout(h_box_layout)