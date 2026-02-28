# 🤖 6-DOF Robot Arm Simulation

This project is a comprehensive playground for learning robot simulation using **Gazebo Sim** and **ROS 2**. It features a custom-designed 6-degree-of-freedom (6-DOF) robot arm, initially modeled in Onshape and brought to life in a physics-based simulation environment.

The ultimate goal of this project is to implement **Inverse Kinematics (IK)** for precise control and to train a **Reinforcement Learning (RL) policy** for autonomous pick-and-place tasks.

---

## 📺 Visual Demonstrations

### 1. Onshape CAD Design
The robot arm was meticulously designed in Onshape to ensure mechanical feasibility and proper joint placement.
> **[Video Demonstration of Onshape CAD Model]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556413660-f705f9bb-d58a-4729-8d5a-9d64384a3087.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIyOTU0NzUsIm5iZiI6MTc3MjI5NTE3NSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDEzNjYwLWY3MDVmOWJiLWQ1OGEtNDcyOS04ZDVhLTlkNjQzODRhMzA4Ny5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyOFQxNjEyNTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YWRjODA4MTg1OTM1NjcyZTQzY2E5MDQ4N2IzMjFjMTA2M2U0NGZhODljYTU1ZDdkNTMyYTFlOTQ4Yzc2YWViJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.bokrKMiH12hXE84-y_dvHo6fBtY9a-NubFsgjO8m5ew" width="100%"></video>

### 2. CAD to Simulation (Onshape-to-Robot)
I use `onshape-to-robot` to automatically convert the CAD assembly into a simulation-ready URDF/SDF format, preserving physical properties like mass and inertia.
> **[Video Demonstration of Onshape-to-Robot-Bullet Conversion]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556410811-5ebabe96-dcf4-42d7-b76b-468ca49682c9.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIyOTQ1ODUsIm5iZiI6MTc3MjI5NDI4NSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDEwODExLTVlYmFiZTk2LWRjZjQtNDJkNy1iNzZiLTQ2OGNhNDk2ODJjOS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyOFQxNTU4MDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lYzU5ZGJlMTAyOTI1MDEyNTU4NGE4NDBhZWZkYTQ0NTgxY2M0YWQyYzE3YTQwYWYwNWExYmRhNjU5N2U5N2MyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.D6qbTheGsO4qA52GAH2DOSvdYzqZ7LzaNeipdnHmFuw" width="100%"></video>

### 3. Gazebo Simulation Init
The robot spawned in Gazebo Sim, ready for ROS 2 interaction via the bridge.
> **[Video Demonstration of Gazebo-Init-Sim]**
> <video controls src="https://private-user-images.githubusercontent.com/122405175/556419621-c8822b1d-a196-418c-a97f-e048d70f14ea.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIyOTY1MTUsIm5iZiI6MTc3MjI5NjIxNSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDE5NjIxLWM4ODIyYjFkLWExOTYtNDE4Yy1hOTdmLWUwNDhkNzBmMTRlYS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMjI4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDIyOFQxNjMwMTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iMTI0ZDY0Y2FlNjhhY2M0MjZiNTJkZWZkMGJlZDkxMmU2NzgzYjQzMTllMGU3ZGE2ZmViMzYwZDQ0ZjMyZjYxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.zIhUC0TMV0ajDRT2M_z6eqL9Z9eYHpPN07KiIbHGyHk" width="100%"></video>

Here's a Ros2 controlled dance in Gazebo!
> **[Gazebo-Init-Sim]**

> <video controls src="https://private-user-images.githubusercontent.com/122405175/556453704-3733941a-2649-4600-b89e-c62bf5a39866.webm?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzIzMTIzMDEsIm5iZiI6MTc3MjMxMjAwMSwicGF0aCI6Ii8xMjI0MDUxNzUvNTU2NDUzNzA0LTM3MzM5NDFhLTI2NDktNDYwMC1iODllLWM2MmJmNWEzOTg2Ni53ZWJtP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDIyOCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjAyMjhUMjA1MzIxWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZGVjZTE4M2IzODg0Nzc3ODAyZDk5ZDMwODA0ZTQ4NTAyNDQ0ZmVmMTU2NzQ2YTBiZTE1M2FiOWJmZjg2NGU0OCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.nFezwOoptf914NyOT-rwazWL_ft7F_lh8Y1XjJbaBEY" width="100%"></video>
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

