from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Simple iRacing API Wrapper"
LONG_DESCRIPTION = "A Python app to get data from the iRacing API endpoints. Helps you get stats, race results, and more! 🏎️ 🏁"

# Setting up
setup(
    name="iracing_garage",
    version=VERSION,
    author="Dang Khoi Vo",
    author_email="<vo.dangkh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=[
        "python",
        "api",
        "racing",
        "iracing",
        "api-wrappers",
        "iracing-api",
    ],
    classifiers=[
        "Development Status :: 1 - Initial Launch",
        "Intended Audience :: Community",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
