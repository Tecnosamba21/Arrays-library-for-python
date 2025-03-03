import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'Array_utilities'
AUTHOR = 'TecnoSamba21'
AUTHOR_EMAIL = 'sannicolas2121@outlook.com' #Modificar con vuestros datos

LICENSE = 'MIT'
DESCRIPTION = 'Utilidades para mejorar el trabajo con arrays'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
