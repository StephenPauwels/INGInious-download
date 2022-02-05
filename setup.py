from setuptools import setup, find_packages

setup(
    name="inginious-download-submissions",
    version="0.1",
    description="Plugin to allow to download all evaluation submissions of students",
    packages=find_packages(),
    install_requires=["inginious"],
    test_require=[],
    extras_require={},
    scripts=[],
    include_package_data=True,
    author="Stephen Pauwels - UAntwerpen",
    author_email="stephen.pauwels@uantwerpen.be",
    license="AGPL 3",
    url=""
)