from setuptools import setup, find_packages

setup(
    name="caesar-cli",
    version="1.0.0",
    description="Simple Caesar cipher CLI tool",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Songa Praneeth",
    url="https://github.com/SongaPraneeth/praneeth-cyber-tools",  
    packages=find_packages(exclude=("tests",)),
    entry_points={
        "console_scripts": [
            "caesar=caesar_cipher.caesar:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
)
#adfasfdafa