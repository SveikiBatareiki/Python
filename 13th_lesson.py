import requests
from collections import Counter
import matplotlib.pyplot as plt

fig = plt.figure()

x = list(range(11))
y = [n**2 for n in x]
y2 = [n+5 for n in y]
y3 = [n+15 for n in y]
plt.bar(x, y)
plt.plot(x, y2)
plt.scatter(x, y3)
plt.savefig("../data/squares.png")

plt.show()