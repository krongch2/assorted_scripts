import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a 1D vector named t and 2D arrays named vx, vy, x, and y to hold the state variables, of size 90 x 1001.
nt = 1001
t = np.linspace(0, 10, nt)
vx = np.zeros((90, nt))
vy = np.zeros((90, nt))
x = np.zeros((90, nt))
y = np.zeros((90, nt))

# 2.  Store the angles from 1 to 90 degrees as radians in a variable called radians.
# Use this to initialize the state variables for vx and vy.
m = 90   # angles to fire at
angles = np.arange(m) + 1
radians = angles * np.pi / 180

# 3.  Define properties like gravity, Callista's surface area, and Callista's mass, and any other parameters you may need as they come up.
A = 0.8  # m^2
g = 9.8  # m/s^2
mass = 65 # kg
C = 1.4 # unitless
rho = 1.225 # kg/m^3
initial_height = 5 # m
initial_velocity = 70 # m/s

# 4.  At this point, you should have defined t, x, y, vx, vy, radians, and the properties you need.  Now, initialize the starting condition in each array:
for i in range(m):
    y[i][0]  = initial_height
    vx[i][0] = initial_velocity * np.cos(radians[i])
    vy[i][0] = initial_velocity * np.sin(radians[i])  # (see "Angles" above)

# 5.  Now you are ready to begin the simulation proper.  You will need two loops, one over every angle, and one over every time step for that angle's launch.
for i in range(m):  # loop over each angle
    for j in range(1, nt):  # loop over each time step
        v = np.sqrt(vx[i, j - 1]**2 + vy[i, j - 1]**2)

        # calculate the acceleration including drag
        a = (0.5 * rho * C * A / mass) * v**2
        if v == 0:
            ax = 0
            ay = 0
        else:
            ax = -a * vx[i, j - 1] / v
            ay = -a * vy[i, j - 1] / v - g

        dt = t[j] - t[j - 1]
        vx[i, j] = vx[i, j - 1] + ax * dt
        vy[i, j] = vy[i, j - 1] + ay * dt

        # calculate the change in position at time ts
        # using the current velocities (vx[ i ][ j ]) and the previous positions (x[ i ][ j-1 ])
        x[i, j] = 0.5 * ax * dt**2 + vx[i, j] * dt + x[i, j - 1]
        y[i, j] = 0.5 * ay * dt**2 + vy[i, j] * dt + y[i, j - 1]

        # check that the location isn't below the ground
        if y[i, j] <= 0 and j != 0:
            vx[i, j] = 0
            vy[i, j] = 0
            x[i, j] = x[i, j - 1]
            y[i, j] = 0

# 6. The purpose of these calculations was to show which angle yielded the farthest distance.
# Find this out and store the result in a variable named best_angle.
best_angle_idx = x[:, -1].argmax()
fig, ax = plt.subplots(nrows=1, ncols=1)
for i in list(range(0, m, 10)) + [best_angle_idx]:
    if i == best_angle_idx:
        ax.plot(x[i, :], y[i, :], c='red', label='best_angle = test')
    else:
        ax.plot(x[i, :], y[i, :], c='blue')
ax.axhline(y=0, c='#2f2f2f')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.tight_layout()
plt.show()
