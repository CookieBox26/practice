# practice

These codes are for CUDA 11.8 + cuDNN v8.9.2 on Window 11.  

### Installation

If you do not have **[Poetry](https://python-poetry.org/docs/)**, please open Windows PowerShell as administrator and run the command below.
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Then, please add the directory where Poetry was installed to your PATH.
```
$ export PATH=${PATH}:/c/Users/`whoami`/AppData/Roaming/Python/Scripts
$ poetry --version
Poetry (version 1.5.1)
```
Then, you can run the command below.
```
poetry install
poetry run pytest
```

### References
- [Poetry](https://python-poetry.org/docs/)
