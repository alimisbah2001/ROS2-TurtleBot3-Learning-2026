import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class SquareRobot(Node):

    def __init__(self):
        super().__init__('square_robot')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        start_time = time.time()

        while rclpy.ok():

            msg = Twist()

            elapsed = time.time() - start_time

            if elapsed < 5:
                msg.linear.x = 0.2

            elif elapsed < 7:
                msg.angular.z = 0.5

            elif elapsed < 12:
                msg.linear.x = 0.2

            elif elapsed < 14:
                msg.angular.z = 0.5

            elif elapsed < 19:
                msg.linear.x = 0.2

            elif elapsed < 21:
                msg.angular.z = 0.5

            elif elapsed < 26:
                msg.linear.x = 0.2

            elif elapsed < 28:
                msg.angular.z = 0.5

            else:
                break

            self.publisher.publish(msg)
            time.sleep(0.1)

def main():
    rclpy.init()
    node = SquareRobot()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
