import numpy as np
import matplotlib.pyplot as plt
import time

xo = 0
yo = 0
velocity = input("Enter the initial velocity (must be a positive integer): ")
theta = input("Enter the initial angle, between 0 and 90: ")
ndots = input("Enter the number of timesteps: ")
theta = np.deg2rad(int(theta))
g = 9.8

# calculate tf

vx = float(velocity) * np.cos(theta)
vy = float(velocity) * np.sin(theta)
print("Horizontal and vertical components of velocity are: " + str(vx), str(vy))
tf = (vy / g) * 2
print("Final time is: " + str(tf))

# set time interval over which to plot
t_array = np.linspace(0, tf, int(ndots))

# initialize arrays on which to plot x and y
xis = np.zeros(len(t_array))
yis = np.zeros(len(t_array))

# feed values using loop
for ti in np.arange(len(t_array)):
    xi = (vx * t_array[ti])
    yi = (vy * t_array[ti]) - ((0.5)*g*t_array[ti]**2)
    xis[ti] = xi
    yis[ti] = yi

# feed values into xis and yis

plt.ion()
for i in np.arange(len(xis)):
    xi = xis[i]
    yi = yis[i]
    plt.xlim(-0.5, max(xis))
    plt.ylim(-0.5, max(yis) + 20)
    plt.plot(xi, yi, color = 'r', marker = 'x', linestyle = '-', label = "Trajectory of a Ballistic")
    plt.text(xi + 1., yi + 1., 't = %.4g s' % (t_array[i]))
    plt.show()
    plt.savefig(str(i) + '_ballistic.png')


plt.plot(xi, yi, color = 'r', marker = 'x')
plt.plot(xis, yis, linestyle = '-', label = "Trajectory of a Ballistic")
plt.text(xi + 1., yi + 1., 't = %.4g s' % (t_array[i]))
plt.savefig('overall.png')