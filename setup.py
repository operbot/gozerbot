# This file is placed in the Public Domain.


"object programming runtime"


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="gozerbot",
    version="100",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/gozerbot",
    description="python3 irc bot",
    long_description=read(),
    license="Public Domain",
    packages=["gozerbot", "gozerbot.mod"],
    include_package_data=True,
    data_files=[
                ("share/gozerbot", ["files/gozerbot.service",]),
               ],

    scripts=["bin/gozerbot", "bin/gozerbotcmd", "bin/gozerbotctl", "bin/gozerbotd"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
