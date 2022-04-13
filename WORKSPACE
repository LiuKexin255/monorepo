workspace(
    name = "monorepo",
)

load("//:archive.bzl", "download_archive")

download_archive()

##################################################################
# 安装 python 工具
load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_version = "3.10"

python_register_toolchains(
    name = "python3_sdk",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = python_version,
)

# 安装依赖

load("//third_party:install.bzl", "install")

install()

load("//third_party:deps.bzl", "dependence")

dependence()
