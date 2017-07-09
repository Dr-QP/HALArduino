from conans import ConanFile, CMake, tools
import os


class HalarduinoConan(ConanFile):
    name = "HALArduino"
    version = "develop"
    license = "Apache License, Version 2.0. https://www.apache.org/licenses/LICENSE-2.0"
    url = "https://github.com/Dr-QP/HALArduino"
    author = "Anton Matosov (anton.matosov@gmail.com)"
    description = "HAL layer implementation for Arduino"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "*", "!build/*", "!test_package/*"
    requires = "HAL/develop@anton-matosov/dev"

    def build(self):
        cmake = CMake(self)
        self.run('cmake . %s' % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*HALArduino.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.cppflags = ['-std=c++11']
        self.cpp_info.libs = ["HALArduino"]
