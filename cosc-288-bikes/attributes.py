"""
attributes.py.

Holds the Attributes class.
"""
from __future__ import absolute_import

import logging

from . import exceptions
from .attribute import NominalAttribute, NumericAttribute


logger = logging.getLogger(__name__)


class Attributes(object):
    """Stores information for attributes for data sets."""

    attributes = []
    _has_nominal_attribute = False
    _has_numeric_attribute = False
    _classindex = 0

    def __iter__(self):
        """Make iterable."""
        return iter(self.attributes)

    def __getitem__(self, val):
        """Allow for indexing."""
        return self.attributes[val]

    @property
    def size(self):
        """Return number of attributes."""
        return len(self.attributes)

    @property
    def classindex(self):
        """Return the class index attribute."""
        return self._classindex

    @property
    def has_numeric_attribute(self):
        """Return True if self.attributes has numeric attribute."""
        return self._has_numeric_attribute

    @property
    def has_nominal_attribute(self):
        """Return true if self.attributes has nominal attribute."""
        return self._has_nominal_attribute

    def add(self, attribute):
        """Add a new attribute to this set of attributes."""
        self.attributes.append(attribute)

    def parse(self, line):
        """Parse a string attribute line."""
        if '@attribute' in line:
            attributes = line.split(" ")
            if attributes[2] == 'numeric':
                attribute = self._parse_numeric_attribute(attributes)
            else:
                attribute = self._parse_nominal_attribute(attributes)
            self.add(attribute=attribute)
            logger.debug('Added attribute %s' % attribute)
        else:
            e = "Line is not an attribute."
            raise exceptions.LogicError(e)

    def _parse_nominal_attribute(self, attributes):
        if len(attributes) < 2:
            e = "Nominal attribute with no domain."
            raise exceptions.LogicError(e)
        attribute = NominalAttribute(name=attributes[1])
        for value in attributes[2:]:
            attribute.add_value(value=value)
        if not self.has_nominal_attribute:
            self._has_nominal_attribute = True
        return attribute

    def _parse_numeric_attribute(self, attributes):
        attribute = NumericAttribute(name=attributes[1])
        if not self.has_numeric_attribute:
            self._has_numeric_attribute = True
        return attribute
