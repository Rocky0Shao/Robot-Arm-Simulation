# 🤖 6-DOF Robot Arm Simulation

This project is a comprehensive playground for learning robot simulation using **Gazebo Sim** and **ROS 2**. It features a custom-designed 6-degree-of-freedom (6-DOF) robot arm, initially modeled in Onshape and brought to life in a physics-based simulation environment.

The ultimate goal of this project is to implement **Inverse Kinematics (IK)** for precise control and to train a **Reinforcement Learning (RL) policy** for autonomous pick-and-place tasks.

---

## 📺 Visual Demonstrations

### 1. Onshape CAD Design
The robot arm was meticulously designed in Onshape to ensure mechanical feasibility and proper joint placement.
> **[PLACEHOLDER: Video Demonstration of Onshape CAD Model]**
> *Insert video link here*

### 2. CAD to Simulation (Onshape-to-Robot)
I use `onshape-to-robot` to automatically convert the CAD assembly into a simulation-ready URDF/SDF format, preserving physical properties like mass and inertia.
> **[PLACEHOLDER: Video Demonstration of Onshape-to-Robot-Bullet Conversion]**
> *Insert video link here*

### 3. Gazebo Simulation Init
The robot spawned in Gazebo Sim, ready for ROS 2 interaction via the bridge.
> **[PLACEHOLDER: Video Demonstration of Gazebo-Init-Sim]**
> *Insert video link here*

---

## 🛠 Project Architecture

The workflow of this project follows these core steps:
1.  **CAD Modeling**: Design in Onshape.
2.  **Conversion**: Transform CAD to SDF/URDF using `onshape-to-robot`.
3.  **Simulation**: Load the model into **Gazebo Sim**.
4.  **Control**: Interface with the simulation using **ROS 2** (Humble/Jazzy).
5.  **Intelligence**: (In Progress) Implementation of IK and RL training.

---

## 🚀 Getting Started

### Prerequisites
*   **ROS 2** (Humble or later recommended)
*   **Gazebo Sim** (Ionic or Harmonic)
*   `ros_gz_bridge` for communication between ROS and Gazebo.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd my-robot
    ```

2.  **Build the ROS 2 workspace**:
    ```bash
    cd ros2_ws
    colcon build
    source install/setup.bash
    ```

### Running the Simulation

1.  **Launch Gazebo and Spawn Robot**:
    Using the provided launch file to start Gazebo, spawn the robot, and initialize the parameter bridge.
    ```bash
    ros2 launch mybot_control sim.launch.py
    ```

2.  **Run the Joint Controller**:
    Run the example controller to see the robot move (the "dance" script).
    ```bash
    python3 mybot_controller.py
    ```

---

## 🎯 Current Goals & Progress

- [x] **6-DOF Arm Design** in Onshape.
- [x] **Automated Conversion** to SDF/URDF.
- [x] **Gazebo Integration** with ROS 2 Bridge.
- [ ] **Inverse Kinematics (IK)** implementation for task-space control.
- [ ] **RL Policy Training** for pick-and-place using stable-baselines3 or similar.

---

