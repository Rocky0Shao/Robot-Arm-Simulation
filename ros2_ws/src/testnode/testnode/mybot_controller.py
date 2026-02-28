import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import math

class MyBotController(Node):
    def __init__(self):
        super().__init__('mybot_controller')
        
        # 1. Create publishers for all 6 bridged topics
        self.pub_base = self.create_publisher(Float64, '/model/mybot/joint/base_rot/cmd_pos', 10)
        self.pub_j1 = self.create_publisher(Float64, '/model/mybot/joint/joint1/cmd_pos', 10)
        self.pub_j2 = self.create_publisher(Float64, '/model/mybot/joint/joint2/cmd_pos', 10)
        self.pub_w3 = self.create_publisher(Float64, '/model/mybot/joint/wrist3/cmd_pos', 10)
        self.pub_j4 = self.create_publisher(Float64, '/model/mybot/joint/joint4/cmd_pos', 10)
        self.pub_w5 = self.create_publisher(Float64, '/model/mybot/joint/wrist5/cmd_pos', 10)
        
        # 2. Create a timer to repeatedly send commands (e.g., 20 times a second)
        self.timer = self.create_timer(0.05, self.timer_callback)
        self.time_counter = 0.0

    def timer_callback(self):
        self.time_counter += 0.05
        msg = Float64()
        
        # Base rotation: Sweeps back and forth using a sine wave
        msg.data = math.sin(self.time_counter)
        self.pub_base.publish(msg)
        
        # Joint 1: Static angle (-0.5 radians)
        msg.data = -0.5
        self.pub_j1.publish(msg)
        
        # Joint 2: Static angle (0.5 radians)
        msg.data = 0.5
        self.pub_j2.publish(msg)
        
        # Wrist 3: Static angle (0.0 radians)
        msg.data = 0.0
        self.pub_w3.publish(msg)
        
        # Joint 4: Sweeps using a cosine wave
        msg.data = math.cos(self.time_counter)
        self.pub_j4.publish(msg)
        
        # Wrist 5: Static angle (0.0 radians)
        msg.data = 0.0
        self.pub_w5.publish(msg)
        
        # Log to the terminal so we know it's working
        if int(self.time_counter * 100) % 100 == 0:  # Print every 1 second
            self.get_logger().info(f'Publishing dance commands at t={self.time_counter:.1f}s')

def main(args=None):
    rclpy.init(args=args)
    node = MyBotController()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
