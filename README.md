# 🤖 6-DOF Robot Arm Simulation

This project is a comprehensive playground for learning robot simulation using **Gazebo Sim** and **ROS 2**. It features a custom-designed 6-degree-of-freedom (6-DOF) robot arm, initially modeled in Onshape and brought to life in a physics-based simulation environment.

The ultimate goal of this project is to implement **Inverse Kinematics (IK)** for precise control and to train a **Reinforcement Learning (RL) policy** for autonomous pick-and-place tasks.

---

## ✨ Key Features
- **6-DOF Custom Arm**: Meticulously designed for robot simulation experiments.
- **Onshape Integration**: Seamless CAD-to-Simulation workflow using `onshape-to-robot`.
- **Physics-Based Simulation**: High-fidelity simulation in Gazebo Sim (Harmonic/Ionic).
- **ROS 2 Powered**: Full control and telemetry via ROS 2 Humble/Jazzy.
- **IK Solver**: Real-time inverse kinematics for task-space target tracking.

---

## 📺 Visual Demonstrations

### 1. Onshape CAD Design
The robot arm was meticulously designed in Onshape to ensure mechanical feasibility and proper joint placement.
> **[Onshape CAD Model]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556413660-f705f9bb-d58a-4729-8d5a-9d64384a3087.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIyOTU0NzUsIm5iZiI6MTc3MjI5NTE3NSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDEzNjYwLWY3MDVmOWJiLWQ1OGEtNDcyOS04ZDVhLTlkNjQzODRhMzA4Ny5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyOFQxNjEyNTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YWRjODA4MTg1OTM1NjcyZTQzY2E5MDQ4N2IzMjFjMTA2M2U0NGZhODljYTU1ZDdkNTMyYTFlOTQ4Yzc2YWViJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.bokrKMiH12hXE84-y_dvHo6fBtY9a-NubFsgjO8m5ew" width="100%"></video>

### 2. CAD to Simulation (Onshape-to-Robot)
I use `onshape-to-robot` to automatically convert the CAD assembly into a simulation-ready URDF/SDF format, preserving physical properties like mass and inertia.
> **[Onshape-to-Robot Conversion]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556410811-5ebabe96-dcf4-42d7-b76b-468ca49682c9.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIyOTQ1ODUsIm5iZiI6MTc3MjI5NDI4NSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDEwODExLTVlYmFiZTk2LWRjZjQtNDJkNy1iNzZiLTQ2OGNhNDk2ODJjOS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyOFQxNTU4MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lYzU5ZGJlMTAyOTI1MDEyNTU4NGE4NDBhZWZkYTQ0NTgxY2M0YWQyYzE3YTQwYWYwNWExYmRhNjU5N2U5N2MyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.D6qbTheGsO4qA52GAH2DOSvdYzqZ7LzaNeipdnHmFuw" width="100%"></video>

### 3. Gazebo Simulation & ROS 2 Control
The robot is spawned in Gazebo Sim, controlled via a ROS 2 joint controller. Here's a "dance" script demonstrating the multi-joint synchronization.
> **[Gazebo Robot Dance]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556453704-3733941a-2649-4600-b89e-c62bf5a39866.webm?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIzMTIzMDEsIm5iZiI6MTc3MjMxMjAwMSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDUzNzA0LTM3MzM5NDFhLTI2NDktNDYwMC1iODllLWM2MmJmNWEzOTg2Ni53ZWJtP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDIyOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAyMjhUMjA1MzIxWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZGVjZTE4M2IzODg0Nzc3ODAyZDk5ZDMwODA0ZTQ4NTAyNDQ0ZmVmMTU2NzQ2YTBiZTE1M2FiOWJmZjg2NGU0OCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.nFezwOoptf914NyOT-rwazWL_ft7F_lh8Y1XjJbaBEY" width="100%"></video>

### 4. Inverse Kinematics Visualization
An IK solver is implemented to enable task-space control. The robot arm tracks a target sphere in Gazebo, which is controlled in real-time.
> **[Inverse Kinematics Tracking]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556460301-d8451d3d-691a-4b4c-997c-a6c5de6ce6a4.webm?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIzMTQwNjIsIm5iZiI6MTc3MjMxMzc2MiwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDYwMzAxLWQ4NDUxZDNkLTY5MWEtNGI0Yy05OTdjLWE2YzVkZTZjZTZhNC53ZWJtP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDIyOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAyMjhUMjEyMjQyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NWQyYzBiNzFlMWZhN2I0MDM4NmMzMThlNGFmN2VhYzA5ZjYzY2MzNGM0YWFlZjBjNzRjYWExODU2N2M4MzVmZSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.6XOPCTHiyxjI-3mP8-_5zP_y-SKU3POGfNtvjMJEI8g" width="100%"></video>

---

## 🛠 Project Architecture

The workflow of this project follows these core steps:
1.  **CAD Modeling**: Design in Onshape.
2.  **Conversion**: Transform CAD to SDF/URDF using `onshape-to-robot`.
3.  **Simulation**: Load the model into **Gazebo Sim**.
4.  **Control**: Interface with the simulation using **ROS 2**.
5.  **Intelligence**: Implementation of Inverse Kinematics and (Planned) Reinforcement Learning.

---

## 🚀 Getting Started

### Prerequisites
*   **ROS 2** (Humble, Iron, or Jazzy)
*   **Gazebo Sim** (Ionic or Harmonic)
*   `ros_gz_bridge` for communication between ROS and Gazebo.
*   `ikpy` for Inverse Kinematics.

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
    Starts Gazebo, spawns the robot, and initializes the parameter bridge.
    ```bash
    ros2 launch mybot_control sim.launch.py
    ```

2.  **Run the Joint Controller (Dance Script)**:
    ```bash
    ros2 run testnode mybot_controller
    ```

3.  **Run the IK Tracker**:
    ```bash
    ros2 run ik_test ik_test
    ```

---

## 🎯 Current Goals & Progress

- [x] **6-DOF Arm Design** in Onshape.
- [x] **Automated Conversion** to SDF/URDF.
- [x] **Gazebo Integration** with ROS 2 Bridge.
- [x] **Inverse Kinematics (IK)** implementation for task-space control.
- [ ] **RL Policy Training** for pick-and-place using stable-baselines3 or similar.

---

