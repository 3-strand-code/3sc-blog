Title: Neural Networks Part 1: The Neuron
Date: 2015-11-20 10:20
Category: machine learning
Tags: neural networks, machine learning, coding
Authors: Eric Carmichael
Summary: This is the first part of a many part series about creating Neural Networks from the ground up. We start with an individual neuron and it's connections!


Last month we did the first part of a many part series about creating Neural Networks
from the ground up. I'll briefly cover some of what Levi went over but I won't do it
justice! You'll have to come to the meet-ups to get the full effect.


What makes a neuron <cont>
 - connected through axons
 - fires with threshold


<img src="https://unsplash.it/700/300?image=0">


How is it similar to the brain <cont>


First we started by making an individual neuron and






Connections, weights <cont>




Activation functions






### Bonus! Python tests

In Python a test is a function with some kind of assertion. The assertion is
a condition that evaluates to a boolean, the most simple example might be:

```python
def test_add_one_plus_one_equals_two():
    assert 1 + 1 == 2
```

We can use tests to help maintain our code and get rid of unforeseen bugs. <cont>



Here's an actual test from my [neuron example](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/python/neural_network_with_connections_tests.py):

```python
def test_connection_adds_to_incoming_and_outgoing_arrays(self):
    # Setup our neurons and connections
    neuron = Neuron(input=0)
    neuron_2 = Neuron()
    neuron.connect_child(neuron_2, weight=1)

    # Let's make sure that there's at least one connection from our neuron to the next neuron
    assert any(neuron == connection.neuron for connection in neuron_2.incoming_neurons)

    # And the same goes for the other neuron, make sure it's connected to us
    assert any(neuron_2 == connection.neuron for connection in neuron.outgoing_neurons)
```

If the above test passes, we can be sure our connections were made properly.


### Example neurons

 * [elixir](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/elixir/neuron.exs)
 * [javascript ES5](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/es5/neuronet.js)
 * [javascript ES7](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/es7/Neuron.js)
 * [ruby](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/ruby/karmen_neural_network.rb)
 * [python](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/python/neural_network_with_connections.py)
 * [python tests](https://github.com/dev-coop/neural-net-hacking-examples/blob/master/python/neural_network_with_connections_tests.py)

Stay tuned for part 2 next month! We'll be layering and maybe even training our neurons!
