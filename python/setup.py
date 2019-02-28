from setuptools import setup

setup(
    name="life",
    version="1.0.0",
    description="Conway's game of life.",
    author="Dylan Anderson",
    url="https://github.com/DylanAnderson/life",
    py_modules=["life"],
    python_requires=">=3.6.0",
    install_requires=["numpy"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Console :: Curses"
    ]
)
