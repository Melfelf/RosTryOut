#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class VoiceCommandNode(Node):
    def __init__(self):
        super().__init__('voice_command_node')
        self.subscriber = self.create_subscription(String, 'speech_text', self.callback, 10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def callback(self, msg):
        cmd = Twist()
        text = msg.data.lower()
        self.get_logger().info(f"Command: {text}")

        if "forward" in text:
            cmd.linear.x = 0.3
        elif "back" in text:
            cmd.linear.x = -0.3
        elif "left" in text:
            cmd.angular.z = 0.5
        elif "right" in text:
            cmd.angular.z = -0.5
        elif "stop" in text:
            pass
        else:
            self.get_logger().info("Unknown command")
            return

        self.publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = VoiceCommandNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()