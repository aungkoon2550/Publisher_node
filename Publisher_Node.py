#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


def main(args=None):
    rclpy.init(args=args)
    node = Node("Node_Name")
    rclpy.spin(node)
    rclpy.shutdonw()

if __name__ == "__main__":
    main()