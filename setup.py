from setuptools import find_packages, setup

setup(
    name="py-rust-fib",
    version = "0.0.1",
    author= "Charles Gallagher",
    author_email="charles.gallagher07@gmail.com",
    description= "calculate fib numbers",
    url="https://github.com/CRG180/py-rust-fib",
    install_requires = [],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development status :: 4 - Beta",
        "Programing Language ::  Python ::3",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3",
    test_requires = ['pytest']
)