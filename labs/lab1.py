"""
# Lab 1: Robot Movie Producer

[//]: # (markdown comment # noqa)

This lab is really simple. You're supposed to just answer one email!

The situation is this: People have lots of ideas about movies.
They can write a short synopsis of the plot.
What they want to know is who should be acting in the movie?
Who should direct it?
And lastly, what should the title be?

So, imagine you get an email (example below) that has a description of a movie.
Your job is to reply back with suggestions of 5-10 actors, a director and title.
That's it!

The deliverable is a python3 program: robotproducer.py [input.txt]

Where input.txt is a plaintext file with content similar to the following:

```
This is a no holds-barred thrilling drama mixed with killing, mayhem and manipulation among working professionals.
This film sheds light on a man's downfall from the pinnacles of success into the depths of his damaged character.
His insecurities lead him into a series of troubled romantic relationships and eventually a web of events that include betrayal and murder.
```

Output to the screen should be like the following;

```
Title suggestion: A crazy work week!

Director suggestion: SOME NAME

Cast suggestions: NAME1, NAME2, NAME3, ...
```


I was just kidding.
This is actually a very difficult, cutting-edge problem.
So, know that I'm not interested in perfection just interesting approaches.

Use the Kaggle database TMDB Movie metadata: https://www.kaggle.com/tmdb/tmdb-movie-metadata

It has two data files totaling about 50MB.
We are interested in three main columns (but you may use any column available, they would actually help).
The three columns are: Title, Overview, Cast (only names) and Crew:Director.


# How to evaluate this?

The title is simply very difficult to evaluate, so that's just something I can assess based on creativity.

However, the director and the cast can be numerically evaluated if you set up the problem as a machine learning exercise.
Divide all the movies into training/test randomly with appropriate ratios.
Then use the description (overview) of one of the test set movies as input into your program.
Evaluate the output like this:

+ 20 points if you get the director right. (20 max)

+ 10 points for every cast member that you guessed that appears on the cast list.
Up to 50 maximum points.

+ 5 points for every cast member guessed correctly that also appears on the top 5 (orders 0-4) of the cast list. (25 max)

Now, optimize for maximum possible score (95).

Submit your code via Polylearn as a zip file.
If you did this on Google Collab, you may download as Python then submit that file.
In addition, to submitting the downloaded .py (from Collab), also share your collab notebook with me (foaadk@gmail.com) and submit a link via Polylearn online text.
"""

# flake8: noqa
from typing import Callable, Iterator, List, NewType, Type

from typing_extensions import Literal, TypedDict

__pdoc__ = {}

DEBUG = False

Overview = NewType("Overview", str)
"""Overview"""
__pdoc__[
    "Overview"
] = """A Overview type
Example:
    ```
    \"\"\"
    This is a no holds-barred thrilling drama mixed with killing,
    mayhem and manipulation among working professionals.
    This film sheds light on a man's downfall
    from the pinnacles of success into the depths of his damaged character.
    His insecurities lead him into a series of troubled romantic relationships
    and eventually a web of events that include betrayal and murder.
    \"\"\"
    ```
"""

FullName = NewType("FullName", str)
"""FullName"""
__pdoc__[
    "FullName"
] = """A FullName type
Example:
    ```
    "FirstName LastName"
    ```
"""

Suggestions = TypedDict(
    "Suggestions", {"title": str, "director": FullName, "cast": List[FullName]},
)
"""Suggestions"""
__pdoc__[
    "Suggestions"
] = """A Suggestions type.

The movie production suggestions that our RobotProducer will provide.

Example:
    ```
    {
        "title": "A Good Movie Title",
        "director": "Good Director",
        "cast": ["Good Actress", "Good Actor", ... ]
    }
    ```
"""


def producer(overview: Overview) -> Suggestions:
    """A robot movie producer.

    Args:
        overview: an [`Overview`](#labs.lab1.Overview) string about the movie.

    Returns:
        A dictionary of [`Suggestions`](#labs.lab1.Suggestions).
    """
    cast1 = FullName("Good Actress")
    cast2 = FullName("Good Actor")
    director = FullName("Good Director")
    suggestions: Suggestions = {
        "title": "A Good Movie Title",
        "director": director,
        "cast": [cast1, cast2],
    }
    return suggestions
