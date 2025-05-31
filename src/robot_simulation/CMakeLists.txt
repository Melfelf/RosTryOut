cmake_minimum_required(VERSION 3.5)
project(robot_simulation)

find_package(ament_cmake REQUIRED)

# Install launch and world files
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
  USE_SOURCE_PERMISSIONS
)

ament_package()