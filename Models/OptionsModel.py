
class Options:
    def __init__(self, *args, **kwargs):
        self.snake_speed = 10
        self.snake_start_length = 3

    def __str__(self):
        return f'Snake speed: {self.snake_speed}, Snake start length: {self.snake_start_length}'
