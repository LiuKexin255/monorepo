"""安装第三方依赖"""

load("//third_party/python:deps.bzl", python_dependence = "dependence")

def dependence():
    python_dependence()
