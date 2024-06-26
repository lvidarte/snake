# Snake Game

A simple Snake game implemented in Python using Tkinter.

![Snake window](https://github.com/lvidarte/snake/raw/main/snake.png)

## Installation

You can install the package via pip. Simply run the following command:

```sh
pip install snake-game-tk
```

Alternatively, you can clone the repository and run it manually:


1. **Clone the repository**

```sh
git clone https://github.com/lvidarte/snake_game.git
```

2. **Install Tkinter Library**

```sh
sudo apt update
sudo apt install python3-tk
```

3. **Play!**

```sh
cd snake_game
python -m snake_game.main
```

4. **Run Tests**

```sh
cd snake_game
python -m unittest discover -s tests
```

## Requirements

Snake game requires Tkinter. Please install the 'python-tk' package for your system.

1. Ubuntu/Debian

```sh
sudo apt install python3-tk
```

2. Fedora

```sh
sudo dnf install python3-tkinter
```

3. Arch Linux

```sh
sudo pacman -S tk
```

4. MacOS

```sh
brew install python-tk
```