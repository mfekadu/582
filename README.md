# 582
CSC 582 Natural Language Processing

## [Documentation][1]

## Getting Started

### 1. [Install Pipenv][2]

Works with macOS, Linux, [Windows][3].

### 2. Setup virtual environment

```bash
pipenv install
```

This will create a virtual environment with the required:

- [Python 3.6.8][4]
- all the `[packages]` listed in the [`Pipfile`](./Pipfile)

### 3. Open virtual environment

```bash
pipenv shell
```

### 4. Verify your python version

```bash
$ python --version
Python 3.6.8
```

## Module Examples 

```python
from labs.lab1 import producer
producer("bad movie overview")
>>> {"title_suggestion": "Bad Movie", "director_suggestion": "Bad Director", "cast_suggestion": "Bad Cast"} 
producer("good movie overview")
>>> {"title_suggestion": "Good Movie", "director_suggestion": "Good Director", "cast_suggestion": "Good Cast"} 
```

## Command-Line Usage 

### Lab1
```
$ python main.py lab1 [input.txt]
$ python robotproducer.py [input.txt]
```

![demo.png](./demo.png)

## How it works

**Assumptions**
- ...
- ...

**Pipeline**

1. ...
2. ...
3. ...

## TODO

- [x] ...
- [ ] ...


## More Details
...
...

## Resources
- [**foobar**][5]
- [**foobar**][5]


[1]: https://mfekadu.github.io/582/
[2]: https://pipenv.pypa.io/en/latest/install/#installing-pipenv
[3]: https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv
[4]: http://python.org
[5]: ???

