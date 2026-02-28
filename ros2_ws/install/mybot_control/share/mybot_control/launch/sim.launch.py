import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_mybot_control = get_package_share_directory('mybot_control')
    
    # Set Gazebo resource path to find meshes in /home/rocky/my-robot/mybot/assets
    # The SDF uses model://mybot/assets/...
    resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value='/home/rocky/my-robot'
    )

    # Gazebo Sim
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py'
        )]),
        launch_arguments={'gz_args': '-r empty.sdf'}.items(),
    )

    # Spawn robot
    sdf_path = '/home/rocky/my-robot/ros2_ws/sdf&urdf/robot.sdf'
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'mybot',
            '-file', sdf_path,
            '-x', '0', '-y', '0', '-z', '0.1'
        ],
        output='screen',
    )

    # Bridge between ROS 2 and Gazebo
    joints = ['base_rot', 'joint1', 'joint2', 'wrist3', 'joint4', 'wrist5']
    bridge_args = []
    for joint in joints:
        # Bridge for commands: ROS -> Gazebo (Double)
        bridge_args.append(f'/model/mybot/joint/{joint}/0/cmd_pos@std_msgs/msg/Float64]gz.msgs.Double')
    
    # Bridge for joint states: Gazebo -> ROS (Model contains JointState)
    bridge_args.append('/model/mybot/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model')

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=bridge_args,
        output='screen'
    )

    return LaunchDescription([
        resource_path,
        gz_sim,
        spawn_robot,
        bridge,
    ])
