import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100,101):
    x = x + [n]

# Create y values
y = [n*n - 3 for n in x]

print(x)

# Print chart
plt.plot(x, y)
plt.show()