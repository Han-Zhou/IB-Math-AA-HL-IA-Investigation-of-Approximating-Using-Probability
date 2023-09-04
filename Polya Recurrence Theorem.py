import matplotlib.pyplot as plt
import random
import math
import numpy as np


collection = []
bins = []




def step_counter(i):
   sn = 0
   stepsList = [-1, 1]
   for j in range(i):
       x = random.choice(stepsList)
       sn = sn + x
   collection.append(sn)
   # if sn == 0:
   #     p += 1



def recurrence_experiment(i, j):
   for k in range(i):
       step_counter(j)


   count0 = (collection.count(0))
   print(count0)

   experimentpi = ((i/count0)**2) / (j/2)
   print(experimentpi)
   error = abs(((math.pi - experimentpi) / math.pi))
   print(error)
   s = -1 * j
   for l in range(2 * j):
       bins.append(s)
       s += 1


recurrence_experiment(10000 , 500)             # i = population size, j = 2n
plt.hist(collection, bins=bins)
plt.xlabel("position S2n after 2n steps")
plt.ylabel("frequency for each S2n")
plt.show()


