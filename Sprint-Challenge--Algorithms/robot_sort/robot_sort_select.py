"""
Algorithms :: Sprint Challenge - robot sort
"""


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l  # The list the robot is tasked with sorting
        self._item = None  # The item the robot is holding
        self._position = 0  # The list position the robot is at
        self._light = "OFF"  # The state of the robot's light
        self._time = 0  # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Repeated steps
        # TODO: find way to get to last item without infinite looping
        while self.can_move_right() is True:  # Never reaches last item
            # 1. Use next item in sequence as "current"
            # AKA: Swap -> move right -> compare
            if self.compare_item() is None:
                self.swap_item()
                self.move_right()

            # 2. Find smallest item to the right of current item
            # list item is greater than or equal to list item
            if self.compare_item() == -1 or self.compare_item() == 0:
                self.move_right()

            # list item is less than held item
            if self.compare_item() == 1:
                self.swap_item()
                self.move_right()

        # 3. Swap current with next smallest item
        # (i.e. Replace None with current lowest)
        while self.compare_item() is not None:
            self.move_left()

        self.swap_item()  # Now holding None again

        # If last item, robot can't move right; done sorting
        self.move_right()
        if self.can_move_right() is True:
            # Position should persist into successive recursive call
            self.sort()
        # else: good robot is done sorting!
        # self.swap_item()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [
        15,
        41,
        58,
        49,
        26,
    ]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)