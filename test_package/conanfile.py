from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "dev")
username = os.getenv("CONAN_USERNAME", "anton-matosov")


class HalarduinoTestConan(ConanFile):
    settings = {"os": ["Arduino"],
                "compiler": {
                    "gcc": {
                        "version": ["4.9"],
                        "libcxx": ["libstdc++11"]
                    }
                },
                "arch": ["avr"]}
    requires = "HALArduino/develop@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        # Tests need to be uploaded to Arduino to run. So do nothing for now
        # self.run(".%sexample" % os.sep)
