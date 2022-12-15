from setuptools import setup, find_packages

setup(
    name='acppred',
    version='0.0.1',
    packages=find_packages(),
    author='Elias Eduardo Barbosa da Rosa',
    entry_points = {
        'console_script': [
            'acppred-train = acppred.train:main',
        ]
    }
)