import numpy as np

temperatures = np.array([
    29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
    12.6, 49.9, 38.6, 31.3, 9.2, 22.2
]).reshape(2, 2, 3)

print(temperatures.shape)
print(temperatures)
print(np.swapaxes(temperatures, 1, 2))