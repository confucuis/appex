from setuptools import setup, find_packages

setup(
    name="appex",
    version="0.1.0",
    package_dir={"": "src"},  # 指定源码所在目录
    packages=find_packages(where="src"),  # 从`src`目录寻找包
)
