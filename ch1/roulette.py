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
        wheel[i] = cumProb
    return wheel


wheel = roulette_wheel(
    [
        ("dog food",0.7),
        ("fish food",0.1),
        ("bird food",0.1),
        ("small rodent food",0.05),
        ("reptile food",0.05)
    ])

for i in range(1000):
    r = math.floor(random.random()*len(wheel))
    print(wheel[int(r)])