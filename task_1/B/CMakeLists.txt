cmake_minimum_required(VERSION 3.16)
project(B)

set(CMAKE_C_STANDARD 99)

add_library(B_lib STATIC lib.c)
