import unittest

from Submissions.Tugdual_Sarazin.arm import Arm


class TestArm(unittest.TestCase):
    def test_init_(self):
        arm = Arm(init_x_arm=1, x_goal=2, speed=3)
        self.assertEqual(1, arm.get_x_arm())
        self.assertEqual(2, arm.get_x_goal())
        self.assertEqual(3, arm.get_speed())
        # default parameters
        arm = Arm()
        self.assertEqual(0, arm.get_x_goal())
        self.assertEqual(0, arm.get_x_goal())
        self.assertEqual(0, arm.get_speed())

    def test_distance(self):
        arm1 = Arm(init_x_arm=4, x_goal=8)
        self.assertEqual(4, arm1.distance())

        arm2 = Arm(init_x_arm=10, x_goal=3)
        self.assertEqual(7, arm2.distance())

    # def test_update_speed_increase(self):
    #     # distance > 10 -> speed should increase
    #     arm1 = Arm(init_x_arm=0, x_goal=10.1)
    #     arm1.update_speed()
    #     self.assertEqual(0.1, arm1.get_speed())
    #     arm1.update_speed()
    #     self.assertEqual(0.2, arm1.get_speed())
    #
    #     # Test max speed
    #     arm2 = Arm(init_x_arm=0, x_goal=10.1, speed=2.8)
    #     arm2.update_speed()
    #     self.assertEqual(2.9, arm2.get_speed())
    #     arm2.update_speed()
    #     self.assertEqual(3, arm2.get_speed())
    #     arm2.update_speed()
    #     self.assertEqual(3, arm2.get_speed())

    # def test_update_speed_not_change(self):
    #     # distance ]5, 10] -> -> speed should not change
    #     arm = Arm(init_x_arm=0, x_goal=10, speed=2)
    #     arm.update_speed()
    #     self.assertEqual(2, arm.get_speed())
    #
    #     arm = Arm(init_x_arm=0, x_goal=5.1, speed=2)
    #     arm.update_speed()
    #     self.assertEqual(2, arm.get_speed())

    # def test_update_speed_decrease(self):
    #     # distance ]0, 5] -> speed should decrease
    #     arm = Arm(init_x_arm=0, x_goal=5, speed=1)
    #     arm.update_speed()
    #     self.assertEqual(0.9, arm.get_speed())
    #
    #     arm = Arm(init_x_arm=0, x_goal=0.1, speed=1)
    #     arm.update_speed()
    #     self.assertEqual(0.9, arm.get_speed())

    def test_update_speed_stop(self):
        # distance == 0 -> speed should be 0
        arm = Arm(init_x_arm=10, x_goal=10, speed=100)
        arm.update_speed()
        self.assertEqual(0, arm.get_speed())

    def test_orientation(self):
        arm = Arm(init_x_arm=10, x_goal=0)
        self.assertEqual(-1, arm.orientation())
        arm = Arm(init_x_arm=0, x_goal=10)
        self.assertEqual(1, arm.orientation())

    def test_move_step(self):
        arm = Arm(init_x_arm=10, x_goal=0, speed=0)
        arm.move_step()
        speed1 = arm.get_speed()
        distance1 = arm.distance()

        arm.move_step()
        speed2 = arm.get_speed()
        distance2 = arm.distance()

        self.assertLess(speed1, speed2)
        self.assertGreater(distance1, distance2)

    def test_move(self):
        arm1 = Arm(init_x_arm=10, x_goal=0, speed=0)
        arm1.move()
        self.assertEqual(arm1.get_x_arm(), arm1.get_x_goal())

        arm2 = Arm(init_x_arm=-100, x_goal=0, speed=0)
        arm2.move()
        self.assertEqual(arm2.get_x_arm(), arm2.get_x_goal())

        arm3 = Arm(init_x_arm=0.8, x_goal=0, speed=0)
        arm3.move()
        self.assertEqual(arm3.get_x_arm(), arm3.get_x_goal())


if __name__ == '__main__':
    unittest.main()
