from setuptools import setup

setup(
    name='Justin',
    version='0.1',
    packages=['justin'],
    url='https://github.com/kewbish/Justin',
    license='NOASSERTION',
    author='kewbish',
    author_email='xyz@abc.com',
    description='Personal Assistant Dashboard',
    package_data={'justin': ['*', '*.*', 'platform/*', 'initializer/*'], '.': [".git/info/*"]},
    include_package_data=True,
    install_requires=['requests', 'terminaltables==3.1.0'],
    entry_points={
        'console_scripts': [
            'justin = justin.justin:main',
        ]
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX'
    ]
)
