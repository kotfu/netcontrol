# netcontrol
Tool for ham radio net controllers to run and log a net

## Set up your dev environment

### OSX/MacOS

#### Install Python 3.5
We can't use python 3.6 yet because PyInstaller doesn't support Python 3.6.

You can use homebrew to install python

```sh
$ brew install python
```

or use pyenv

```sh
$ brew install pyenv
$ env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install -v 3.5.3
$ pyenv shell 3.5.3
```

You will also need pip and setuptools:

```sh
$ pip3 install -U pip setuptools
```

#### Install the other dependencies

```sh
$ python3 setup.py develop
$ pip install -e .[dev,test]
```

## Run from the command line

```sh
$ python3 -m netcontrol
```

## Build a binary distribution

### OSX/MacOS

```sh
$ pyinstaller --onefile --windowed netcontrol/netcontrol.py
```
