Title: Neural Networks Part 1: The Neuron
Date: 2015-11-20 10:20
Category: machine learning
Tags: neural networks, machine learning, coding
Authors: Eric Carmichael
Summary: This is the first part of a many part series about creating Neural Networks from the ground up. We start with an individual neuron and it's connections!


Last month we did the first part of a many part series about creating Neural Networks
from the ground up. I'll briefly cover some of what Levi went over but I won't do it
justice! You'll have to come to the meet-ups to get the full effect.


The first session will cover the most basic piece of a neural network: the neuron. Full
neural networks consist of a few more parts, but they are all there to glue together
the basic neuron.

Neurons in artifical neural networks

 - connections to other neurons via memory pointers
 - fires when connections meet some threshold number
 - digital

Real neurons

 - branching dendrites to receive chemical signals
 - axon projection to conduct a nerve signal
 - analog


![Neuron](images/neuron.png)


First we started by making one neuron and activating it. Activation functions
take some input and smooth it out. Normalizing our inputs from 0...1 makes it
easier to work with in the neural network.

We ended up using the Rectifier activation function:

```1 / (1 + math.exp(-x))```

After completing the activation function, then we connected the neurons to each
other.






### Bonus: Python tests

In Python a tests are many functions run one after the other checking a suite of software for errors.
These functions have simple assertions in them gauranteeing the behavior of a piece of code.
If the assertion fails, the test fails.

The assertion is a condition that evaluates to a boolean, like "assert that when I add 1 + 1 I get the result 2."

```python
def test_add_one_plus_one_equals_two():
    assert 1 + 1 == 2
```

We can use tests to help maintain our code and get rid of unforeseen bugs. For example, if you
are working on a website with 10,000 lines of code... how can you be sure when you touch *this thing over here*
it doesn't break *that thing over there*? Well! You write about twice as much code making sure the original
code does what it's supposed to by asserting exactly how it should behave.


[Here's](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/python/neural_network_with_connections_tests.py) a test from the Python example:

```python
def test_connection_adds_to_incoming_and_outgoing_arrays(self):
    # Setup our neurons and connections
    neuron = Neuron(input=0)
    neuron_2 = Neuron()
    neuron.connect_child(neuron_2, weight=1)

    # Let's make sure that there's at least one connection
    # from our neuron to the next neuron
    assert [neuron == connection.neuron for connection in neuron_2.incoming_neurons].count(True) == 1

    # And the same goes for the other neuron, make sure
    # it's connected to us
    assert [neuron_2 == connection.neuron for connection in neuron.outgoing_neurons].count(True) == 1
```

If the above test passes, we can be sure our connection was made properly!


### Example neuron code

 * [elixir](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/elixir/neuron.exs)
 * [javascript ES5](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/es5/neuronet.js)
 * [javascript ES7](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/es7/Neuron.js)
 * [ruby](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/ruby/karmen_neural_network.rb)
 * [python](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/python/neural_network_with_connections.py)
 * [python tests](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/python/neural_network_with_connections_tests.py)

Stay tuned for part 2 next month! We'll be layering and maybe even training our neurons!
