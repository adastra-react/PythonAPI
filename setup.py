from setuptools import setup, find_packages

setup(
    name='my_translation_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'deep_translator',
        'flask'
    ],
)
