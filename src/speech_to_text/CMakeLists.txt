cmake_minimum_required(VERSION 3.5)
project(speech_to_text)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(PROGRAMS
  scripts/whisper_node.py
  DESTINATION lib/speech_to_text
)

ament_package()