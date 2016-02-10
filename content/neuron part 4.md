Title: Neural Networks Part 4: 
Date: 2016-1-06 10:20
Category: machine learning
Tags: neural networks, machine learning, coding
Authors: Eric Carmichael
Summary: Every month we participate in the [Developer Co-op](http://meetup.com/dev-coop/) meetup in Liberty Lake, Washington. This month we had part 4 of learning neural networks. This session we didn't add much new behavior, but tied things nicely together in a `Trainer` class.


This session we didn't add much new behavior, but tied things nicely together in a `Trainer` class and added 
nicer output to track the current error.


Here's an example usage of the new class:

```python
OR_GATE = (
    # (input, output)
    ([0, 0], [0]),
    ([1, 0], [1]),
    ([1, 1], [1]),
    ([0, 1], [1]),
)

network = Network([2, 1])
trainer = Trainer(network, OR_GATE)
trainer.train()
```

When run this outputs:
```
$ python neural_network_with_connections.py
Epoch  0 error = 0.0976866206323
Epoch  1000 error = 0.0175155899397
Epoch  2000 error = 0.00643827724377
Epoch  3000 error = 0.00322907067653
Epoch  4000 error = 0.00191442445754
Epoch  5000 error = 0.00125869287738
Epoch  6000 error = 0.000887481325948
Epoch  7000 error = 0.000657994207371
Epoch  8000 error = 0.000506639806887
Epoch  9000 error = 0.000401750116057
Epoch  10000 error = 0.000326163968267
```

Notice as we train the `error` gets lower and lower, our neural network is learning!

Such cool stuff, come checkout the [Dev Coop meet up](http://www.meetup.com/dev-coop/) in Liberty Lake, WA!




