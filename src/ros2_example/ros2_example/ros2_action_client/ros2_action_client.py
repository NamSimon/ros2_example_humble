import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from custom_interfaces.action import CountDown

class CountActionClient(Node):
    def __init__(self):
        super().__init__('countdown_action_client')#노드 초기화(노드 이름 : countdown_action_client)
        self._action_client = ActionClient(self, CountDown, 'countdown') 
        #countdown이라는 ActionClient 생성 
        self._goal_done = False  # 작업 완료 여부를 추적하는 변수 추가

    def send_goal(self):
        start_number = int(input('Enter the number to start counting down from: '))

        goal_msg = CountDown.Goal()#Count Action 인터페이스 객체 생성
        goal_msg.start_number = start_number # 목표값 설정
        self._action_client.wait_for_server()# 액션서버 준비될때까지 대기
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, self.feedback_callback)
        #비동기적으로 목표 전송하고 피드백을 콜백 함수 호출
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        #목표가 action server에 승인되면 결과 요청 콜백

    def goal_response_callback(self, future):
        #목표가 서버에 전송 되었을때 호출되는 콕백 한수
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected')
            return
        self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        #목표 수락시 get_result_async호출 하여  실행후 결과 요청
        self._get_result_future.add_done_callback(self.result_callback)
        # 결과 처리하는 콜백함수 설정
        
    def feedback_callback(self, feedback_msg):
        #서버 실행중 피드백 보낼때 호출되는 콜백
        self.get_logger().info(f'Received feedback: {feedback_msg.feedback.current_number}')

    def result_callback(self, result_future):
        #goal이 도달하면 서버가 반환하는 겨로가를 처리하느 콜백
        result = result_future.result().result
        if result.success:
            self.get_logger().info('Result: Success')
        else:
            self.get_logger().info('Result: Failure')

        self.get_logger().info('Shutting down the client node...')
        self._goal_done = True  # 작업 완료 상태를 업데이트

def main(args=None):
    rclpy.init(args=args)# ROS2 초기화
    node = CountActionClient()# 노드 생성

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