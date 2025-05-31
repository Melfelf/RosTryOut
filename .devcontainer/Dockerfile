FROM --platform=linux/arm64 ros:humble

# Install desktop components and development tools
RUN apt-get update && apt-get install -y \
    ros-humble-desktop \
    python3-pip \
    git \
    bash-completion \
    vim \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd --gid 1000 ros && \
    useradd --uid 1000 --gid ros --shell /bin/bash --create-home ros && \
    echo "ros ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd

# Setup ROS environment
RUN echo "source /opt/ros/humble/setup.bash" >> /home/ros/.bashrc && \
    echo "source /usr/share/bash-completion/completions/ros2" >> /home/ros/.bashrc

# Create workspace directory and set permissions
RUN mkdir -p /home/ros/ros2_ws/src && chown -R ros:ros /home/ros/ros2_ws

# Switch to ros user
USER ros
WORKDIR /home/ros/ros2_ws
