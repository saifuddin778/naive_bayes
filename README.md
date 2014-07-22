naive_bayes
===========

A ready-made Naive Bayes classification model for binary vectors. More info [here](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)

###Usage:
A simple example usage is given below:
```python
>>> from naive_bayes import naive_bayes
>>> data = [('customer', [1,1,1,0]), ('not_customer', [1,0,1,0]), ('potential_customer', [1,1,1,1])....('some_class', [some_vector])]
>>> features = ['employed', 'married', 'has_children', 'has_car']
>>> p = naive_bayes(data, features)
>>> p.process()
>>> p.predict(vector, key_only=True/False)
>>> ...
```
Here is the list of all the parameters for the parent `naive_bayes` method:
* `data` - a 2D dataset containing samples in this format: `('class', vector)`
* `features` - a 1D array containing all the feature labels as 'strings'
And the predictor method:
* `vector` - input vector to classify (provide either as a list or as a tuple)
* `key_only` - setting this to `True` returns only the predicted label, and to `False` returns probabilities for all the classes.
