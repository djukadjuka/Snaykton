import PyQt5.QtWidgets as wigs


class HighScoreEntryWidget(wigs.QWidget):
    def __init__(self, index='#', name='N/A', score=100, *args, **kwargs):
        super(HighScoreEntryWidget, self).__init__(*args, **kwargs)

        self.index = index
        self.name = name
        self.score = score

        self.init_components()

    def init_components(self):
        index_widget = wigs.QLabel()
        index_widget.setText(str(self.index))

        name_widget = wigs.QLabel()
        name_widget.setText(str(self.name))

        score_widget = wigs.QLabel()
        score_widget.setText(str(self.score))

        hbox_layout = wigs.QHBoxLayout()
        hbox_layout.addWidget(index_widget)
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(name_widget)
        hbox_layout.addStretch(1)
        hbox_layout.addWidget(score_widget)

        self.setLayout(hbox_layout)
