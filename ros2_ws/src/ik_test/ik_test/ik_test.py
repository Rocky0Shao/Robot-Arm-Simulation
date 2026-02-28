import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from geometry_msgs.msg import PoseStamped # To read the dummy target's pose
import ikpy.chain
import numpy as np

class MyBotIKController(Node):
    def __init__(self):
        super().__init__('mybot_ik_controller')
        
        # 1. Load the robot's kinematics chain from your URDF file
        # Make sure you have a URDF file that defines your 6 joints!
        self.robot_chain = ikpy.chain.Chain.from_urdf_file(
            "/home/rocky/my-robot/ros2_ws/src/ik_test/ik_test/robot.urdf",
        )
        
        # 2. Create publishers (same as you had before)
        self.pub_base = self.create_publisher(Float64, '/model/mybot/joint/base_rot/cmd_pos', 10)
        self.pub_j1 = self.create_publisher(Float64, '/model/mybot/joint/joint1/cmd_pos', 10)
        self.pub_j2 = self.create_publisher(Float64, '/model/mybot/joint/joint2/cmd_pos', 10)
        self.pub_w3 = self.create_publisher(Float64, '/model/mybot/joint/wrist3/cmd_pos', 10)
        self.pub_j4 = self.create_publisher(Float64, '/model/mybot/joint/joint4/cmd_pos', 10)
        self.pub_w5 = self.create_publisher(Float64, '/model/mybot/joint/wrist5/cmd_pos', 10)

        # 3. Create a Subscriber to listen to the target sphere's pose from Gazebo
        # You will need to bridge the pose of the target object to this ROS topic
        self.target_sub = self.create_subscription(
            PoseStamped, 
            '/model/target_sphere/pose',
            self.pose_callback, 
            10
        )
        
        # Keep track of the current joint positions to feed as a starting guess to the IK solver
        self.current_joints = [0.0] * len(self.robot_chain.links)

    def pose_callback(self, msg):
        # 1. Extract the X, Y, Z position from the incoming Gazebo message
        target_position = [
            msg.pose.position.x,
            msg.pose.position.y,
            msg.pose.position.z
        ]
        
        # 2. Calculate Inverse Kinematics
        # target_orientation can also be added, but let's stick to position for now
        ik_solution = self.robot_chain.inverse_kinematics(
            target_position=target_position,
            initial_position=self.current_joints
        )
        
        # Update our current joints for the next calculation
        self.current_joints = ik_solution
        
        # 3. Publish the calculated angles to Gazebo
        # Note: IKPy returns an array including the base link (index 0). 
        # Your actual movable joints usually start at index 1 depending on your URDF.
        self.publish_joints(ik_solution)

    def publish_joints(self, joints):
        # Ensure the indices match how your URDF is structured in IKPy
        # Usually: joints[1] is base_rot, joints[2] is j1, etc.
        
        msg = Float64()
        
        msg.data = joints[1]
        self.pub_base.publish(msg)
        
        msg.data = joints[2]
        self.pub_j1.publish(msg)
        
        msg.data = joints[3]
        self.pub_j2.publish(msg)
        
        msg.data = joints[4]
        self.pub_w3.publish(msg)
        
        msg.data = joints[5]
        self.pub_j4.publish(msg)
        
        msg.data = joints[6]
        self.pub_w5.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MyBotIKController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()