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
from typing import (
    Any,
    Callable,
    Iterator,
    List,
    NewType,
    Optional,
    Tuple,
    Type,
    Union,
    cast,
)

from keras.models import load_model
import numpy as np
import pandas as pd
import sklearn
import spacy
from sklearn.feature_extraction import DictVectorizer
from typing_extensions import Literal, TypedDict

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


# TODO: organize this && make better types
NumpyArray = Any  # np.ndarray
OneHot = List[List[int]]
VectorizedInput = Any  # List[int]
VectorizedOutput = Any  # List[int]  # Union[List[int], NumpyArray]
SpacyNLP = spacy.language.Language
NLP = Union[SpacyNLP]  # Union[SpacyNLP, SomeOtherNLP]
Vectorizer = Union[DictVectorizer]


def _is_spacy(nlp: Any):
    """
    Return True if the given object is an instance of the SpaCy NLP pipeline, else False.
    """
    return isinstance(nlp, spacy.language.Language)


def _extract_entities_spacy(overview: Overview, nlp: SpacyNLP) -> List[str]:
    """
    Returns a list of entities inside the document using spaCy as nlp.
    """
    assert _is_spacy(nlp), "only spacy nlp allowed"
    doc = nlp(overview)
    return [ent.text for ent in doc.ents]


def _extract_entities(overview: Overview, nlp: NLP) -> List[str]:
    """
    Returns a list of entities inside the document.
    """
    if _is_spacy(nlp):
        spacy_nlp: SpacyNLP = cast(SpacyNLP, nlp)  # pyre-ignore[22]
        return _extract_entities_spacy(overview, spacy_nlp)
    else:
        raise NotImplementedError("non-spacy NLP is not yet implemented")


def _file_exists(filename: str):
    return os.path.isfile(filename)


def _assert_file_exists(filename: str, msg: Optional[str] = None):
    msg = msg or f"expected file: {filename}"
    assert _file_exists(filename), msg


def _csv_to_dict(filename: str):
    """
    Example:
        **consider the following CSV**

         ,the 22nd century, the moon pandora
        0,7995            , 8373

        **example output**
        {
            "the 22nd century": 7995,
            "the moon pandora": 8373
        }
    """
    return pd.read_csv(filename).T.to_dict()[0]


def _get_vocabulary(vocab_csv_file: Optional[str] = None) -> dict:
    """
    TODO: ...
    FIXME: pd.read_csv is not memory efficient vs using `import csv`
    """
    vocabulary_file = vocab_csv_file or "models/vocabulary.csv"
    _assert_file_exists(vocabulary_file)
    vocabulary: dict = _csv_to_dict(vocabulary_file)
    return vocabulary


def _make_entity_vectorizer(
    entities: List[str], vocab_csv_file: Optional[str] = None
) -> Tuple[OneHot, Vectorizer]:
    """
    TODO: ...

    >>> one_hot
    array([[0., 1., 0.],
           [1., 0., 1.]])
    """
    vocabulary = _get_vocabulary(vocab_csv_file)
    # in this case we only have one document: `overview`,
    # but imagine there could be more documents, thus more predictions.
    # the value of each entity is 1 because one-hot vectors
    ent_map = {e: 1 for e in entities if e in vocabulary}
    ent_map_list: List[dict] = [ent_map]
    vectorizer = DictVectorizer(sparse=False)
    # this encodes all numbers as one-hot arrays of binary data, again becsuse NN
    one_hot = vectorizer.fit_transform(ent_map_list)
    assert vectorizer.inverse_transform(one_hot) == ent_map_list
    return one_hot, vectorizer


def _vectorize_by_entities(overview: Overview, nlp: NLP) -> Tuple[OneHot, Vectorizer]:
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

    # TODO: normalize/clean `entities`

    one_hot, vectorizer = _make_entity_vectorizer(entities, "models/vocabulary.csv")

    return one_hot, vectorizer


def _vectorize(overview: Overview, nlp: NLP) -> Tuple[OneHot, Vectorizer]:
    """
    Returns the input transformed into one-hot vectors via DictVectorizer
    """
    return _vectorize_by_entities(overview, nlp)


def _is_good_one_hot_for_dict_vec(oh: OneHot, dv: DictVectorizer) -> bool:
    """
    TODO: ...
    """
    oh_is_list = type(oh) == list
    oh_is_numpy = type(oh) == np.ndarray
    any_of_these = oh_is_list or oh_is_numpy
    both_of_these = len(oh) > 0 and len(oh[0]) > 0
    is_good = any_of_these and both_of_these
    return is_good


def _inverse_vectorize(one_hot: OneHot, vectorizer: Vectorizer) -> List[Any]:
    """
    TODO: return something unambiguous
    """
    if isinstance(vectorizer, DictVectorizer):  # pyre-ignore[25]
        msg = "bad one hot"
        assert _is_good_one_hot_for_dict_vec(one_hot, vectorizer), msg
        return vectorizer.inverse_transform(one_hot)
    else:
        raise NotImplementedError("non-DictVectorizer not yet implemented.")


def _predict_director_vec(
    input_vector: VectorizedInput, filename: str = "entities_predict_director.h5"
) -> VectorizedOutput:
    """
    Returns the predictions of the `entities_predict_director.h5` model
    """
    model = load_model(filename)
    output: VectorizedOutput = model.predict(input_vector)
    return output


def _predict_director(overview: Overview, nlp: NLP) -> str:
    """
    Returns a director prediction from the overview.
    """
    mi, mv = _vectorize(overview, nlp)
    model_input: VectorizedInput = mi
    model_vectorizer: DictVectorizer = mv
    model_one_hot: VectorizedOutput = _predict_director_vec(model_input)
    predictions: List[Any] = _inverse_vectorize(model_one_hot, model_vectorizer)
    model_output: str = str(predictions[0])
    return model_output


def producer(
    overview: Overview, nlp: Optional[NLP] = None, use_large=False
) -> Suggestions:
    """A robot movie producer.

    Args:
        overview: an [`Overview`](#labs.lab1.Overview) string about the movie.
        TODO: nlp...use_large...

    Returns:
        A dictionary of [`Suggestions`](#labs.lab1.Suggestions).
    """
    model_name = "en_core_web_lg" if use_large else "en_core_web_sm"
    nlp: NLP = spacy.load(model_name) if nlp == None else nlp

    if not _is_spacy(nlp):
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
