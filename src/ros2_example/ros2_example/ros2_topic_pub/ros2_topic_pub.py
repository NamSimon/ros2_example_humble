import rclpy
from rclpy.node import Node
from std_msgs.msg import String
#라이브러리 임포트

class ExampleTopicPub(Node):
    def __init__(self):
        super().__init__('example_publisher')#노드 초기화(노드이름 : example_publisher)
        self.publisher=self.create_publisher(String,'example_topic',10)
        #example_ topic이라는 토픽을 publish 생성
        #큐사이즈 10
        self.timer=self.create_timer(0.5,self.timer_callback)
        #0.5초 마다 timer_callback 함수 호출
        
    def timer_callback(self):
        #timer callback 함수
        msg=String()# Topic 인터페이스 객체 생성
        msg.data= 'Hello World'# 메세지 데이터설정 
        self.publisher.publish(msg)# 메세지 발행 
        self.get_logger().info('Publishing: "%s"' % msg.data)
        #발행된 메세지 출력
        
def main(args=None):
    rclpy.init(args=args)# ROS2 초기화
    node=ExampleTopicPub()# Publish 노드 생성
    rclpy.spin(node)# 실행 상태 반복
    node.destory_node()# 노드 종료시 노드 파괴
    rclpy.shutdown()# ROS2 종료
    
if __name__=='__main__':
    main()
    
    