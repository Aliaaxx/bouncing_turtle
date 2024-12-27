# Turtle Bouncing Motion Simulation

This project simulates a TurtleSim robot that moves within the boundaries of a simulation window, bouncing off the walls and continuously changing direction. The robot's trajectory is recorded and visualized after the simulation ends using the Matplotlib library.

## Description

The TurtleSim moves until it hits a wall, at which point it exhibits a bouncing behavior. When the robot reaches the boundaries of the window, it slightly shifts up and continues moving in the opposite direction. This motion repeats continuously within the boundaries of the simulation window until the user interrupts the program.

### Demo

Watch the demo video showcasing the simulation:

[View Demo](https://drive.google.com/file/d/1kQPFOdu86epOyQBQUQaNGtvOgdsBRvfC/view?usp=sharing)

### Figures
![Task 2 documentation_page-0001](https://github.com/user-attachments/assets/bfdfd51a-73f8-4a49-8ad9-e6153a574426)


## Code Overview

This simulation is created using ROS2 with Python and the `rclpy` library. The code defines a single ROS2 node, `BouncingTurtle`, which:

- Subscribes to the `/turtle1/pose` topic to receive the current pose of the TurtleSim.
- Publishes to the `/turtle1/cmd_vel` topic to control its velocity.

### Key Components

1. **Initialization:**
   - Subscriptions and publishers are set up for controlling the robot's motion.
   - Initial velocities and direction variables are defined.

2. **Pose Callback:**
   - The `pose_callback` function is triggered upon receiving pose messages.
   - The robot's position `(x, y)` is recorded in the `turtle_pose` list.
   - Directional changes are applied when the robot hits the window boundaries, creating a bouncing effect.

3. **Velocity Updates and Publishing:**
   - The `update_velocity` and `publish_velocity` methods manage and publish the velocity based on the robot's current direction.

4. **Main Loop:**
   - The `rclpy.spin(bouncing_turtle)` function keeps the node running until manually interrupted by the user.

5. **Trajectory Visualization:**
   - After the program is interrupted, the `turtle_pose` list is visualized using Matplotlib to plot the turtle's path.

## Requirements

- ROS2 (e.g., Foxy or later)
- Python 3
- rclpy library
- Matplotlib library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aliaaxx/turtle-bouncing-motion.git
   cd turtle-bouncing-motion
