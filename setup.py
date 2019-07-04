"""  """
# pylint: disable=I0011,W0312,C0410
import os
from setuptools import setup, find_packages

REQUIREMENTS = ['exoedge>=18.11.17', 'pymodbus', 'six']

def read(fname):
    """ Primarily used to open README file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

try:
    README = read('README.rst')
except:
    README = 'README Not Found'

version = {}
with open("exoedge_modbus/__version__.py") as fp:
    exec(fp.read(), version) # pylint: disable=W0122
    assert version.get('__version__'), "Unable to parse version from exoedge_modbus/__version__.py."

setup(
    name="exoedge_modbus",
    version=version['__version__'],
    author="Exosite LLC",
    author_email="support@exosite.com",
    description="An ExoEdge source for interfacing with Modbus devices.",
    license="Apache 2.0",
    keywords="murano exosite iot iiot client gateway modbus tcp rtu",
    url="https://github.com/exosite/lib_exoedge_modbus_python",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'exomod = exoedge_modbus.cli:main',
        ]
    },
    install_requires=REQUIREMENTS,
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Operating System Kernels :: Linux",
        "Topic :: Software Development :: Embedded Systems",
        "License :: OSI Approved :: Apache Software License",
    ],
)
