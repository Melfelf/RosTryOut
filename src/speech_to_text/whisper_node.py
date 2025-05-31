from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-entity', 'mobile_robot',
                '-file', '/workspaces/RosTryOut/src/robot_description/urdf/mobile_robot.urdf.xacro',
                '-x', '0', '-y', '0', '-z', '0.1'
            ],
            output='screen'
        ),
    ])