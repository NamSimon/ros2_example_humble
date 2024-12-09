import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # ros2_action_server 노드 실행
        Node(
            package='ros2_example',
            executable='ros2_action_server',
            name='action_server_node',
            output='screen',  # 로그를 화면에 출력
        ),

        # ros2_service_server 노드 실행
        Node(
            package='ros2_example',
            executable='ros2_service_server',
            name='service_server_node',
            output='screen',  # 로그를 화면에 출력
        ),

        # ros2_topic_sub 노드 실행
        Node(
            package='ros2_example',
            executable='ros2_topic_sub',
            name='topic_sub_node',
            output='screen',  # 로그를 화면에 출력
        ),
    ])
