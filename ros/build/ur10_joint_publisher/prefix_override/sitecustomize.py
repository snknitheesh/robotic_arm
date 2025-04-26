import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zozo/zobot_ws/robotic_arm/ros/install/ur10_joint_publisher'
