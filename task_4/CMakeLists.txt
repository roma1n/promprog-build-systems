cmake_minimum_required(VERSION 3.10)

project( task_4 )

find_package( OpenCV REQUIRED )

include_directories( ${OpenCV_INCLUDE_DIRS} )

# default solution
add_executable( main main.cpp )
target_link_libraries( main ${OpenCV_LIBS} )

# code generation
# generate file
execute_process(
    COMMAND python ${CMAKE_SOURCE_DIR}/generate_code.py
)

add_executable( code_gen code_gen.cpp )
target_link_libraries( code_gen ${OpenCV_LIBS} )