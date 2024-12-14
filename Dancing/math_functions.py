from math import cos, sin, pi
from matplotlib import pyplot as plt

fig_names = ('circle', 'spiral', 'deltoid', 'spiral_diff', 'circle_diff')

def circle(t, r=1.0):
    x = r*cos(t)
    y = r*sin(t)
    return (x, y)

def spiral(t, r = 1.0):
    x = r*t*cos(t)
    y = r*t*sin(t)
    return (x, y)

def deltoid(t):
    x = 2*cos(t)+cos(2*t)
    y = 2*sin(t)-sin(2*t)
    return (x, y)

def spiral_diff(t, r = 1.0):
    x = -t*sin(t)+cos(t)
    y = t*cos(t)+sin(t)
    return (x*r, y*r)

def circle_diff(t, r = 1.0):
    x = -sin(t)
    y = cos(t)
    return (x*r, y*r)



if __name__ == '__main__':

    X = []
    Y = []
    for t_i in range(0, 2*330, 30):
        t_i = t_i/100
        x,y = circle_diff(t_i)
        print(x)
        print(y)
        X.append(x)
        Y.append(y)
    plt.grid(True)
    plt.plot(X,Y)
    plt.show()



        
