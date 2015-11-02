from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import cython_gsl
import numpy as np

extensions = [
    Extension("wigner_3j.wigner_3j",
              sources=["wigner_3j/wigner_3j.pyx"],
              language="c", libraries = cython_gsl.get_libraries(),
              library_dirs = [cython_gsl.get_library_dir()],
              include_dirs = [cython_gsl.get_cython_include_dir(), np.get_include()])
]

setup(
    name='Max Help',
    version='0.01',
    packages=['wigner_3j'],
    url='',
    license='',
    author='Bryan Weinstein',
    author_email='bweinstein@seas.harvard.edu',
    description='',
    include_dirs = [cython_gsl.get_include(), np.get_include()],
    ext_modules = cythonize(extensions, annotate=True, reload_support=True)
)