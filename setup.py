from setuptools import setup, find_packages

setup(
    name='QVasp',
    description='A quick post-process for resolve or assistant the VASP calculations',
    author='hui_zhou',
    version='0.0.1',
    license='GPL-3.0',
    python_requires='>=3.9',
    platforms="manylinux_x86_64",
    packages=find_packages(),
    install_requires=[
        'Cython',
        'lxml',
        'matplotlib',
        'numpy',
        'pandas',
        'pymatgen',
        'pymatgen-analysis-diffusion',
        'pyyaml',
        'scipy'],
    include_package_data=True,
    package_data={"QVasp": ["lib/*.so", "*.json", "*.yaml", "INCAR", "pot.tgz"]},
    entry_points={'console_scripts': ['QVasp = QVasp.main:main']}
)
