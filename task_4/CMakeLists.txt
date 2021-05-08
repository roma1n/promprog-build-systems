cmake_minimum_required(VERSION 3.10)
 
project( task_4 )
 
find_package( OpenCV REQUIRED )
 
include_directories( ${OpenCV_INCLUDE_DIRS} )
 
# default solution
add_executable( main main.cpp )
target_link_libraries( main ${OpenCV_LIBS} )
 
# code generation
# generate file
add_custom_command(
    OUTPUT ${CMAKE_SOURCE_DIR}/code_gen.cpp
    COMMAND python ${CMAKE_SOURCE_DIR}/code_gen.py
)
 
add_executable( code_gen ${CMAKE_SOURCE_DIR}/code_gen.cpp )
target_link_libraries( code_gen ${OpenCV_LIBS} )