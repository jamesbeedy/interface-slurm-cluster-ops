from setuptools import find_packages, setup


setup(
    name='interface-slurm-cluster',
    packages=find_packages(include=['interface_slurm_cluster']),
    version='0.0.1',
    license='MIT',
    long_description=open('README.md', 'r').read(),
    url='https://github.com/omnivector-solutions/interface-slurm-cluster-ops',
    install_requires=[],
    python_requires='>=3.6',
)
