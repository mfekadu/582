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

- [**foobar**][5]
- [**foobar**][5]

[1]: https://mfekadu.github.io/582/
[2]: https://pipenv.pypa.io/en/latest/install/#installing-pipenv
[3]: https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv
[4]: http://python.org
[5]: ???
