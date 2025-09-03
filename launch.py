from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    config_dir = os.path.join(
        os.getenv('HOME'), 'slam_ws', 'src', 'my_slam_launch', 'config'
    )

    return LaunchDescription([
        # Cartographer Node
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            parameters=[{
                'use_sim_time': False,
            }],
            arguments=[
                '-configuration_directory', config_dir,
                '-configuration_basename', 'p1.lua',
            ],
            remappings=[
                ('scan', '/p1/scan'),
                ('tf', '/p1/tf'),
                ('tf_static', '/p1/tf_static'),
                ('odom', '/p1/odom')
            ],
            output='screen',
        ),

        # Occupancy Grid Node
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_grid',
            parameters=[{'use_sim_time': False}],
            remappings=[
                ('tf', '/p1/tf'),
                ('tf_static', '/p1/tf_static'),
            ],
            output='screen',
        ),

        # Static TF: base_link -> laser_frame
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_tf_laser',
            arguments=['0', '0', '0.17', '0', '0', '0', 'base_link', 'laser_frame'],
            remappings=[
                ('tf', '/p1/tf'),
                ('/tf_static', '/p1/tf_static')
            ],
            output='screen',
        )
    ])