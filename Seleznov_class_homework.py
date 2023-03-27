# 1. Create Vector class on the 2-d plane ([Optional] n-d plane). Add cross-product method.
# v = Vector(1, 3)
# u = Vector(5, 2)
#  v.cross_product(u) -> 1*5 + 3*2 = 11


from tkinter.font import ROMAN


class Old_vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cross_product(self, other):
        return self.x * other.x + self.y * other.y




# 2. Implement the previous method with the magic method
# v = Vector(1, 3)
# u = Vector(5, 2)
#  v * u == 11


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __str__(self):
        return f'{self.x}, {self.y}'



# Create a Robot class with the following attributes: orientation, position_x, position_y. The Robot class should have the following methods: 
# move, turn, and display_position. The move method should take a number of steps and move the robot in the direction it is currently facing. 
# The turn method should take a direction (left or right) and turn the robot in that direction. The display_position method should print the 
# current position of the robot.

class Robot:
    def __init__(self, orientation: str, position_x: int, position_y: int):
        try:
            self.position_x = int(position_x)
            self.position_y = int(position_y)
        except ValueError:
            print('That was wrong position value. Please use an int')
            return

        self.validate_orientation(orientation)

        self.orientation = orientation.lower()

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
        self.orientation = orientation

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


if __name__ == '__main__':
    v = Old_vector(1, 3)
    u = Old_vector(5, 2)
    result = v.cross_product(u)
    print(result)

    v = Vector(1, 3)
    u = Vector(5, 2)
    result = v * u
    print(result)

    my_robot = Robot('Up', 2, 3,)
    my_position = my_robot.display_position()
    print(my_position)
    my_robot.turn('down')
    new_position = my_robot.display_position()
    print(new_position)
