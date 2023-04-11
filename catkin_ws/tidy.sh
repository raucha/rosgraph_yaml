
cd /workspaces/rosgraph_yaml/catkin_ws
catkin_make -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=1

cd build
clang-tidy -checks=* ../src/navigation/base_local_planner/src/trajectory.cpp