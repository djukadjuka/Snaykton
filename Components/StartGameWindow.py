import PyQt5 as pyqt5
import PyQt5.Qt as qt
import PyQt5.QtCore as qtcore
import PyQt5.QtGui as qtgui
import PyQt5.QtWidgets as wigs

import Controls.OptionsControls as option_controls
from Components.GameWidget import GameWidget
from Controls import HighScoreControls
from Models.GameStatusModel import GameStatusModel


class StartGameWindow(wigs.QDialog):
    def __init__(self, *args, **kwargs):
        super(StartGameWindow, self).__init__(*args, **kwargs)

        self.loaded_options = option_controls.load_options()
        self.game_status = GameStatusModel()
        self.game_status.snake_length = self.loaded_options.snake_start_length
        self.game_status.snake_speed = self.loaded_options.snake_speed
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
        self.quit_game_button.clearFocus()

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

        self.game_widget = GameWidget(self.game_status, self)
        self.game_widget.focusWidget()

        self.main_layout = wigs.QVBoxLayout()
        self.main_layout.addWidget(self.game_widget)
        self.main_layout.addLayout(self.bottom_panel_hbox)

        self.setLayout(self.main_layout)

    def increase_points(self, points):
        self.current_points_value_label.setText(str(points))

    def increase_snake_length(self, length):
        self.current_snake_length_value_label.setText(str(length))

    def increase_snake_length_value(self, length):
        self.current_snake_length_value_label.setText(str(length))

    def __quit_game_button_clicked(self):
        self.game_widget.game_timer.stop()
        self.close()

    def closeEvent(self, a0: qtgui.QCloseEvent) -> None:
        if self.game_status.snake_pulse == self.game_status.SNAKE_PULSE_ALIVE:
            super(StartGameWindow, self).closeEvent(a0)
            return

        high_scores = HighScoreControls.load_high_scores_from_file()
        all_scores = [hs[1] for hs in high_scores]

        eulogy = 'It looks like you have died ... :(\n'
        eulogy += 'Your final stats are as follows: \n'
        eulogy += str(self.game_status)

        # -- If there is not a new high score, then a basic message box can be displayed
        if all_scores[len(all_scores) - 1] >= self.game_status.points:
            msgbox = wigs.QMessageBox()
            msgbox.setWindowTitle('Game Over')
            msgbox.setText(eulogy)
            msgbox.exec()
        else:
            death_dialog = wigs.QDialog()
            death_dialog.setWindowTitle('$ NEW HIGH SCORE! $')
            death_dialog_v_box = wigs.QVBoxLayout()

            death_dialog_label = wigs.QLabel(eulogy)

            death_dialog_name_input = wigs.QLineEdit()
            death_dialog_name_input_label = wigs.QLabel('Your Name: ')
            death_dialog_name_okay_button = wigs.QPushButton('OK')
            death_dialog_name_okay_button.setEnabled(False)
            def death_dialog_okay_button_clicked():
                for (idx, hs) in enumerate(high_scores):
                    if hs[1] < self.game_status.points:
                        high_scores.insert(idx, [death_dialog_name_input.text(), self.game_status.points])
                        break
                high_scores.pop()
                HighScoreControls.save_high_scores_to_file(high_scores)
                death_dialog.close()
            death_dialog_name_okay_button.clicked.connect(death_dialog_okay_button_clicked)
            death_dialog_name_h_layout = wigs.QHBoxLayout()
            death_dialog_name_h_layout.addWidget(death_dialog_name_input_label)
            death_dialog_name_h_layout.addWidget(death_dialog_name_input)
            def name_text_changed():
                txt = death_dialog_name_input.text()
                if len(txt) == 0 or len(txt) > 20:
                    death_dialog_name_okay_button.setEnabled(False)
                else:
                    death_dialog_name_okay_button.setEnabled(True)
            death_dialog_name_input.textChanged.connect(name_text_changed)
            death_dialog_name_v_layout = wigs.QVBoxLayout()
            death_dialog_name_v_layout.addLayout(death_dialog_name_h_layout)
            death_dialog_name_v_layout.addWidget(death_dialog_name_okay_button)

            death_dialog_v_box.addWidget(death_dialog_label)
            death_dialog_v_box.addLayout(death_dialog_name_v_layout)

            death_dialog_h_box = wigs.QHBoxLayout()
            death_dialog_h_box.addLayout(death_dialog_v_box)

            death_dialog.setLayout(death_dialog_h_box)
            death_dialog.setModal(True)
            death_dialog.exec_()
            pass


        super(StartGameWindow, self).closeEvent(a0)
