"""安装 python 工具和依赖"""

load("@python3_sdk//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")
load(":defs.bzl", "requirements_lock")

def install():
    pip_parse(
        name = "python_deps",
        python_interpreter_target = interpreter,
        requirements_lock = requirements_lock,
        extra_pip_args = [
            "-i",
            "https://pypi.tuna.tsinghua.edu.cn/simple",
        ],
    )
