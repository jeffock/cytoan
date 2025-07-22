from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="cytoan",
    version="0.0.1",
    description="Cell image processing & analysis library",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffock/cytoan",
    author="jeffock",
    author_email="jeffock1656@gmail.com",
    license="GPL-3.0-only",
    classifiers=[
        "License :: OSI Approved :: GPL v3.0",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": ["pytest>=8.4.1", "twine>=6.1.0"],
    },
    python_requires=">=3.12",
)