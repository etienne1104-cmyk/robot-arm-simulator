import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

L1 = 3
L2 = 5


def forward_kinematics(theta1, theta2):

    t1 = np.radians(theta1)
    t2 = np.radians(theta2)

    x1 = L1*np.cos(t1)
    y1 = L1*np.sin(t1)

    x2 = x1 + L2*np.cos(t2+t1)
    y2 = y1 + L2*np.sin(t2+t1)

    base = (0,0)
    coude = (x1, y1)
    extremite = (x2, y2)
    return base, coude, extremite

base, coude, extremite = forward_kinematics(30,45)

x_points = [base[0], coude[0], extremite[0]]
y_points = [base[1], coude[1], extremite[1]]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
ax.set_aspect("equal")
ax.grid(True)
ax_slider1 = plt.axes([0.2, 0.15, 0.6, 0.03])
ax_slider2 = plt.axes([0.2, 0.05, 0.6, 0.03])
slider_t1 = Slider(ax_slider1, "theta1", -180, 180, valinit=45)
slider_t2 = Slider(ax_slider2, "theta2", -180, 180, valinit=45)
line, = ax.plot(x_points, y_points,"-g",marker="o",markersize=7)
ax.set_xlim(-8,8)
ax.set_ylim(-8,8)

def update(val):
    theta1 = slider_t1.val
    theta2 = slider_t2.val
    base, coude, extremite = forward_kinematics(theta1,theta2)
    x_points = [base[0], coude[0], extremite[0]]
    y_points = [base[1], coude[1], extremite[1]]
    line.set_xdata(x_points)
    line.set_ydata(y_points)
    fig.canvas.draw_idle()
slider_t1.on_changed(update)
slider_t2.on_changed(update)
plt.show()