import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from custom_interfaces.action import CountDown

class CountActionClient(Node):
    def __init__(self):
        super().__init__('countdown_action_client')
        self._action_client = ActionClient(self, CountDown, 'countdown')
        self._goal_done = False  # 작업 완료 여부를 추적하는 변수 추가

    def send_goal(self):
        start_number = int(input('Enter the number to start counting down from: '))

        goal_msg = CountDown.Goal()
        goal_msg.start_number = start_number
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Received feedback: {feedback_msg.feedback.current_number}')

    def result_callback(self, result_future):
        result = result_future.result().result
        if result.success:
            self.get_logger().info('Result: Success')
        else:
            self.get_logger().info('Result: Failure')

        self.get_logger().info('Shutting down the client node...')
        self._goal_done = True  # 작업 완료 상태를 업데이트

def main(args=None):
    rclpy.init(args=args)
    node = CountActionClient()

    # Goal 전송
    node.send_goal()

    # 작업 완료 시 spin 종료
    while rclpy.ok() and not node._goal_done:
        rclpy.spin_once(node)

    # 클라이언트 노드 종료
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()