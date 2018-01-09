from distutils.core import setup

setup(
    name='conversion_scripts',
    version='0.0.1',
    packages=['converters', 'utils'],
    url='https://github.com/QROWD/conversion_scripts',
    license='Apache License Version 2.0',
    author='Patrick Westphal',
    author_email='patrick.westphal@informatik.uni-leipzig.de',
    description='',
    scripts=['bin/convert_abbreviations'],
    install_requires=[
        'rdflib==4.2.2'
    ]
)
