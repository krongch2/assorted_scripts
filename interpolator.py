import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RegularGridInterpolator

def create_data():

    def f(x, y):
        return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

    x = np.linspace(0, 1, 10)
    y = np.linspace(0, 1, 20)
    data = f(*np.meshgrid(x, y, indexing='ij', sparse=True))
    return data

def reshape_data(old_data, new_dimension):
    x = np.linspace(0, 1, old_data.shape[0])
    y = np.linspace(0, 1, old_data.shape[1])
    rgi = RegularGridInterpolator((x, y), old_data)
    new_x = np.linspace(0, 1, new_dimension[0])
    new_y = np.linspace(0, 1, new_dimension[1])
    points = np.meshgrid(new_x, new_y, indexing='ij', sparse=False)
    flat = np.array([m.flatten() for m in points]).T
    new_data = rgi(flat).reshape(new_dimension[0], new_dimension[1])
    return new_data

old_data = create_data()
new_data = reshape_data(old_data, (500, 1000))

plt.subplot(121)
plt.imshow(old_data.T, extent=(0, 1, 0, 1), origin='lower')
plt.title('original')

plt.subplot(122)
plt.imshow(new_data.T, extent=(0, 1, 0, 1), origin='lower')
plt.title('interpolated')
plt.show()