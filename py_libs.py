# import random
from random import randrange, random # Considered best practice.
# from random import * # If you want all the methods inside random.
import math
import time

print('///////////////////////RANDOM///////////////////////////')
time.sleep(1)
print(random())
time.sleep(0.5)
print(randrange(10, 44))

# Libraries
# They come built in
# You just need to import.

# They are maintained by python organisation
# They are very stable and considered vanilla python.
# check the documentation for more
# https://docs.python.org/3/library/random.html

print('///////////////////////MATHS///////////////////////////')
time.sleep(2)
num = 24.64
print(math.ceil(num))
time.sleep(0.31)
print(math.floor(num))
time.sleep(0.51)
print(math.pi)