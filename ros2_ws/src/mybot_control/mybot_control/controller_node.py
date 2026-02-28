import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math
import time

class MyBotController(Node):
    """
    A simple ROS 2 node that controls the joints of the robot by 
    publishing target positions to the bridged Gazebo topics.
    """
    def __init__(self):
        super().__init__('mybot_controller')
        self.joints = ['base_rot', 'joint1', 'joint2', 'wrist3', 'joint4', 'wrist5']
        self.publishers_ = {}
        
        # Create a publisher for each joint command topic
        for joint in self.joints:
            topic = f'/model/mybot/joint/{joint}/0/cmd_pos'
            self.publishers_[joint] = self.create_publisher(Float64, topic, 10)
            self.get_logger().info(f'Created publisher for: {topic}')
        
        # Timer to publish commands at 10Hz
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = time.time()
        self.get_logger().info('MyBot Controller Node started.')

    def timer_callback(self):
        elapsed = time.time() - self.start_time
        
        # Loop through all joints and send a sinusoidal position command
        for i, joint in enumerate(self.joints):
            msg = Float64()
            # Generate a target position between -1.0 and 1.0 radians
            # Different phase for each joint to see them move independently
            msg.data = 1.0 * math.sin(elapsed + i * 0.8)
            
            self.publishers_[joint].publish(msg)

def main(args=None):
    rclpy.init(args=args)
    controller = MyBotController()
    try:
        rclpy.spin(controller)
    except KeyboardInterrupt:
        pass
    finally:
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
