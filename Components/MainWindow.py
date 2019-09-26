import sys
import PyQt5.QtWidgets as wigs
import PyQt5.QtCore as qtCore
from Components.HighScorePanel import HighScorePanel


class MainWindow(wigs.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # -- Setup methods
        self.housekeeping()

        # -- Initialize Components
        self.init_components()

        # -- Register actions
        # self.actions_setup()

        self.__move_window_to_center()

        self.show()

    def housekeeping(self):
        # -- Set width and height of the window
        # -- Attributes
        self.window_min_width = 640
        self.window_min_height = 480
        self.setMinimumWidth(self.window_min_width)
        self.setMinimumHeight(self.window_min_height)

    def init_components(self):
        # -- Init start game button
        self.start_game_button = wigs.QPushButton()
        self.start_game_button.setText('Start Game')
        self.start_game_button.setShortcut('Ctrl+S')
        # self.start_game_action = wigs.QAction('&Start Game', self)
        # self.start_game_action.setShortcut('Ctrl+S')
        # self.start_game_action.triggered.connect(self.__start_game)
        # self.start_game_button.addAction(self.start_game_action)
        self.start_game_button.clicked.connect(self.__start_game)

        # -- Init high scores button
        self.show_high_scores_button = wigs.QPushButton()
        self.show_high_scores_button.setText('High Scores')
        self.show_high_scores_button.setShortcut('Ctrl+H')
        # self.show_high_scores_action = wigs.QAction('&High Scores', self)
        # self.show_high_scores_action.setShortcut('Ctrl+H')
        # self.show_high_scores_action.triggered.connect(self.__show_high_scores)
        # self.show_high_scores_button.addAction(self.show_high_scores_action)
        self.show_high_scores_button.clicked.connect(self.__show_high_scores)

        # -- Init options button
        self.options_button = wigs.QPushButton()
        self.options_button.setText('Options')
        self.options_button.setShortcut('Ctrl+O')
        # self.options_action = wigs.QAction('&Options', self)
        # self.options_action.setShortcut('Ctrl+O')
        # self.options_action.triggered.connect(self.__show_options)
        # self.options_button.addAction(self.options_action)
        self.options_button.clicked.connect(self.__show_options)

        # -- Init quit button
        self.quit_button = wigs.QPushButton()
        self.quit_button.setText('Quit')
        self.quit_button.setShortcut('Ctrl+Q')
        # self.quit_action = wigs.QAction('Quit', self)
        # self.quit_action.setShortcut('Ctrl+Q')
        # self.quit_action.triggered.connect(self.__quit_application)
        # self.quit_button.addAction(self.quit_action)
        self.quit_button.clicked.connect(self.__quit_application)

        # -- Add components to vertical layout
        self.vertical_layout = wigs.QVBoxLayout()
        # self.vertical_layout.addStretch(1)
        self.vertical_layout.addWidget(self.start_game_button)
        self.vertical_layout.addWidget(self.show_high_scores_button)
        self.vertical_layout.addWidget(self.options_button)
        self.vertical_layout.addWidget(self.quit_button)
        # self.vertical_layout.setContentsMargins(0, 20, 0, 20)
        # self.vertical_layout.addStretch(1)

        # -- Add vertical layout to horizontal layout
        self.horizontal_layout = wigs.QHBoxLayout()
        # self.horizontal_layout.addStretch(1)
        self.horizontal_layout.addLayout(self.vertical_layout)
        # self.horizontal_layout.addStretch(1)
        self.horizontal_layout.setContentsMargins(100, 100, 100, 100)

        self.container_widget = wigs.QWidget()
        self.container_widget.setLayout(self.horizontal_layout)
        self.setCentralWidget(self.container_widget)

    def __show_options(self):
        print('Show options')

    def __show_high_scores(self):
        high_score_window = wigs.QMainWindow(parent=self)
        high_score_window.setWindowModality(True)
        hsp = HighScorePanel()
        high_score_window.setCentralWidget(hsp)
        high_score_window.show()

    def __start_game(self):
        print('Start Game')

    def __quit_application(self):
        sys.exit(0)

    def __move_window_to_center(self):
        # -- This returns a point in the center of the current screen
        center_point = wigs.QDesktopWidget().availableGeometry().center()
        # -- Get the main rectangle of this window
        main_rectangle = self.frameGeometry()
        # -- Move the main rectangles center to the point you found as the center of the screen
        main_rectangle.moveCenter(center_point)
