import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst',
    'CHANGES.rst',
])
setup(
    name='socketIO-client',
    version='0.7.1',
    description='A socket.io client library',
    long_description=DESCRIPTION,
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
    ],
    keywords='socket.io node.js',
    author='Roy Hyunjin Han',
    author_email='rhh@crosscompute.com',
    url='https://github.com/invisibleroads/socketIO-client',
    install_requires=[
        'requests>=2.7.0',
        'six',
        'websocket-client==0.39.0',
    ],
    tests_require=[
        'nose',
        'coverage',
    ],
    dependency_links=[
        'https://github.com/schrodingersket/websocket-client/tarball/master#egg=websocket-client-0.39.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False)
