from setuptools import find_packages, setup
setup(
    name='pywebselenium',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='My first python Library',
    author='me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
