#!/bin/bash

# Clean up background processes when the script exits or is interrupted (Ctrl+C)
trap 'echo "Shutting down processes..."; kill $(jobs -p); exit' SIGINT SIGTERM EXIT

echo "Starting Gazebo simulator..."
gz sim -r robot.sdf &

# Wait a few seconds to let Gazebo initialize before starting the bridge
sleep 5 

echo "Starting ROS 2 - Gazebo bridge..."
ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=mybot_bridge.yaml &



# Wait a couple of seconds to ensure the bridge is up before the controller starts
sleep 2 

echo "Starting Python controller..."
cd ros2_ws
source install/setup.bash
# ros2 run testnode testnode &
ros2 run ik_test ik_controller &

# Wait for all background processes to finish (keeps the script running)
wait