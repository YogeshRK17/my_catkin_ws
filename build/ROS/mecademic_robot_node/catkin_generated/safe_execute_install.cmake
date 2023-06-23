execute_process(COMMAND "/home/yogesh/catkin_ws/build/ROS/mecademic_robot_node/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/yogesh/catkin_ws/build/ROS/mecademic_robot_node/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
