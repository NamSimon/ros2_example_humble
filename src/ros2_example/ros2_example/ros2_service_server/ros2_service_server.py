import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class ServiceServer(Node):
    def __init__(self):
        super().__init__('service_server')# service_server노드 초기화
        self.service = self.create_service(AddTwoInts, 'add_two_ints', self.callback)
        #service server 생성
        #client로 부터 2개의 int형을 받으면 콜백함수 호출
    
    def callback(self, request, response):
        # 콜백함수
        response.sum = request.a * request.b
        self.get_logger().info(f'Received request: {request.a} * {request.b} = {response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)#ROS2 초기화
    node = ServiceServer()#Server 노드 생성
    rclpy.spin(node)#실행 반복
    node.destroy_node()# 노드 종료시 노드 파괴
    rclpy.shutdown()#ROS2 종료

if __name__ == '__main__':
    main()