from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Pfad zur sim_launch.py
    robot_sim_launch = os.path.join(
        os.getenv('COLCON_PREFIX_PATH', ''),  # Fallback leer
        'robot_simulation', 'share', 'robot_simulation', 'launch', 'sim_launch.py'
    )

    return LaunchDescription([
        # Gazebo-Simulation starten
        ExecuteProcess(
            cmd=['ros2', 'launch', 'robot_simulation', 'sim_launch.py'],
            output='screen',
        ),

        # Whisper Speech-to-Text Node
        Node(
            package='speech_to_text',
            executable='whisper_node.py',
            output='screen'
        ),

        # Voice Command Node
        Node(
            package='voice_command_node',
            executable='voice_control.py',
            output='screen'
        ),
    ])