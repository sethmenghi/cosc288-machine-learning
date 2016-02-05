"""
attributes.py.

Holds the Attributes class.
"""
from __future__ import absolute_import

import logging

from .attribute import NumericAttribute, NominalAttribute
from . import exceptions


logger = logging.getLogger(__name__)


class Attributes(object):
    """Stores information for attributes for data sets."""

    attributes = []
    has_nominal_attribute = False
    has_numeric_attribute = False
    _classindex = 0

    def __iter__(self):
        """Make iterable."""
        return iter(self.attributes)

    def __getitem__(self, val):
        """Allow for indexing."""
        return self.attributes[val]

    @property
    def classindex(self):
        """Return the class index attribute."""
        return self._classindex

    def add(self, attribute):
        """Add a new attribute to this set of attributes."""
        self.attributes.append(attribute)




