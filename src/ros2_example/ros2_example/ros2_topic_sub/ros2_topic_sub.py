import rclpy
from rclpy.node import Node
from std_msgs.msg import String
#라이브러리 임포트


class ExampleTopicSub(Node):
    def __init__(self):
        super().__init__('example_subscriber')# 노드 초기화(노드 이름 :example_subscriber )
        self.subscription=self.create_subscription(String,'example_topic',self.listener_callback,10)
        #example_topic라는 토픽을 subscribe 생성
        #큐사이즈 10으로 설정(10개 데이터 모이면 수신)
          
    def listener_callback(self,msg):
        # 콜백함수 토픽에서 메세지를 수신 되면 호출
        self.get_logger().info('I heard: "%s"' % msg.data)# ROS2에서 로그를 출력하는 함수

def main(args):
    rclpy.init(args=args)#ROS2 초기화
    node=ExampleTopicSub()# subscribe 노드 생성
    rclpy.spin(node)# 실행 반복
    node.destroy_node()# 노드 종료시 노드 파괴
    rclpy.shutdown()# ROS2 종료


if __name__=='__main__':
    main()