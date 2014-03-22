from __future__ import division

# In-built libraries
import sys
import random
import math

# Messy, but necessary for the any function random distributor
from numpy import *

# External libraries
import numpy as np

# rnd = random.SystemRandom()
## Use system produced random numbers

def produce_randoms(num):
    # Produce num evenly distributed random numbers 

    print "Producing {} uniformly distributed random numbers... ".format(num),
    even = np.random.uniform(0,2,num)
    print "done"

    return even

def display_progress(current, target):
    # Displays progress bar showing how close current is to target

    percentage = 100*(current+1)/target

    if percentage%1 == 0:
        sys.stdout.flush()
        sys.stdout.write("\r\t\t\t\t\t["+"#"*int(percentage)+" "*int(100 - percentage)+"]"+"(%3d%%)"%(percentage))
        if percentage == 100:
            print

    return 0

def string_to_func(string):
    # Turn string taken from argument into function to produce random distribution around

    func = lambda x: eval(string)

    return func

def reject_accept_fixed(num, verb, func_str, range):
    # Use reject-accept method to produce fixed number of random numbers
    # distributed as per user-defined function

    func = string_to_func(func_str)

    # The 5 is just because chance if I produce 9 times the number I need then
    # chances are at that I'll get at least num out (specifically, 1*num produces
    # about 0.6*num out, so 9*num is insufficient in ~1% of all runs). There is a 
    # trade-off here in terms of efficiency and processing time.
    first = np.random.uniform(range[0],range[1],9*num)
    second = np.random.uniform(0,func(range[1]),9*num)
    dist = []

    criterion = second < func(first)

    print "Producing fixed number {} of random user-distributed numbers "\
          "via reject-accept method...".format(num),

    if verb:
        print
        print "Random numbers produced: ",

    for i in range(len(criterion)):
        if criterion[i]:
            dist.append(first[i])
            if len(dist) >= num:
                print "done"

                return dist 
        if verb:
            display_progress(len(dist),num)

    return False

def reject_accept(num, verb, func_str, range):
    # Use reject-accept method to produce random numbers distributed as 
    # general user-defined function in user-defined range

    func = string_to_func(func_str)

    first = np.random.uniform(range[0],range[1],num)
    second = np.random.uniform(0,func(range[1]),num)
    sinusoid = []

    criterion = second < func(first)

    print "Producing random user-distributed numbers using reject-accept method...",

    if verb:
        print
        print "Random numbers produced:",

    for i in range(num):
        if criterion[i]:
            sinusoid.append(first[i])
        if verb:
            display_progress(i+1,num)

    print "done"

    if verb:
        print "{} random numbers produced.".format(len(sinusoid))

    return sinusoid
