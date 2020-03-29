from setuptools import setup

setup(
    name="Justin",
    description="A personalized assistant interface.",
    version="1.0",
    url="https://github.com/kewbish/Justin",
    author="kewbish",
    author_email="kewbish@gmail.com",
    install_requires=["requests==2.23.0", "terminaltables==3.1.0"],
    packages=["justin"],
    entry_points={"console_scripts": ["justin = justin.justin:jstn_command"]},
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
)
