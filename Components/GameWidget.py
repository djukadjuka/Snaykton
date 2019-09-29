import sys
import PyQt5 as pyqt5
import PyQt5.Qt as qt
import PyQt5.QtCore as qtcore
import PyQt5.QtGui as qtgui
import PyQt5.QtWidgets as wigs
import os
import random

from Components import StartGameWindow
from Models.GameStatusModel import GameStatusModel


class GameWidget(wigs.QWidget):
    def __init__(self, game_status: GameStatusModel, parent: StartGameWindow, *args, **kwargs):
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
        # -- Save parent to increase view points
        self.parent = parent

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

        # -- Initialize food
        self.food_position = None
        self.special_food_position = None

        self.start()

    def paintEvent(self, event):
        self.game_painter.begin(self)
        self.painter_set_basic_painter()
        self.game_painter.drawRect(0, 0, self.window_min_width - 1, self.window_min_height - 1)
        self.draw_food()
        self.draw_special_food()
        # -- Check if snake ate the food here
        self.draw_snake()
        self.game_painter.end()

    def draw_snake(self):
        self.painter_set_snake_painter()
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

        for snake_cell in self.snake_cells:
            self.game_painter.drawRect(snake_cell[0],
                                       snake_cell[1],
                                       self.snake_cell_size,
                                       self.snake_cell_size)

        self.food_eaten()
        self.special_food_eaten()

        self.snake_cells.pop(0)
        self.snake_cells.append((
                self.snake_cells[len(self.snake_cells)-1][0] + offset_x,
                self.snake_cells[len(self.snake_cells)-1][1] + offset_y
        ))

    def draw_food(self):
        self.painter_set_food_painter()
        if self.food_position is None:
            self.generate_food()
            if self.game_status.food_ate % 3 == 0 and self.game_status.food_ate != 0:
                self.generate_special_food()
        self.game_painter.drawEllipse(self.food_position[0], self.food_position[1], self.snake_cell_size, self.snake_cell_size)

    def draw_special_food(self):
        if self.special_food_position is None:
            return
        self.painter_set_special_food_painter()
        self.game_painter.drawEllipse(self.special_food_position[0], self.special_food_position[1], self.snake_cell_size, self.snake_cell_size)

    def generate_food(self):
        xmin, xmax = 1, (self.window_min_width - 6) / 5
        ymin, ymax = 1, (self.window_min_height - 6) / 5

        food_x = None
        food_y = None

        while food_x is None or food_y is None or (food_x, food_y) in self.snake_cells:
            food_x = random.randint(xmin, xmax) * 5
            food_y = random.randint(ymin, ymax) * 5

        self.food_position = (food_x, food_y)

    def generate_special_food(self):
        self.painter_set_special_food_painter()
        xmin, xmax = 1, (self.window_min_width - 6) / 5
        ymin, ymax = 1, (self.window_min_height - 6) / 5

        special_food_x = None
        special_food_y = None

        while special_food_x is None or special_food_y is None or \
                (special_food_x, special_food_y) in self.snake_cells or \
                (special_food_x, special_food_y) == self.food_position:
            special_food_x = random.randint(xmin, xmax) * 5
            special_food_y = random.randint(ymin, ymax) * 5

        self.special_food_position = (special_food_x, special_food_y)

    def painter_set_snake_painter(self):
        self.game_painter.setPen(qt.QPen(qt.QColor(0, 0, 0), 1, qtcore.Qt.SolidLine))
        self.game_painter.setBrush(qt.QBrush(qt.QColor(0, 255, 0), qtcore.Qt.SolidPattern))

    def painter_set_basic_painter(self):
        self.game_painter.setPen(qt.QPen(qt.QColor(0, 0, 0), 1, qtcore.Qt.SolidLine))
        # self.game_painter.setBrush(qtcore.Qt.NoBrush)
        self.game_painter.setBrush(qt.QBrush(qt.QColor(254, 254, 254), qtcore.Qt.Dense4Pattern))
        pass

    def painter_set_food_painter(self):
        self.game_painter.setPen(qt.QPen(qt.QColor(0, 255, 0), 1, qtcore.Qt.SolidLine))
        self.game_painter.setBrush(qt.QBrush(qt.QColor(0, 200, 0), qtcore.Qt.SolidPattern))

    def painter_set_special_food_painter(self):
        self.game_painter.setPen(qt.QPen(qt.QColor(0, 0, 0), 1, qtcore.Qt.SolidLine))
        self.game_painter.setBrush(qt.QBrush(qt.QColor(255, 0, 0), qtcore.Qt.Dense3Pattern))

    def calculate_snake_speed(self):
        self.timer_speed = 1000 - (95 * self.game_status.snake_speed)

    def food_eaten(self):
        snake_head = self.snake_cells[len(self.snake_cells) - 1]
        snake_head_x = snake_head[0]
        snake_head_y = snake_head[1]
        food_x, food_y = self.food_position
        if snake_head_x == food_x and snake_head_y == food_y:
            self.game_status.food_ate += 1
            self.increase_points(1)
            self.food_position = None
            return True
        return False

    def special_food_eaten(self):
        if self.special_food_position is None:
            return False
        snake_head = self.snake_cells[len(self.snake_cells) - 1]
        snake_head_x = snake_head[0]
        snake_head_y = snake_head[1]
        food_x, food_y = self.special_food_position
        if snake_head_x == food_x and snake_head_y == food_y:
            self.game_status.special_food_ate += 1
            self.increase_points(3)
            self.special_food_position = None
            return True
        return False

    def increase_points(self, points):
        self.game_status.points += points
        self.parent.increase_points(self.game_status.points)

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

    def start(self):
        self.is_game_started = True
        self.game_timer.start(self.timer_speed, self)
        self.repaint()

    """Where update should go"""
    def timerEvent(self, event):
        self.repaint()
