import math_functions as mf
import requests
import math
from matplotlib import pyplot as plt

fig_names = ('circle', 'spiral', 'deltoid', 'spiral_diff', 'circle_diff', 'astroid', 'gipocicloid', 'epicycloid', 'heart')
#########################################
aruco_id = 1 ###DEPENDS ON YOUBOT'S ID###
#########################################
url_fig = 'http://192.168.0.164:8000/target/figure/'

response = requests.get(url=url_fig, params={'aruco_id': aruco_id})


if __name__ == '__main__':
    k = response.json()[0]['k']
    r = response.json()[0]['r']
    name = response.json()[0]['name']
    name = 'circle'
    X = []
    Y = []
    if name == 'circle':
        for i in range(0, 361, 10):
            t_i = math.pi * i / 180
            x, y = mf.circle(t_i, r)
            X.append(x)
            Y.append(y)
    print(k, r, name) 
    plt.grid(True)
    plt.plot(X,Y)
    plt.show()
