cmake_minimum_required(VERSION 3.5)
set(PROJECT_NAME HALArduino)
project(${PROJECT_NAME} VERSION 1.0.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB_RECURSE ${PROJECT_NAME}_HDRS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.h)
file(GLOB_RECURSE ${PROJECT_NAME}_SRCS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

generate_arduino_library(${PROJECT_NAME})
