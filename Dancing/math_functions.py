from math import cos, sin, pi
from matplotlib import pyplot as plt

fig_names = ('circle', 'spiral', 'deltoid', 'spiral_diff', 'circle_diff', 'astroid', 'gipocicloid', 'epicycloid', 'heart')

def circle(t, r=1.0, *args):
    x = r*cos(t)
    y = r*sin(t)
    return (x, y)

def spiral(t, r = 1.0, *args):
    x = r*t*cos(t)
    y = r*t*sin(t)
    return (x, y)

def deltoid(t, *args):
    x = 2*cos(t)+cos(2*t)
    y = 2*sin(t)-sin(2*t)
    return (x, y)

def spiral_diff(t, r = 1.0, *args):
    x = -t*sin(t)+cos(t)
    y = t*cos(t)+sin(t)
    return (x*r, y*r)

def circle_diff(t, r = 1.0, *args):
    x = -sin(t)
    y = cos(t)
    return (x*r, y*r)

def astroid(t, *args):    
    x = 2 * sin(t)** 3
    y = 2 * cos(t) ** 3
    return (x, y)

def gipocicloid(t, r, k, *args):
    x = r * (cos(t) + (cos(k*t)/k))
    y = r * (sin(t) - (sin(k*t)/k))
    return (x, y)

def epicycloid(t, r, k, *args):
    x = (k*r+r) * cos(t) - r * cos((k+1)*t)
    y = (k*r+r) * sin(t) - r * sin((k+1)*t)
    return (x, y)

def heart(t, r, *args):
    x = r * sin(t)**3
    y = 0.8125*r*cos(t) - 0.3125*r*cos(2*t) - 0.125*r*cos(3*t) - 0.0625*r*cos(4*t)
    return (x, y)

if __name__ == '__main__':
    X = []
    Y = []
    T = 315
    n = 2
    k = 0.5
    r = 1
    for t_i in range(0, n*T, 1):
        t_i = t_i/100
        x,y = heart(t_i, r)
        # print(x)
        # print(y)
        X.append(x)
        Y.append(y)
    plt.grid(True)
    plt.plot(X,Y)
    plt.show()



        
