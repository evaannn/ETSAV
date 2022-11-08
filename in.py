# ETSAV - evans terrible and shitty audio visualizer

import sys
from setuptools import setup, find_packages

with open("README.md", "r") as exdee:
    long_description = exdee.read()

if sys.version_info < (3, 5):
    raise EnvironmentError("yo dumbass you need python 3.7 lol")



MAJOR       = 0
MINOR       = 2
MICRO       = 0
PRE_RELEASE = 'a'
VERSION = f"{MAJOR}.{MINOR}.{MICRO}-{PRE_RELEASE}"

DEFAULT_URL = 'https://evan.systems'

metadata = dict(
    name='evans terrible and shitty audio visualizer',
    version=VERSION,
    description='audio waveform generator but shitty and garbage',
    long_description=long_description,
    url=DEFAULT_URL,
    download_url=DEFAULT_URL+'releases/',
    author='evan (god)',
    author_email='me@evan.systems',
    keywords="shit cum balls audio visualizer",
    project_urls={
        "Bug Tracker": DEFAULT_URL+"issues/"
    },
    install_requires=['numpy',
                      'scipy',
                      'matplotlib',
                      'opencv-python'],
    packages=find_packages()
)

setup(**metadata)
