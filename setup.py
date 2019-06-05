import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open('trellab/version.py').read()) # loads __version__

setup(
    name='trellab',
    version=__version__,
    author='Zulko',
    url='https://github.com/Edinburgh-Genome-Foundry/trellab',
    description='Python-Trello routines for project-tracking in a biofoundry',
    long_description=open('pypi-readme.rst').read(),
    license='MIT',
    keywords="Trello DNA assembly biofoundry",
    packages=find_packages(exclude='docs'),
    install_requires=['py-trello', 'pyyaml', 'python-box', 'fuzzywuzzy']
)
