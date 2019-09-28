
MAX_SNAKE_SPEED = 10
MIN_SNAKE_SPEED = 1

MAX_SNAKE_START_LENGTH = 10
MIN_SNAKE_START_LENGTH = 5

class Options:
    def __init__(self, *args, **kwargs):
        self.snake_speed = 5
        self.snake_start_length = 3

    def __str__(self):
        return f'Snake speed: {self.snake_speed}, Snake start length: {self.snake_start_length}'
