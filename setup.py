from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()


setup(
    name='dmensamenu',
    version='0.0.1',
    description='Print Heidelberg INF canteen menu using dmenu',
    long_description=long_description,
    url='https://github.com/dotlambda/dmensamenu',
    author='Robert Schütz',
    author_email='robert.schuetz@stud.uni-heidelberg.de',
    license='MIT',
    
    classifiers=[
        'Programming Language :: Python :: 3'
    ],

    packages=['dmensamenu'],
    install_requires=['beautifulsoup4', 'requests'],

    python_requires='>=3',

    entry_points={
        'console_scripts': [
            'dmensamenu=dmensamenu.dmensamenu:main',
        ],
    }
)
