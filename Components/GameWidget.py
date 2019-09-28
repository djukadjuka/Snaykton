import sys
import PyQt5 as pyqt5
import PyQt5.Qt as qt
import PyQt5.QtCore as qtcore
import PyQt5.QtGui as qtgui
import PyQt5.QtWidgets as wigs
import os

from Models.GameStatusModel import GameStatusModel


class GameWidget(wigs.QWidget):
    def __init__(self, game_status: GameStatusModel, *args, **kwargs):
        super(GameWidget, self).__init__(*args, **kwargs)

        # == CRUCIAL FOR GETTING KEYS TO WORK
        self.setFocusPolicy(qtcore.Qt.StrongFocus)

        # -- Init some constants
        self.__DIRECTION_UP = 'UP'
        self.__DIRECTION_DOWN = 'DOWN'
        self.__DIRECTION_LEFT = 'LEFT'
        self.__DIRECTION_RIGHT = 'RIGHT'

        # -- Save game status to a local var
        self.game_status = game_status

        # -- Window configuration / size / colors ...
        self.window_min_width = 501
        self.window_min_height = 501
        self.setMinimumWidth(self.window_min_width)
        self.setMinimumHeight(self.window_min_height)

        # -- Configure painter and painting parameters
        self.game_painter = qtgui.QPainter()
        self.game_painter.setBrush(qtgui.QColor(0, 0, 0))
        self.snake_cell_size = 5
        self.snake_direction = self.__DIRECTION_RIGHT

        # -- Configure timer
        self.game_timer = qtcore.QBasicTimer()
        self.calculate_snake_speed()

        # -- Configure layout of components
        self.vbox_layout = wigs.QVBoxLayout()
        self.hbox_layout = wigs.QHBoxLayout()
        self.hbox_layout.addLayout(self.vbox_layout)
        self.setLayout(self.hbox_layout)

        # -- Initialize snake
        self.snake_cells = [(10, 10)]
        for idx in range(self.game_status.snake_length - 1):
            self.snake_cells.append((self.snake_cells[idx][0] + self.snake_cell_size, self.snake_cells[idx][1]))

        self.start()

    def paintEvent(self, event):
        print('repaint called')
        self.game_painter.begin(self)
        self.game_painter.drawRect(0, 0, self.window_min_width - 1, self.window_min_height - 1)
        self.draw_snake()
        self.game_painter.end()

    def draw_snake(self):
        offset_x = 0
        offset_y = 0

        if self.snake_direction is self.__DIRECTION_RIGHT:
            offset_x = self.snake_cell_size
        elif self.snake_direction is self.__DIRECTION_UP:
            offset_y = -self.snake_cell_size
        elif self.snake_direction is self.__DIRECTION_LEFT:
            offset_x = -self.snake_cell_size
        else:
            offset_y = self.snake_cell_size

        self.snake_cells.pop(0)
        for snake_cell in self.snake_cells:
            self.game_painter.drawRect(snake_cell[0],
                                       snake_cell[1],
                                       self.snake_cell_size,
                                       self.snake_cell_size)
        self.snake_cells.append((
                self.snake_cells[len(self.snake_cells)-1][0] + offset_x,
                self.snake_cells[len(self.snake_cells)-1][1] + offset_y
        ))


    def keyPressEvent(self, event: qtgui.QKeyEvent):
        # -- If the snake is going up or down, it can then go left or right
        if self.snake_direction == self.__DIRECTION_UP or self.snake_direction == self.__DIRECTION_DOWN:
            if event.key() == qtcore.Qt.Key_A or event.key() == qtcore.Qt.Key_Left:
                self.snake_direction = self.__DIRECTION_LEFT
                self.repaint()
            elif event.key() == qtcore.Qt.Key_D or event.key() == qtcore.Qt.Key_Right:
                self.snake_direction = self.__DIRECTION_RIGHT
                self.repaint()
        # -- If the snake is going left or right, it can then go up or down
        if self.snake_direction == self.__DIRECTION_LEFT or self.snake_direction == self.__DIRECTION_RIGHT:
            if event.key() == qtcore.Qt.Key_W or event.key() == qtcore.Qt.Key_Up:
                self.snake_direction = self.__DIRECTION_UP
                self.repaint()
            elif event.key() == qtcore.Qt.Key_S or event.key() == qtcore.Qt.Key_Down:
                self.snake_direction = self.__DIRECTION_DOWN
                self.repaint()

    def calculate_snake_speed(self):
        self.timer_speed = 1000 - (95 * self.game_status.snake_speed)
        print(self.timer_speed)

    def start(self):
        self.is_game_started = True
        self.game_timer.start(self.timer_speed, self)
        self.repaint()

    """Where update should go"""
    def timerEvent(self, event):
        self.repaint()

    def key_press_event(self, event):
        print('key press event!')

