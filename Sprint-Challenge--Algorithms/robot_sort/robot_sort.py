
# %%
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
        # NOTE: The problem constraints seem to indicate using a modified
        # bubble sort as the base algorithm.

        # Bubble sorting loops through n - 1 elements...
        # Or in robot-speak, while possible to move right, do so.

        # NOTE: Robot starts out holding `None`, which when compared to
        # any other item, returns None.
        # However, the `.compare_item()` method returns `None` for both cases:
        # One of `held` *or* `facing` is None. That complicates things a bit.
        # TODO: Work around this behavior
        # If robot's light is "ON", do not swap in the `None` case
        # If robot's light is "OFF", swap the `None`
        if self.light_is_on() is False and self.compare_item() is None:
            # Robot's light is "OFF" and compare is None: `facing` is None
            self.swap_item()
            self.move_right()  # Move on past the None item

        # Keep track of swap using the robot's light
        self.set_light_off()  # starts out each iteration "OFF"

        # Move to the right (i.e. forward iteration)
        while self.can_move_right() is True:
            # First, compare `held` (i) with `facing` (i + 1).
            # NOTE: Rule of thumb: "hold" onto the greater of the two items
            # If held is greater, `held` should go to the right
            if self.compare_item() == 1:
                # Do not swap items -> move right -> repeat
                self.move_right()
            # If `facing` is greater, it should go to the right
            # i.e. `facing` should be picked up and moved with the robot
            elif self.compare_item() == -1:
                # Swap items -> turn robot's light on -> move right -> repeat
                self.swap_item()
                self.set_light_on()  # Turn on to indicate a swap has occurred
                self.move_right()
            elif self.compare_item() == 0:  # Items are equal
                # Do not swap (to save 1 time credit) -> move right -> repeat
                self.swap_item()
                self.move_right()
            # If `facing` is None (ruled out `held` being None above loop)
            elif self.compare_item() is None:
                # Do not swap -> move right -> repeat
                self.move_right()

        # Robot reaches end (right) of list

        # If any swaps occurred during the loop, restart - call method again
        if self.light_is_on() is True:
            # If the light is on when the robot reaches the end of the list,
            # the last action will be a swap?
            # NOTE: infinite loop?
            self.swap_item()

            # This process should start from the very left side of list
            # So better make sure that the robot is all the way left to start!
            # While loop moves it all the way to left
            while self.can_move_left() is True:
                self.move_left()
                # if self.compare_item() == 1:
                #     # Do not swap items -> move left -> repeat
                #     self.move_left()
                # # If `facing` is less, it should go to the right
                # # i.e. `facing` should be picked up and moved with the robot
                # elif self.compare_item() == -1:
                #     # Swap items -> turn robot's light on -> move right -> repeat
                #     self.swap_item()
                #     self.set_light_on()  # Turn on to indicate a swap has occurred
                #     self.move_left()
                # elif self.compare_item() == 0:  # Items are equal
                #     # Do not swap (to save 1 time credit) -> move right -> repeat
                #     self.swap_item()
                #     self.move_left()
                # # If `facing` is None (ruled out `held` being None above loop)
                # elif self.compare_item() is None:
                #     # Do not swap -> move right -> repeat
                #     self.move_left()

            self.sort()

        # Once a loop is completed with no swaps, sorting is complete!
        # NOTE: this method sorts an instance variable; no return is needed.


# %%
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    
    l = [
        15,
        41,
        26,
        4,
        0,
        26,
    ]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


# %%

    # l = [
    #     15,
    #     41,
    #     58,
    #     49,
    #     26,
    #     4,
    #     28,
    #     8,
    #     61,
    #     60,
    #     65,
    #     21,
    #     78,
    #     14,
    #     35,
    #     90,
    #     54,
    #     5,
    #     0,
    #     87,
    #     82,
    #     96,
    #     43,
    #     92,
    #     62,
    #     97,
    #     69,
    #     94,
    #     99,
    #     93,
    #     76,
    #     47,
    #     2,
    #     88,
    #     51,
    #     40,
    #     95,
    #     6,
    #     23,
    #     81,
    #     30,
    #     19,
    #     25,
    #     91,
    #     18,
    #     68,
    #     71,
    #     9,
    #     66,
    #     1,
    #     45,
    #     33,
    #     3,
    #     72,
    #     16,
    #     85,
    #     27,
    #     59,
    #     64,
    #     39,
    #     32,
    #     24,
    #     38,
    #     84,
    #     44,
    #     80,
    #     11,
    #     73,
    #     42,
    #     20,
    #     10,
    #     29,
    #     22,
    #     98,
    #     17,
    #     48,
    #     52,
    #     67,
    #     53,
    #     74,
    #     77,
    #     37,
    #     63,
    #     31,
    #     7,
    #     75,
    #     36,
    #     89,
    #     70,
    #     34,
    #     79,
    #     83,
    #     13,
    #     57,
    #     86,
    #     12,
    #     56,
    #     50,
    #     55,
    #     46,
    # ]

    # robot = SortingRobot(l)

    # robot.sort()
    # print(robot._list)


# %%