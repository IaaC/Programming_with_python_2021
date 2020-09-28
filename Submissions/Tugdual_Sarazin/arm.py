class Arm:
    _x_arm: float = None
    _x_goal: float = None
    _speed: float = None

    def __init__(self, init_x_arm=0, x_goal=0, speed=0):
        self._x_arm = init_x_arm
        self._x_goal = x_goal
        self._speed = speed

    def get_x_arm(self) -> float:
        return self._x_arm

    def get_x_goal(self) -> float:
        return self._x_goal

    def get_speed(self) -> float:
        return self._speed

    def distance(self) -> float:
        """
        Return absolute distance between x_arm and x_goal
        :rtype: float
        """
        return abs(self._x_goal - self._x_arm)

    def update_speed(self):
        """
        Update the speed of the arm.
        - If distance is bigger than 10 cm and speed less than 3 then move faster
        - If distance is bigger than 5 cm then move at the same speed
        - If distance is between the desired distance and 5cm then reduce the speed
        - if distance is less than the desired one then stop
        """
        # TODO: increase/decrease exponentially
        distance = self.distance()
        if distance > 5 and self._speed < 3:
            self._speed += 0.1
        elif 5 >= distance > 0.1:
            if distance < 3:
                self._speed = distance / 2
            else:
                self._speed -= 0.1
        elif distance > 0.1:
            self._speed = distance
        elif distance == 0:
            self._speed = 0

        #self._speed = round(self._speed, 2)

    def orientation(self) -> int:
        """
        Orientation between x_arm and x_pos. return 1 if positive else return -1
        """
        if self._x_goal - self._x_arm > 0:
            return 1
        else:
            return -1

    def move_step(self):
        """
        Update the speed and move by processing the new x_arm
        """
        self.update_speed()
        self._x_arm += self._speed * self.orientation()

    def move(self):
        """
        Move the arm until the x_arm is the same as x_goal
        """
        while self._x_arm != self._x_goal:
            self.move_step()
            #print(self)

    def __str__(self):
        return f"Arm(x_arm={self._x_arm}, x_target={self._x_goal}, speed={self._speed})"
