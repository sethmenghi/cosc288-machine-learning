"""
TrainTestSets.py.

Holds the DataSet class.
"""
from __future__ import absolute_import

import logging

from .attributes import Attributes

from . import exceptions
from .example import Examples
from .dataset import DataSet


class TrainTestSets(object):

    _test = None
    _train = None

    def __init__(self, args=None):
        if args:
            self.set_options(args)
            self.main()

    @property
    def test_set(self): # noqa
        return self._test

    @property
    def train(self):  # noqa
        return self._train

    def set_train(self, train):
        self._train = train

    def set_test(self, test):
        self._test = test

    def set_options(self, options):
        args = options.split(" ")
        i = 0
        if len(args) < 2:
            e = "Incorrect number of arguments."
            raise exceptions.LogicError(e)
        while(args[i] != "-t"):
            if i == len(args):
                e = "Incorrect number of arguments."
                raise exceptions.LogicError(e)
            i += 1
        self.test_path = args[i + 1]

    def __str__(self):
        if self.test_set and self.train:
            return str(self.test_set) + "\n" + str(self.train)
        elif self.test_set:
            return str(self.test_set) + "\n"
        elif self.train:
            return str(self.train)
        else:
            return "No data loaded."

    def main(self):
        with open(self.test_path) as f:
            attributes = Attributes()
            at_examples = False
            for line in f:
                line = line.replace("\n", "")
                if '@dataset' in line:
                    l = line.split(" ")
                    name = l[1]
                if '@attribute' in line:
                    attributes.parse(line)
                if '@example' in line:
                    at_examples = True
                    examples = Examples(attributes)
                    d = DataSet(name=name, attributes=attributes)
                    continue
                if at_examples and len(line) > 1:
                    examples.parse(line)
        d._examples = examples
        self.set_test(d)
