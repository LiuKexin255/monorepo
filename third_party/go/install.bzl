load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")
load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

go_version = "1.18"

def install():
    """安装 golang 工具"""

    go_rules_dependencies()

    go_register_toolchains(version = go_version)

    gazelle_dependencies()
