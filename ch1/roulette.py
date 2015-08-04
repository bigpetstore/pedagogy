__author__ = 'jayvyas'
import random
import math

def roulette_wheel(model):
    wheel = [None] * len(model)
    cumProb = 0.0
    for i in range(len(model)):
        (item, prob) = model[i]
        print(i,item,prob)
        cumProb += prob
        wheel[i] = (item, cumProb)
    return wheel


## Corresponds to the following roulette wheel...
## [.1,.8, .9, .95, 1.0]
wheel = roulette_wheel(
    [
        ("fish food",0.1),
        ("dog food",0.7),
        ("bird food",0.1),
        ("small rodent food",0.05),
        ("reptile food",0.05)
    ])

### Now , we grab the bin that binds a random number.
### For example
### Random number = .1 ---> fish food.
### Random number = .6 ---> dog food,
### And so on...
for i in range(1000):
    r = random.random()
    print([it for (it, cp) in wheel if cp >= r ][0])