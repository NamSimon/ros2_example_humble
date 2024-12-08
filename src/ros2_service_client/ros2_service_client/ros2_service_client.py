import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class ServiceClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for the service to become available...')

    def send_request(self):
        while True:  # 반복적으로 사용자 입력을 받음
            print("\nInput two integers to add (or type 'exit' to quit)")

            try:
                # 사용자 입력 처리
                a_input = input("input a: ")
                if a_input.lower() == 'exit':
                    self.get_logger().info("Exiting...")
                    break

                b_input = input("input b: ")
                if b_input.lower() == 'exit':
                    self.get_logger().info("Exiting...")
                    break

                # 숫자로 변환
                request = AddTwoInts.Request()
                request.a = int(a_input)
                request.b = int(b_input)

                # 요청 보내기
                self.get_logger().info(f'Sending request: {request.a} + {request.b}')
                future = self.client.call_async(request)
                rclpy.spin_until_future_complete(self, future)

                # 응답 처리
                if future.result() is not None:
                    self.get_logger().info(f'Received response: {future.result().sum}')
                else:
                    self.get_logger().error('Service call failed!')
            except ValueError:
                self.get_logger().error("Invalid input. Please enter integers or 'exit'.")

def main(args=None):
    rclpy.init(args=args)

    node = ServiceClient()
    node.send_request()  # 요청 반복 처리
    node.destroy_node()  # 노드 종료
    rclpy.shutdown()

if __name__ == '__main__':
    main()