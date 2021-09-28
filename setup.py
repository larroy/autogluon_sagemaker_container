#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup
from pkutils import parse_requirements

INSTALL_REQUIRES = list(parse_requirements("requirements.txt"))
EXTRAS_REQUIRE = {"test": list(parse_requirements("requirements-dev.txt"))}

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="autogluon_container",
    version="0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    #package_data={"": [""]},
    #include_package_data=True,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    scripts=["bin/entrypoint.py"],
    data_files=[
    ],
)
