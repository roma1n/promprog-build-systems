cmake_minimum_required(VERSION 3.16)
project(task_1)

set(CMAKE_C_STANDARD 99)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# generate file for project A
execute_process(
    COMMAND python ${CMAKE_SOURCE_DIR}/A/preparing.py
)

set(MAIN C/main.c)

include_directories(.)

add_subdirectory(B)

add_executable(task_1 ${MAIN})

target_link_libraries(task_1 B_lib)