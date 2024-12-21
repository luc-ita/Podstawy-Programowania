import matplotlib.pyplot as plt
import math

x = list(range(0, 361))

y = [math.sin(math.radians(angle)) for angle in x]

plt.plot(x, y)
plt.show()