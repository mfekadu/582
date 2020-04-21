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
import os
from typing import Any, Callable, Iterator, List, NewType, Optional, Type, Union

import spacy
from sklearn.feature_extraction import DictVectorizer
from typing_extensions import Literal, TypedDict

import pandas as pd
from utils.terminal_colors import print_debug

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

# TODO: organize this...
VectorizedInput = Any
VectorizedOutput = Any
SpacyNLP = spacy.language.Language
NLP = Union[SpacyNLP, SpacyNLP]  # Union[SpacyNLP, SomeOtherNLP]


def _extract_entities_spacy(overview: Overview, nlp: SpacyNLP) -> List[str]:
    """
    Returns a list of entities inside the document using spaCy as nlp.
    """
    assert isinstance(nlp, spacy.language.Language), "only spacy nlp allowed"
    doc = nlp(overview)
    return [ent.text for ent in doc.ents]


def _extract_entities(overview: Overview, nlp: Optional[NLP] = None) -> List[str]:
    """
    Returns a list of entities inside the document.
    """
    return _extract_entities_spacy(overview, nlp)


def _vectorize_by_entities(
    overview: Overview, nlp: Optional[NLP] = None
) -> VectorizedInput:
    """This does the vectorization based on the entities inside the overview.
    Basically creates a giant spreadsheet.
    One-hot encoding.

    Args:
        overview: An [`Overview`](#labs.lab1.Overview) string about the movie.
        nlp: the [`NLP`](#labs.lab1.NLP) pipeline to extract entities with. Defaults to spaCy.

    Resources:
        https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html
    """

    entities: List[str] = _extract_entities(overview, nlp)

    # TODO: normalize `entities`

    vectorizer = DictVectorizer(sparse=False)

    vocabulary_file = "models/vocabulary.csv"

    assert os.path.isfile(
        vocabulary_file
    ), f"expected vocabulary file: {vocabulary_file}"

    vocabulary: dict = pd.read_csv(vocabulary_file).T.to_dict()[0]

    ent_map = {e: 1 for e in entities if e in vocabulary}

    # in this case we only have one document: `overview`.
    # but imagine there could be more documents, thus more predictions
    ent_map_list: List[dict] = [ent_map]

    # this encodes all numbers as one-hot arrays of binary data, again becsuse NN
    one_hot = vectorizer.fit_transform(ent_map_list)

    assert vectorizer.inverse_transform(one_hot) == ent_map_list

    return one_hot


def _vectorize(overview: Overview, nlp: Optional[NLP] = None) -> VectorizedInput:
    """
    Returns the input transformed into one-hot vectors via DictVectorizer
    """
    return _vectorize_by_entities(overview, nlp)


def _predict_director_vec(input_vector: VectorizedInput) -> VectorizedOutput:
    """
    Returns the predictions of the `entities_predict_director.h5` model
    """
    pass


def _predict_director(overview: Overview, nlp: Optional[NLP] = None) -> str:
    """
    Returns a director prediction from the overview.
    """
    model_input = _vectorize(overview, nlp)
    pass


def producer(
    overview: Overview, nlp: Optional[NLP] = None, use_large=False
) -> Suggestions:
    """A robot movie producer.

    Args:
        overview: an [`Overview`](#labs.lab1.Overview) string about the movie.

    Returns:
        A dictionary of [`Suggestions`](#labs.lab1.Suggestions).
    """
    model_name = "en_core_web_lg" if use_large else "en_core_web_sm"
    nlp: NLP = spacy.load(model_name) if nlp == None else nlp

    if not isinstance(nlp, spacy.language.Language):
        raise NotImplementedError("non-spacy NLP is not yet implemented")

    if DEBUG:
        print_debug("model_name", model_name)
        print_debug("nlp", nlp)

    entities: List[str] = _extract_entities(overview, nlp)
    print_debug("entities", entities) if DEBUG else None

    model_output: str = _predict_director(overview, nlp)
    print_debug("model_output", model_output) if DEBUG else None

    cast1 = FullName("Good Actress")
    cast2 = FullName("Good Actor")
    director = FullName("Good Director")
    suggestions: Suggestions = {
        "title": "A Good Movie Title",
        "director": director,
        "cast": [cast1, cast2],
    }
    return suggestions
