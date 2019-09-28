import PyQt5 as pyqt5
import PyQt5.Qt as qt
import PyQt5.QtCore as qtcore
import PyQt5.QtGui as qtgui
import PyQt5.QtWidgets as wigs

import Controls.OptionsControls as option_controls


class StartGameWindow(wigs.QDialog):
    def __init__(self, *args, **kwargs):
        super(StartGameWindow, self).__init__(*args, **kwargs)

        # -- TODO: Create space for current running game widget

        self.loaded_options = option_controls.load_options()
        self.snake_speed = self.loaded_options.snake_speed
        self.snake_length = self.loaded_options.snake_start_length
        self.snake_points = 0

        self.init_components()

    def init_components(self):
        # -- Button to quit current runing game
        self.quit_game_button_text = 'Quit'
        self.quit_game_button = wigs.QPushButton()
        self.quit_game_button.setText(self.quit_game_button_text)
        self.quit_game_button.clicked.connect(self.__quit_game_button_clicked)

        # -- Label to show current points
        self.current_points_label_text = 'Points: '
        self.current_points_label = wigs.QLabel(self.current_points_label_text)
        self.current_points_value_label = wigs.QLabel(str(0))
        self.current_points_hbox = wigs.QHBoxLayout()
        self.current_points_hbox.addWidget(self.current_points_label)
        self.current_points_hbox.addWidget(self.current_points_value_label)

        # -- Label to show current snake length
        self.current_snake_length_label_text = 'Snake length: '
        self.current_snake_length_label = wigs.QLabel(self.current_snake_length_label_text)
        self.current_snake_length_value_label = wigs.QLabel(str(self.loaded_options.snake_start_length))
        self.current_snake_length_hbox = wigs.QHBoxLayout()
        self.current_snake_length_hbox.addWidget(self.current_snake_length_label)
        self.current_snake_length_hbox.addWidget(self.current_snake_length_value_label)

        # -- Label to show current snake speed
        self.current_snake_speed_label_text = 'Snake speed: '
        self.current_snake_speed_label = wigs.QLabel(self.current_snake_speed_label_text)
        self.current_snake_speed_value_label = wigs.QLabel(str(self.loaded_options.snake_speed))
        self.current_snake_speed_hbox =  wigs.QHBoxLayout()
        self.current_snake_speed_hbox.addWidget(self.current_snake_speed_label)
        self.current_snake_speed_hbox.addWidget(self.current_snake_speed_value_label)

        # -- Layout to hold all snakey information
        self.snake_info_vbox = wigs.QVBoxLayout()
        self.snake_info_vbox.addStretch(1)
        self.snake_info_vbox.addLayout(self.current_points_hbox)
        self.snake_info_vbox.addLayout(self.current_snake_length_hbox)
        self.snake_info_vbox.addLayout(self.current_snake_speed_hbox)
        self.snake_info_vbox.addStretch(1)

        # -- Layout to hold all bottom panel things
        self.bottom_panel_hbox = wigs.QHBoxLayout()
        self.bottom_panel_hbox.addLayout(self.snake_info_vbox)
        self.bottom_panel_hbox.addStretch(1)
        self.bottom_panel_hbox.addWidget(self.quit_game_button)

        self.setLayout(self.bottom_panel_hbox)

    def __quit_game_button_clicked(self):
        self.close()
