cmake_minimum_required(VERSION 3.5)
project(PackageTest CXX)

if(NOT EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    message(WARNING "The file conanbuildinfo.cmake doesn't exist.\nRunning 'conan install' first...")
    execute_process(COMMAND conan install "${CMAKE_CURRENT_SOURCE_DIR}" -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++11
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
endif()

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

generate_arduino_firmware(${PROJECT_NAME}
        SKETCH example.ino
#        ARDLIBS StandardCplusplus
        )