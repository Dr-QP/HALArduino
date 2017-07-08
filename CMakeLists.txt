cmake_minimum_required(VERSION 3.8.0)
set(CMAKE_TOOLCHAIN_FILE ${CMAKE_SOURCE_DIR}/cmake/ArduinoToolchain.cmake)
set(PROJECT_NAME HALArduino)
project(${PROJECT_NAME} VERSION 1.0.0)

# include(CTest)
# enable_testing()

file(GLOB_RECURSE ALL_CODE_HDRS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.h)
file(GLOB_RECURSE ALL_CODE_SRCS ${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp)

add_library(${PROJECT_NAME} ${ALL_CODE_HDRS} ${ALL_CODE_SRCS} ${SOURCE_FILES})

set_target_properties(${PROJECT_NAME} PROPERTIES LINKER_LANGUAGE CXX)

# set(CPACK_PROJECT_NAME ${PROJECT_NAME})
# set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
# include(CPack)

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

# # Register board and libraries
# link_directories(${CMAKE_SOURCE_DIR}/libraries)
# register_hardware_platform("${CMAKE_SOURCE_DIR}/hardware/XYZrobot")

# # Setup global config for board, port and serial
# set(ARDUINO_DEFAULT_BOARD XYZrobot1280)
# set(ARDUINO_DEFAULT_PORT /dev/cu.usbserial-A104D3XB)
# set(ARDUINO_DEFAULT_SERIAL screen @SERIAL_PORT@ 115200)


# set(SOURCE_DIR ${CMAKE_SOURCE_DIR}/src)

# add_subdirectory(${SOURCE_DIR}/Bolide)
# add_subdirectory(${SOURCE_DIR}/RobotEditor)
# add_subdirectory(${SOURCE_DIR}/ServoIdSetting)