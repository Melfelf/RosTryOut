cmake_minimum_required(VERSION 3.5)
project(voice_command_node)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

install(PROGRAMS
  scripts/voice_control.py
  DESTINATION lib/voice_command_node
)

ament_package()