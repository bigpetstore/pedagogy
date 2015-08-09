__author__ = 'jayvyas'
import random
import math

#558986-AFCN6-EJ927-WAEZ1-D95LF-BTAY4

def roulette_probability_boundaries(model):
    """
    Wheel returns a list of (item, probability) tuples with additive probability boundaries.
    Input: [("fish food", .1), ("dog food", .1), ("cat food", .8)]
    Output: [("fish food", .1 ), ("dog food", .2), ("cat food", .8)]
    """
    wheel = [None] * len(model)
    cumProb = 0.0
    for i in range(len(model)):
        (item, prob) = model[i]
        print(i, item, prob)
        cumProb += prob
        wheel[i] = (item, cumProb)
    return wheel

## Corresponds to the following roulette wheel...
## [.1,.8, .9, .95, 1.0]
wheel = roulette_probability_boundaries(
    [
        ("fish food",0.1),
        ("dog food",0.7),
        ("bird food",0.1),
        ("small rodent food",0.05),
        ("reptile food",0.05)
    ])


def samples(n):
    """
    Generate 100 products and print them to std out.
    Input: Integer number of samples
    """
    l=[]
    for i in range(n):
        r = random.random()
        # Sequential scan of the roulette wheel.
        # pick the first probability >= to the random #.
        product = [it for (it, cp) in wheel if cp >= r ][0]
        l.append(product)
    return l

def exersize1():
    samples(1000)

def exersize2():
    s10 = samples(10)
    s100 = samples(100)
    s1000 = samples(1000)

    expected_dog_food=10*.7
    actual_dog_food=len([s10 for it in s10 if it == "dog food"])
    print(actual_dog_food, expected_dog_food)
    print("10 samples, Dog food accuracy = " + str(100 - math.fabs( (actual_dog_food-expected_dog_food) / expected_dog_food)))

    expected_dog_food=100*.7
    actual_dog_food=len([s100 for it in s100 if it == "dog food"])
    print(actual_dog_food, expected_dog_food)
    print("100 samples, Dog food accuracy = " + str(100 - math.fabs( (actual_dog_food-expected_dog_food) / expected_dog_food)))

    expected_dog_food=1000*.7
    actual_dog_food=len([s1000 for it in s1000 if it == "dog food"])
    print(actual_dog_food, expected_dog_food)
    print("1000 samples, Dog food accuracy = " + str(100 - math.fabs( (actual_dog_food-expected_dog_food) / expected_dog_food)))

def exersize3():

    p = .9999
    dfp=[]
    minP=(1, "")
    maxP=(0, "")
    # Sample 100 items, 1000
    while len(dfp) < 1000:
        # Sample 10 products from the distribution.
        sample = samples(10)
        # Below, we implement the multinomial probability function
        # p = ((x1+x2+...)!/(x1!x2!x3!))*(r1^o1)*(r2^o2)...
        cp = 1 # Reset p to 1.
        df = len([it for it in sample if it == "dog food"])
        ff = len([it for it in sample if it == "fish food"])
        bf = len([it for it in sample if it == "bird food"])
        srf = len([it for it in sample if it == "small rodent food"])
        rf = len([it for it in sample if it == "reptile food"])
        cp=cp * math.pow(.7, df)/math.factorial(df)
        cp=cp * math.pow(.1, ff)/math.factorial(ff)
        cp=cp * math.pow(.1, bf)/math.factorial(bf)
        cp=cp * math.pow(.05, srf)/math.factorial(srf)
        cp=cp * math.pow(.05, rf)/math.factorial(rf)
        cp=cp * math.factorial(df+ff+bf+srf+rf)
        if cp < minP[0]:
            print (cp,"<",minP)
            minP = (cp, sample)
        if cp > maxP[0]:
            maxP = (cp, sample)

        if maxP[0]!= 1 and maxP[0] > minP[0]*20000:
            print("...................................")
            print minP
            print maxP
            print("...................................")
            if len([it for it in maxP[1] if it == "dog food"]) > 6:
                print "Got > 6 dog foods in the high probability sample....Test passes."
            else:
                print "Failed.  Expected high number of dog foods in high probability sample!"

            return

exersize3()
