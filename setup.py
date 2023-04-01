from distutils.core import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="CapSolverpy",
    version="1.0",
    packages=["CapSolverpy"],
    url="https://github.com/neyboo/capsolverpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Neyboo Lux",
    author_email="admin@archo.host",
    description="CapSolver.com library for Python",
    requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    use_scm_version=True,
    setup_requires=["setuptools_scm", "wheel"],
    install_requires=["requests", "six"],
    python_requires=">=3",
    project_urls={
        "Documentation": 'https://github.com/neyboo/capsolverpy#readme',
        "Source": 'https://github.com/neyboo/capsolverpy',
        "Tracker": 'https://github.com/neyboo/capsolverpy/issues',
    },
)