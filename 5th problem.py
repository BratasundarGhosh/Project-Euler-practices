# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible divisible with no remainder by all of the numbers from 1 to 20?
import math
num = []
for i in range(1, 20):
    num.append(i)
print(math.lcm(*num))