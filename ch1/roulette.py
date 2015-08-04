__author__ = 'jayvyas'
import random


def roulette_wheel(model):

    wheel = []
    cumProb = 0.0
    for item, prob in model.items():
        cumProb += prob
        print(cumProb)
        bin = (item, cumProb)
        wheel.append(bin)
    r = random.random()
    previous = None
    for item, upperbound in wheel:
        if upperbound >= r:
            return previous
        previous = item


print(roulette_wheel({"age":.25}))