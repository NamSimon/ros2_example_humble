cmake_minimum_required(VERSION 3.5)
project(custom_interfaces)

# ROS 2 기본 빌드 의존성
find_package(rosidl_default_generators REQUIRED)

# 메시지, 서비스, 액션 정의 파일
set(action_files
  "action/CountDown.action"
)

# 인터페이스 빌드
rosidl_generate_interfaces(${PROJECT_NAME}

  ${action_files}
)

# 설치
ament_package()