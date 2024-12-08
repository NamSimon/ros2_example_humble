import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ExampleTopicSub(Node):
    def __init__(self):
        super().__init__('example_subscriber')
        self.subscription=self.create_subscription(String,'example_topic',self.listener_callback,10)
        self.subscription
        
    def listener_callback(self,msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args)
    rclpy.init(args=args)
    node=ExampleTopicSub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()