from setuptools import setup

setup(
    name='mod_hello',
    packages=['mod_hello'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
