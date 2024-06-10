from setuptools import setup, find_packages

setup(
    name='snake-game-tk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'snake-game-tk = snake_game.main:run'
        ]
    },
    author="Leo Vidarte",
    author_email="lvidarte@gmail.com",
    description="A simple Snake game using Tkinter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lvidarte/snake_game",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
