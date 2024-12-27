import rclpy
import matplotlib.pyplot as plt
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class BouncingTurtle(Node):
    def __init__(self):
        super().__init__('bouncing_turtle')
        self.subscriber = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10) # Receive the current pose
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) # Control the turtle's movement
        self.timer = self.create_timer(0.1, self.timer_callback)# Call a callback function at regular intervals that updates the turtle's velocity.
        self.velocity = Twist()
        self.turtle_position = []
        
        self.direction_x = 1  
        self.direction_y = 1
        self.direction_z = -0.2

    def pose_callback(self, msg):
        self.turtle_position.append((msg.x, msg.y))

        # Reverse directions upon reaching a wall
        if msg.x > 10.0 or msg.x < 1.0:
            self.direction_x *= -1
            self.direction_z *= -1
        if msg.y < 1.0 or msg.y > 10.0:
            self.direction_y *= -1
            self.direction_z *= -1

    def timer_callback(self):
        self.velocity.linear.x = 3.0 * self.direction_x
        self.velocity.linear.y = 0.1 * self.direction_y
        self.velocity.angular.z = -0.1 *self.direction_z
        self.publisher.publish(self.velocity)

    def spin(self):
        rclpy.spin(self)

    def get_trajectory(self):
        return self.turtle_position

def main(args=None):
    rclpy.init(args=args)
    bouncing_turtle = BouncingTurtle()
    
    try:
        rclpy.spin(bouncing_turtle)
    except KeyboardInterrupt:
        pass

    turtle_trajectory = bouncing_turtle.get_trajectory()
    bouncing_turtle.destroy_node()
    rclpy.shutdown()

    # Visualize the trajectory after destroying the node
    x, y = zip(*turtle_trajectory)
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('TurtleSim Trajectory')
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()