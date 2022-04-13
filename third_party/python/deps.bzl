"""安装 python 依赖"""

load("@python_deps//:requirements.bzl", "install_deps")

def dependence():
    install_deps()
