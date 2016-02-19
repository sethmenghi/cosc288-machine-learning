"""
dataset.py.

Holds the DataSet class.
"""
from __future__ import absolute_import

import logging

from .attributes import Attributes

from . import exceptions
from .example import Examples


class DataSet(object):
    """Implements a class for a data set for machine-learning methods."""

    _name = None
    _attributes = None
    _examples = None

    def __init__(self, attributes=None, name=None):
        """Constructor, default attributes argument=None."""
        self._attributes = attributes
        self._examples = Examples(self._attributes)
        self._name = name

    @property
    def attributes(self):
        """Getter for _attributes."""
        return self._attributes

    @property
    def examples(self):
        """Return self._examples."""
        return self._examples

    @property
    def has_nominal_attributes(self):  # noqa
        return self._attributes.has_nominal_attributes

    def has_numeric_attributes(self):  # noqa
        return self._attributes.has_numeric_attributes

    def add(self, example=None, dataset=None):
        """Add example or dataset to current dataset."""
        if example is None and dataset is None:
            e = "No arguments in add method."
            raise exceptions.LogicError(e)
        if dataset:
            self._add_dataset(dataset)
        if example:
            self._add_example(example)

    def _add_dataset(self, dataset):
        """Add dataset to current dataset."""
        for example in dataset.examples:
            self._examples.append(example)
        for attribute in dataset.attributes:
            self.attributes.add(attribute)

    def _add_example(self, example):
        """Add example to current dataset."""
        self._examples.append(example)

    def __str__(self):
        """Return string representation of dataset as would look in file."""
        string = "@dataset %s\n\n" % self._name
        string = string + str(self.attributes) + "\n"
        string = string + "@examples\n\n"
        string = string + str(self.examples)
        return string
