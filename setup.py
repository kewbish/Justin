from setuptools import setup

setup(
    name='Justin',
    description='A personalized assistant interface.',
    version='0.99',
    url='https://github.com/kewbish/Justin',
    author='kewbish',
    author_email='kewbish@gmail.com',
    install_requires=['requests', 'terminaltables==3.1.0'],
    entry_points={
        'console_scripts': [
            'justin = justin.justin_command',
        ]
    },
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ]
)
