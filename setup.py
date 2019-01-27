from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dmensamenu',
    version='1.2.1',
    description='Print canteen menus using dmenu and OpenMensa',
    long_description=long_description,
    url='https://github.com/dotlambda/dmensamenu',
    author='Robert Schütz',
    author_email='robert.schuetz@stud.uni-heidelberg.de',
    license='MIT',
    
    classifiers=[
        'Programming Language :: Python :: 3'
    ],

    packages=['dmensamenu'],
    install_requires=['requests'],

    python_requires='>=3',

    entry_points={
        'console_scripts': [
            'dmensamenu=dmensamenu.dmensamenu:main',
        ],
    }
)
