from setuptools import find_packages, setup

package_name = 'ros2_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/ros2_example', ['package.xml']), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='cknam0708@sju.ac.kr',
    description='ROS 2 Example Package with Custom Interfaces',
    license='TODO: License declaration',
    tests_require=['pytest'],
    test_suite='tests',  
    entry_points={
        'console_scripts': [
            'ros2_topic_sub=ros2_example.ros2_topic_sub.ros2_topic_sub:main',
            'ros2_topic_pub=ros2_example.ros2_topic_pub.ros2_topic_pub:main',
            'ros2_action_client=ros2_example.ros2_action_client.ros2_action_client:main',
            'ros2_action_server=ros2_example.ros2_action_server.ros2_action_server:main',
            'ros2_service_client=ros2_example.ros2_service_client.ros2_service_client:main',
            'ros2_service_server=ros2_example.ros2_service_server.ros2_service_server:main',
        ],
    },
)
