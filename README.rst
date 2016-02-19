===============================
cosc-288-bikes
===============================

Machine learning  project written for COSC-288 Machine Learning. 

* Documentation: https://cosc-288-bikes.readthedocs.org.

How To
--------

Install bikes package:

$ cd cosc-288-bikes
$ pip install -r requirements_dev.txt 
$ python setup.py install

Run from command line:

$ bikes -t dest/to/file

Create own script:

..code:: python

    raw_data = "-t example_file.mff"
    testset = TrainTestSet(raw_data)
    print(testset)

