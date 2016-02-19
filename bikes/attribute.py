"""
attributes.py.

Holds the Attribute, NominalAttribute, and NumericAttribute classes.
"""
from __future__ import absolute_import

import logging

from . import exceptions


logger = logging.getLogger(__name__)


class Attribute(object):
    """Stores information for an attribute."""

    domain = []
    _type = None

    def __init__(self, name=None):
        """Constructor for the Attribute object.

        Args:
        name (str): name of the attribute.
            default=None
        """
        self._name = name
        self.domain = []

    @property
    def name(self):
        """Return name attribute."""
        return self._name

    @name.setter
    def name(self, name):
        """Set the name attribute to `name`."""
        self._name = name

    @property
    def type(self):
        """Return attribute type."""
        return self._type

    def __str__(self):
        """The string repr. of an Attribute is it's name."""
        string = "@attribute %s" % self.name
        if self.type == 'Nominal':
            for v in self.domain:
                string = string + " %s" % v
        elif self.type == 'Numeric':
            string = string + " %s" % 'numeric'
        return string

    def __repr__(self):
        """Representation of the object."""
        return (self.name, self.domain)


class NominalAttribute(Attribute):
    """An attribute with nominal representation."""

    _type = 'Nominal'
    domain = []

    @property
    def size(self):
        """Return size attribute."""
        return len(self.domain)

    def __iter__(self):
        """Make iterable."""
        return iter(self.domain)

    def __getitem__(self, val):
        """Allow for indexing."""
        return self.domain[val]

    def add_value(self, value):
        """Add a new nominal value to the domain of this nominal attribute."""
        try:
            if value not in self.domain:
                self.domain.append(value)
        except:
            e = 'Error with adding value: %s.' % value
            raise exceptions.LogicError(e)

    def index(self, value):
        """Return the index of the `value` for this nominal attribute."""
        for i, k in enumerate(self):
            if k == value:
                return i


class NumericAttribute(Attribute):
    """Store information for a numeric attribute.

    A numeric attribute has a name. Its domain is the real numbers.
    """

    _type = 'Numeric'
    domain = ['numeric']
    pass
