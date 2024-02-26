from setuptools import setup

setup(
    name='DeadPixl',
    version='1.0',
    description='A tool to test for dead pixels on display screens',
    author='Tao Vuokko',
    packages=['dead_pixl'],
    install_requires=[
        'pygame>=2.5.2',
    ],
    entry_points={
        'console_scripts': [
            'dead_pixel_tester=dead_pixel_tester.main:main',
        ],
    },
)
