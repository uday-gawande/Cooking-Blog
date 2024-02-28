import random
import numpy as np
import matplotlib.pyplot as plt
times = int(input())
x = []
y = []
for i in range(times):
    n = random.randint(1,50)
    t = random.randint(1,50)
    x.append(n)
    y.append(t)
plt.plot(x, y, 'ro')

def connectpoints(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

connectpoints(x,y,0,1)
connectpoints(x,y,2,3)

plt.axis('equal')
plt.show()