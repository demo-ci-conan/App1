from conans import ConanFile, CMake

class App1(ConanFile):
    name = "App1"
    version = "0.0"

    settings = "os", "arch", "compiler", "build_type"

    generators = "cmake"

    scm = {"type": "git",
           "url": "auto",
           "revision": "auto"}

    exports_sources = "LICENSE" # to avoid build info bug

    def requirements(self):
        self.requires("libB/0.0@demo/testing")
        self.requires("libC/0.0@demo/testing")
        self.requires("libG/0.0@demo/testing")
        self.requires("libH/0.0@demo/testing")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses")
