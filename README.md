# 582

CSC 582 Natural Language Processing

## [Documentation][1]

## Getting Started

### 1. [Install Poetry][2]

Works with macOS, Linux, [Windows][3].

### 2. Setup virtual environment

```bash
poetry install
```

This will create a virtual environment with the required:

- [Python 3.6.8][4]
- all the `[packages]` listed in the [`pyproject.toml`](./pyproject.toml), which is [standardized][5].

### 3. Open virtual environment

```bash
poetry shell
```

### 4. Verify your python version

```bash
$ poetry env info

Virtualenv
Python:         3.6.8
Implementation: CPython
Path:           /path/to/.../.../pypoetry/virtualenvs/582-Edwit1zX-py3.6
Valid:          True

System
Platform: darwin (example on macOS)
OS:       posix  (example on macOS)
Python:   /Library/Frameworks/Python.framework/Versions/3.6  (example on macOS)
```

### 5. Download NLP stuff

```bash
$ python -m spacy download en_core_web_sm
$ python -m spacy download en_core_web_lg
```

## Module Examples

```python
from labs.lab1 import producer
producer("good movie overview")
>>>
{
    "title": "A Good Movie Title",
    "director": "Good Director",
    "cast": ["Good Actress", "Good Actor"],
}
producer("bad movie overview")
>>>
{
    "title": "A Bad Movie Title",
    "director": "Bad Director",
    "cast": ["Bad Actress", "Bad Actor"],
}
```

## Command-Line Usage

### Lab1

```
$ python main.py lab1 inputs/in1.txt
$ python robotproducer.py inputs/in1.txt
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

- [**foobar**][6]
- [**foobar**][6]

[1]: https://mfekadu.github.io/582/
[2]: https://python-poetry.org/docs/#installation
[3]: https://python-poetry.org/docs/#installation
[4]: http://python.org
[5]: https://www.python.org/dev/peps/pep-0518/
[6]: ????