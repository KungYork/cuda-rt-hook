from setuptools import setup, find_packages
import os, sys

def sync_shell(cmd):
    err = os.system(cmd)
    assert not err, f'exec cmmand:{cmd} fail!'

sync_shell("rm -rf build")
script_dir = os.path.dirname(os.path.abspath(__file__))
sync_shell(f"cmake -S {script_dir} -B build -GNinja && cmake --build build")
sync_shell(r"cd build/lib && ls | grep -v '\<cuda_mock\>' | xargs -I {} rm -rf {}")

setup(
    name="cuda-mock",
    version="0.0.4",
    author="lipracer",
    author_email="lipracer@gmail.com",
    description="a tools hook some api call at runtime",

    url="https://github.com/lipracer/torch-cuda-mock", 

    packages=['cuda_mock'],
    package_dir={'cuda_mock': 'src/cuda_mock'}
)