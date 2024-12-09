import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from custom_interfaces.action import CountDown  # 정의한 Action 메시지

class CountActionServer(Node):
    def __init__(self):
        super().__init__('countdown_action_server')
        self._action_server = ActionServer(
            self,
            CountDown,
            'countdown',
            self.execute_callback  # Goal을 처리하는 콜백 함수
        )
        
    def execute_callback(self, goal_handle):
        self.get_logger().info(f"Received goal: Start counting down from {goal_handle.request.start_number}")
        
        feedback_msg = CountDown.Feedback()
        feedback_msg.current_number = goal_handle.request.start_number  # 초기화
        
        while feedback_msg.current_number >= 0:
            goal_handle.publish_feedback(feedback_msg)  # 피드백 전송
            self.get_logger().info(f'Counting down: {feedback_msg.current_number}')
            feedback_msg.current_number -= 1
            time.sleep(1)  # 1초 대기
        
        goal_handle.succeed()  # 작업 완료
        result = CountDown.Result()
        result.success = True
        self.get_logger().info("Countdown complete, sending result.")
        return result

def main(args=None):
    rclpy.init(args=args)  # ROS 2 초기화
    node = CountActionServer()  # 서버 노드 생성
    try:
        rclpy.spin(node)  # 노드 실행
    except KeyboardInterrupt:
        node.get_logger().info('Server shutting down.')  # 종료 로그
    finally:
        node.destroy_node()  # 노드 파괴
        rclpy.shutdown()  # ROS 2 종료

if __name__ == '__main__':
    main()