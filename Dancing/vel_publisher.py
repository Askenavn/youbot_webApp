from math_functions import spiral_diff, circle_diff, circle
import requests
from time import time, sleep
from matplotlib import pyplot as plt

count = 0
vX1 = []
vY1 = []

x_curr = 0.2
y_curr = 0
t_start = time()
for t_i in range(0, 2*314+34, 17):
    sleep(1)
    t_i = t_i/100
    x_next, y_next = circle(t_i, r=0.2)
    x = x_next - x_curr
    y = y_next - y_curr
    print(x)
    # input()
    t_curr = time()
    t = t_curr - t_start
    print('T: ', t)
    t_start = time()
    vx = x/t
    vy = y/t    
    
    print('vx: ', vx)
    print('vy: ', vy)
    
    vX1.append(vx)
    vY1.append(vy)
    
    r = requests.put('http://192.168.0.164:8000/cmd_vel/?aruco_id=1', params={'x': vx, 'y': vy})
    

plt.plot(vX1, vY1)    
plt.grid(True)
plt.show()


# vX = []
# vY = []
# sleep(2)
# t_start = time()
# while True:
#     t_curr = time()
#     dt1 = t_curr - t_start
#     print(dt1)
#     vx, vy = circle_diff(dt1, 0.2)
#     if dt1 >= 6.28:
#         break
#     count += 1
#     sleep(0.01)
#     vX.append(vx)
#     vY.append(vy)
#     r = requests.put('http://192.168.0.164:8000/cmd_vel/?aruco_id=1', params={'x': vx/5, 'y': vy/5})
    # print(r.url)

r = requests.put('http://192.168.0.164:8000/cmd_vel/?aruco_id=1', params={'x': 0, 'y': 0})
# plt.plot(vX, vY)
# plt.show()


