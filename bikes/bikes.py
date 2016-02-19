# -*- coding: utf-8 -*-
#
# Name: Seth menghi
# E-mail Address: swm36@georgetown.edu
# Platform: MacOS
# Language/Environment: python
#
# In accordance with the class policies and Georgetown's Honor Code,
# I certify that, with the exceptions of the class resources and those
# items noted below, I have neither given nor received any assistance
# on this project.
#

from .traintestsets import TrainTestSets

t = TrainTestSets('-t ..data/bikes.mff')
print(t)
