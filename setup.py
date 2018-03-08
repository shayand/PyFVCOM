from setuptools import setup

setup(
    name = 'PyFVCOM',
    packages = ['PyFVCOM'],
    version = '2.1.0',
    description = ("PyFVCOM is a collection of various tools and utilities which can be used to extract, analyse and plot input and output files from FVCOM."),
    author = 'Pierre Cazenave',
    author_email = 'pica@pml.ac.uk',
    url = 'https://gitlab.ecosystem-modelling.pml.ac.uk/fvcom/PyFVCOM',
    download_url = 'http://gitlab.em.pml.ac.uk/fvcom/PyFVCOM/repository/archive.tar.gz?ref=2.1.0',
    keywords = ['fvcom', 'unstructured grid', 'mesh'],
    license = 'MIT',
    platforms = 'any',
    install_requires = ['pyshp', 'jdcal', 'scipy', 'numpy>=1.13.0', 'matplotlib', 'netCDF4', 'lxml', 'pyproj', 'pytz', 'networkx', 'UTide', 'pandas', 'cmocean'],
    classifiers = []
)

