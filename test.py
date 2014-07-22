from naive_bayes import naive_bayes

def test_naive_bayes():
    #just an example data
    #in real world, should be more sophisticated and more detailed dataset.
    data = [
            ('saif', [1,1,0]),
            ('ali', [1,1,1]),
            ('kamran', [0,1,1]),
            ('ali', [1,1,1]),
            ('saif', [0,1,0]),
            ('kamran', [1,0,1])
        ]
    features_set = ['low', 'med', 'high']
    p = naive_bayes(data, features_set)
    p.process()
    for a in data:
        print a[0], p.predict(a[1], key_only=True)

#call
test_naive_bayes()
    
