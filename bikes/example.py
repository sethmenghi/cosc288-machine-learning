"""
example.py.

Holds the Example and Examples classes.
"""
from __future__ import absolute_import

import logging

from . import exceptions


class Example(object):
    """Stores the attribute values of an example.

    Numeric values are stored as is. Nominal values are stored as doubles
    and are indices of the value in the attributes structure.
    """

    _n = 0

    def __init__(self, n=0):
        """Explicit constructor, `n` is the number of examples."""
        self._n = n
        self._values = []

    def __str__(self):
        """String representation fo example."""
        return self._n

    @property
    def values(self):  # noqa
        return self._values

    def append(self, val):
        """Append a value onto self._values."""
        self._values.append(val)
        self._n = len(self._values)


class Examples(object):
    """Stores examples for data sets for machine learning."""

    _attributes = None

    def __init__(self, attributes=None):
        """Constructor, `attributes` (default=None), Attributes() object."""
        self._attributes = attributes
        self._examples = []

    def parse(self, line):
        """Given the attributes structure, parses into Examples."""
        values = line.split(" ")
        example = Example()
        for i, v in enumerate(values):
            if i >= self._attributes.size:
                e = "Out of bounds for val %s in Examples.parse." % v
                raise exceptions.LogicError(e)
            if self._attributes[i].type == 'Numeric':
                val = v
            elif self._attributes[i].type == 'Nominal':
                val = self._attributes[i].index(v)
            else:
                e = "No attribute type for %s in Examples.parse()" % self._attributes[i]
                raise exceptions.LogicError(e)
            example.append(val)
        self._examples.append(example)

    def __str__(self):
        """Return string reprsentation of Examples."""
        # self._examples.values
        string = ""
        for e in self._examples:
            for i, v in enumerate(e.values):
                if self._attributes[i].type == 'Nominal':
                    string = string + self._attributes[i].domain[v]
                else:
                    string = string + v
                if i == len(e.values) - 1:
                    string = string + "\n"
                else:
                    string = string + " "
        return string
