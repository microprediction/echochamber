import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="echochamber",
    version="0.0.6",
    description="Using an Echo State Network to crawl Microprediction.Org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/echochamber",
    author="microprediction",
    author_email="info@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["echochamber"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["pathlib","microprediction","numpy"],
    entry_points={
        "console_scripts": [
            "echochamber=echochamber.__main__:main",
        ]
     },
     )
