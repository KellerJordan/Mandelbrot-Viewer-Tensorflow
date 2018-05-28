import pprint

import numpy as np


pp = pprint.PrettyPrinter()

def get_meshgrid(X, Y, R, n_x=1000, n_y=1000):
    Rx = R
    Ry = (n_y / n_x) * Rx
    x_ubd, x_lbd = X + Rx, X - Rx
    y_ubd, y_lbd = Y + Ry, Y - Ry
    
    x_rng = np.linspace(x_lbd, x_ubd, n_x, dtype=np.float64)
    y_rng = np.linspace(y_lbd, y_ubd, n_y, dtype=np.float64)
    
    X, Y = np.meshgrid(x_rng, y_rng)
    Z = X + 1j*Y
    return Z

def fractal_to_img(a):
    # cyclically color the points by number of iterations to diverge
    cycle_steps = 20 # number of steps before colors cycle
    a_cyclic = 2 * np.pi * a / cycle_steps
    rgb = [127 + 80 * np.cos(a_cyclic),
           127 + 80 * np.sin(a_cyclic),
           127 + 80 * np.cos(a_cyclic)]
    img = np.stack(rgb, 2)

    # color points which never diverged black
    img[a == a.max()] = 0
    img = np.uint8(img)
    return img
