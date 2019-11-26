#encoding: utf-8
import numpy as np
import math
import matplotlib.pyplot as plt

lidar_path = 'lidar_data/3/lidar2_data.txt'

lidar_angle = []
lidar_range = []
lidar_x = [0] * 1080
lidar_y = [0] * 1080

with open(lidar_path, 'r') as lidar_data:
    lines = lidar_data.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        lidar_angle.append(value[0])
        lidar_range.append(value[1])

for i in range(len(lidar_angle)):
    if abs(lidar_range[i]) < 20:
        lidar_x[i] = lidar_range[i] * math.cos(lidar_angle[i] / 180 * math.pi)
        lidar_y[i] = -lidar_range[i] * math.sin(lidar_angle[i] / 180 * math.pi)


pointcloud_lidar = np.array([lidar_x , lidar_y])

plt.plot(pointcloud_lidar[0], pointcloud_lidar[1], 'r.', label = "lidar")
plt.title('Calibration')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.axis('equal')
plt.show()