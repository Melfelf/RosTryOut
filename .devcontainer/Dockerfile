FROM osrf/ros:humble-desktop

# Install required packages for ROS 2 development and simulation
RUN apt-get update && \
    apt-get install -y \
        python3-colcon-common-extensions \
        ros-humble-gazebo-ros-pkgs \
        ros-humble-xacro \
        ros-humble-joint-state-publisher-gui \
        ros-humble-rviz2 \
        ros-humble-ros2-control \
        ros-humble-ros2-controllers \
        build-essential \
        git \
        curl \
        lsb-release \
        sudo \
        && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd --gid 1000 ros && \
    useradd --uid 1000 --gid ros --shell /bin/bash --create-home ros && \
    echo "ros ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd

# Switch to ros user
USER ros
WORKDIR /home/ros/ros2_ws
