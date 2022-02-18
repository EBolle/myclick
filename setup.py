# from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='myclick',
    version='0.1.0',
    py_modules=['myclick'],
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts': [
            'myclick = myclick:cli'
        ],
    }
)