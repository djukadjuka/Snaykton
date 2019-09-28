import PyQt5.QtWidgets as wigs
import PyQt5.QtGui as qtgui
import PyQt5.QtCore as qtcore
import Controls.OptionsControls as OptionsControls


class OptionsWindow(wigs.QDialog):
    def __init__(self, *args, **kwargs):
        super(OptionsWindow, self).__init__(*args, **kwargs)

        self.min_window_width = 350
        self.min_window_height = 120
        self.setMinimumWidth(self.min_window_width)
        self.setMinimumHeight(self.min_window_height)

        self.loaded_options = OptionsControls.load_options()

        # -- Setup layouts / components / ..
        self.init_components()
        self.show()

    def init_components(self):
        self.grid_layout = wigs.QGridLayout()

        # -- Snake speed options
        self.snake_speed_tooltip = 'This determines the speed at which the snake moves on the field.\n' \
                                   'It is generally more difficult to play with a faster snake.'
        self.snake_speed_label_text = 'Snake Speed: '
        self.snake_speed_label = wigs.QLabel()
        self.snake_speed_label.setText(self.snake_speed_label_text)
        self.snake_speed_label.setToolTip(self.snake_speed_tooltip)

        self.snake_speed_slider = wigs.QSlider()
        self.snake_speed_slider.setTickInterval(1)
        self.snake_speed_slider.setMaximum(10)
        self.snake_speed_slider.setMinimum(1)
        self.snake_speed_slider.setToolTip(self.snake_speed_tooltip)
        self.snake_speed_slider.setOrientation(qtcore.Qt.Horizontal)
        self.snake_speed_slider.setValue(self.loaded_options.snake_speed)
        self.snake_speed_slider.valueChanged.connect(self.__snake_speed_slider_value_changed)

        self.snake_speed_value_label = wigs.QLabel()
        # -- Enough to set only this ones minimum width, other components will follow
        self.snake_speed_value_label.setMinimumWidth(20)
        self.snake_speed_value_label.setText(str(self.loaded_options.snake_speed))

        self.grid_layout.addWidget(self.snake_speed_label, 1, 0)
        self.grid_layout.addWidget(self.snake_speed_slider, 1, 1)
        self.grid_layout.addWidget(self.snake_speed_value_label, 1, 2)

        # -- Snake length options
        self.snake_start_length_tooltip = 'This determines how long the snake will be at the start of the game.\n' \
                                          'This will most probably be removed once the level module is implemented.'
        self.snake_start_length_label_text = 'Snake start length: '
        self.snake_start_length_label = wigs.QLabel()
        self.snake_start_length_label.setText(self.snake_start_length_label_text)
        self.snake_start_length_label.setToolTip(self.snake_start_length_tooltip)

        self.snake_start_length_slider = wigs.QSlider()
        self.snake_start_length_slider.setTickInterval(1)
        self.snake_start_length_slider.setMaximum(10)
        self.snake_start_length_slider.setMinimum(1)
        self.snake_start_length_slider.setOrientation(qtcore.Qt.Horizontal)
        self.snake_start_length_slider.setValue(self.loaded_options.snake_start_length)
        self.snake_start_length_slider.valueChanged.connect(self.__snake_start_length_slider_value_changed)

        self.snake_start_length_value_label = wigs.QLabel()
        self.snake_start_length_value_label.setText(str(self.loaded_options.snake_start_length))

        self.grid_layout.addWidget(self.snake_start_length_label, 2, 0)
        self.grid_layout.addWidget(self.snake_start_length_slider, 2, 1)
        self.grid_layout.addWidget(self.snake_start_length_value_label, 2, 2)

        # -- Configure Header
        self.header_text = '$ Options $'
        self.header_text_font = qtgui.QFont('Courier', 16, qtgui.QFont.Bold)
        self.header_label = wigs.QLabel()
        self.header_label.setText(self.header_text)
        self.header_label.setFont(self.header_text_font)
        self.header_label.setAlignment(qtcore.Qt.AlignHCenter | qtcore.Qt.AlignVCenter)
        self.header_label.setStyleSheet('border: 2px dashed black')
        self.grid_layout.addWidget(self.header_label, 0, 0, 1, 3)

        # -- Configure back and apply buttons
        self.apply_button_text = 'Apply'
        self.apply_button = wigs.QPushButton()
        self.apply_button.setText(self.apply_button_text)
        self.apply_button.clicked.connect(self.__apply_button_clicked)

        self.back_button_text = 'Back'
        self.back_button = wigs.QPushButton()
        self.back_button.setText(self.back_button_text)
        self.back_button.clicked.connect(self.__back_button_clicked)

        self.button_layout = wigs.QHBoxLayout()
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.apply_button)
        self.button_layout.addWidget(self.back_button)
        self.button_layout.addStretch(1)

        self.grid_layout.addLayout(self.button_layout, 3, 0, 1, 3)

        self.setLayout(self.grid_layout)
        self.setModal(True)

    def __snake_start_length_slider_value_changed(self):
        self.loaded_options.snake_start_length = int(self.snake_start_length_slider.value())
        self.snake_start_length_value_label.setText(str(self.loaded_options.snake_start_length))

    def __snake_speed_slider_value_changed(self):
        self.loaded_options.snake_speed = int(self.snake_speed_slider.value())
        self.snake_speed_value_label.setText(str(self.loaded_options.snake_speed))

    def __apply_button_clicked(self):
        print(f'Apply button clicked!')

    def __back_button_clicked(self):
        self.close()
