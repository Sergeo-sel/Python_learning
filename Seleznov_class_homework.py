# 1. Create Vector class on the 2-d plane ([Optional] n-d plane). Add cross-product method.
# v = Vector(1, 3)
# u = Vector(5, 2)
#  v.cross_product(u) -> 1*5 + 3*2 = 11


from tkinter.font import ROMAN


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross_product(self, other):
        return self.x * other.x + self.y * other.y


v = Vector(1, 3)
u = Vector(5, 2)
result = v.cross_product(u)
print(result)


# 2. Implement the previous method with the magic method
# v = Vector(1, 3)
# u = Vector(5, 2)
#  v * u == 11


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross_product(self, other):
        return (v.x.__mul__(u.x)).__add__(v.y.__mul__(u.y))


v = Vector(1, 3)
u = Vector(5, 2)
result = v.cross_product(u)
print(result)


# Create a Robot class with the following attributes: orientation, position_x, position_y. The Robot class should have the following methods: 
# move, turn, and display_position. The move method should take a number of steps and move the robot in the direction it is currently facing. 
# The turn method should take a direction (left or right) and turn the robot in that direction. The display_position method should print the 
# current position of the robot.

class Robot:
    def __init__(self, orientation: str, position_x: int, position_y: int):
        try:
            position_x = int(position_x)
            position_y = int(position_y)
        except ValueError:
            print('That was wrong position value. Please use an int')
            return

        self.validate_orientation(orientation)

        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, steps_count: int):
        try:
            steps_count = int(steps_count)
        except ValueError:
            print("""That was wrong steps value.
            Please use an int as steps count""")
            return
        if self.orientation == 'up':
            self.position_y += steps_count
            return

        if self.orientation == 'down':
            self.position_y -= steps_count
            return

        if self.orientation == 'right':
            self.position_x += steps_count
            return

        if self.orientation == 'left':
            self.position_x -= steps_count
            return

    def turn(self, orientation):
        self.validate_orientation(orientation)
        return self.orientation == orientation

    def display_position(self) -> str:
        return f'Position is ({self.position_x}, {self.position_y}), ' + \
                f"orientation is '{self.orientation}'"

    def validate_orientation(self, orientation):
        if orientation.lower() not in ('up', 'down', 'left' 'right'):
            raise ValueError(
                """Sorry, your position is wrong. 
                It's possible to choose only: Up, Down,
                Right of Left position"""
                )
