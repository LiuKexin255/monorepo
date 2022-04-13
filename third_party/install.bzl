"""安装工具"""

load("//third_party/python:install.bzl", python_install = "install")

def install():
    python_install()
