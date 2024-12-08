import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ExampleTopicPub(Node):
    def __init__(self):
        super().__init__('example_publisher')
        self.publisher=self.create_publisher(String,'example_topic',10)
        self.timer=self.create_timer(0.5,self.timer_callback)
        
    def timer_callback(self):
        msg=String()
        msg.data= 'Hello World'
        self.publisher.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        
def main(args=None):
    rclpy.init(args=args)
    node=ExampleTopicPub()
    rclpy.spin(node)
    node.destory_node()
    rclpy.shutdown()
    
if __name__=='__main__':
    main()
    
    