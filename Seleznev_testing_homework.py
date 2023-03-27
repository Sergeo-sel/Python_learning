from unittest.mock import Mock
from Seleznov_class_homework import Robot
import unittest

class TestStringMethods(unittest.TestCase):
    def test_turn_function(self):
        my_robot = Robot('Up', 2, 3,)
        my_robot.turn('down')
        self.assertEqual(my_robot.orientation, 'down')

    def test_failed_turn_function(self):
        my_robot = Robot('Up', 2, 3,)
        my_robot.turn('down')
        self.assertEqual(my_robot.orientation, 'up')

if __name__ == '__main__':
    unittest.main()
