import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class UR10JointCommandSender(Node):
    def __init__(self):
        super().__init__('ur10_joint_command_sender')

        # Publisher for joint commands
        self.joint_command_pub = self.create_publisher(JointState, '/joint_command', 10)

        # Define the list of joint positions to send
        self.joint_positions_list = [
            [0.5, -1.0, 1.5, -0.5, 0.3],
            [0.6, -0.8, 1.2, -0.3, 0.2],
            [0.4, -1.2, 1.7, -0.6, 0.5],
            [0.3, -0.9, 1.4, -0.2, 0.1],
            [0.7, -1.1, 1.6, -0.4, 0.4]
        ]

        self.current_index = 0  # To track which position to send next

        # Create timer to send a command every 3 seconds
        self.timer = self.create_timer(3.0, self.send_joint_command)

    def send_joint_command(self):
        if self.current_index >= len(self.joint_positions_list):
            self.get_logger().info('All joint commands sent. Stopping timer.')
            self.timer.cancel()
            return

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = [
            'joint1',
            'joint2',
            'joint3',
            'joint4',
            'joint5'
        ]
        msg.position = self.joint_positions_list[self.current_index]

        self.joint_command_pub.publish(msg)
        self.get_logger().info(f'Sent joint command {self.current_index + 1}: {msg.position}')

        self.current_index += 1  # Move to next position for the next timer call

def main(args=None):
    rclpy.init(args=args)
    node = UR10JointCommandSender()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
