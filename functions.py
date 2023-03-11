# Functions created by Sebastián Sarasti
# This functions help to make RPT analysis
import numpy as np
import matplotlib.pyplot as plt


# define a function to plot a 3D box
def plot_box_3d(x_l, y_l, z_l, axis_p, alpha_val=0.3):
    """"
  This function graph a 3d shape of a box, also it can be drawn a rectangular prisma
  This function plots with axes
  x_l: length in x coordinate
  y_l: length in y coordinate
  z_l: length in z coordinate
  axis_p: axis in which is going to be plotted the box
  """
    # face 1
    xl1 = np.linspace(0, x_l, 100, endpoint=True)
    yl1 = np.linspace(0, y_l, 100, endpoint=True)
    Xl1, Yl1 = np.meshgrid(xl1, yl1)
    zl1 = np.full(len(np.ravel(Xl1)), 0)
    Zl1 = zl1.reshape(Xl1.shape)
    # face 2
    xl2 = np.linspace(0, x_l, 100, endpoint=True)
    yl2 = np.linspace(0, y_l, 100, endpoint=True)
    Xl2, Yl2 = np.meshgrid(xl2, yl2)
    zl2 = np.full(len(np.ravel(Xl2)), y_l)
    Zl2 = zl2.reshape(Xl2.shape)
    # face 3
    xl3 = np.linspace(0, x_l, 100, endpoint=True)
    zl3 = np.linspace(0, z_l, 100, endpoint=True)
    Xl3, Zl3 = np.meshgrid(xl3, zl3)
    yl3 = np.full(len(np.ravel(Xl3)), 0)
    Yl3 = yl3.reshape(Xl3.shape)
    # face 4
    xl4 = np.linspace(0, x_l, 100, endpoint=True)
    zl4 = np.linspace(0, z_l, 100, endpoint=True)
    Xl4, Zl4 = np.meshgrid(xl4, zl4)
    yl4 = np.full(len(np.ravel(Xl4)), z_l)
    Yl4 = yl4.reshape(Xl4.shape)
    axis_p.plot_surface(Xl1, Yl1, Zl1, alpha=alpha_val, color='blue')
    axis_p.plot_surface(Xl2, Yl2, Zl2, alpha=alpha_val, color='blue')
    axis_p.plot_surface(Xl3, Yl3, Zl3, alpha=alpha_val, color='blue')
    axis_p.plot_surface(Xl4, Yl4, Zl4, alpha=alpha_val, color='blue')


# function to create trajectories
def trajectory(P_1, P_2, lb):
    """
    P1: is a matrix where it is saved the points at the beginning of the trajectory - shape (x1,y1,z1)
    P2: is a matrix where it is saved the points at the end of the trajectory  - shape (x1,y1,z1)
    lb: is the doming along the trajectory is going to be created - shape (points)
    """
    uv = P_2 - P_1
    n = np.sqrt(np.sum(uv ** 2))
    x1 = np.zeros(len(lb))
    y1 = np.zeros(len(lb))
    z1 = np.zeros(len(lb))
    for i in range(len(lb)):
        x1[i] = P_1[0] + uv[0] * lb[i]
        y1[i] = P_1[1] + uv[1] * lb[i] + np.cos(np.random.uniform(low=0, high=np.pi)) * 0.2 * 0.01
        z1[i] = P_1[2] + uv[2] * lb[i] + np.sin(np.random.uniform(low=0, high=np.pi)) * 0.2 * 0.01
    return (x1, y1, z1)
