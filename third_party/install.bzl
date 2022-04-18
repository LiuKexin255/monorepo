"""安装工具"""

load("//third_party/python:install.bzl", python_install = "install")
load("//third_party/go:install.bzl", go_install = "install")

def install():
    go_install()
    python_install()
