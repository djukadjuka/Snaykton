
class GameStatusModel():
    def __init__(self, points=0, snake_speed=0, snake_length=0, food_ate=0, special_food_ate=0, *args, **kwargs):
        self.points = points
        self.snake_speed = snake_speed
        self.snake_length = snake_length
        self.food_ate = food_ate
        self.special_food_ate = special_food_ate
        self.SNAKE_PULSE_ALIVE = 1
        self.SNAKE_PULSE_DEAD = 0
        self.snake_pulse = self.SNAKE_PULSE_ALIVE

    def __str__(self):
        return f'Total points: {self.points}\n' \
               f'Speed played: {self.snake_speed}\n' \
               f'Total length: {self.snake_length}\n' \
               f'Total regular food ate: {self.food_ate}\n' \
               f'Total special food ate: {self.special_food_ate}\n'