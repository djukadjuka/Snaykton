
class GameStatusModel():
    def __init__(self, points=0, snake_speed=0, snake_length=0, food_ate=0, special_food_ate=0, *args, **kwargs):
        self.points = points
        self.snake_speed = snake_speed
        self.snake_length = snake_length
        self.food_ate = food_ate
        self.special_food_ate = special_food_ate
