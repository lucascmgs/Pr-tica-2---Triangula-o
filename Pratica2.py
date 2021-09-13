import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import data_structures as dt
import triangulation



polygon1_file = open('polygon2.txt', 'r')

lines = polygon1_file.readlines()

points_x = []
points_y = []

for line in reversed(lines) :
    elements = line.split('  ')
    elements[1] = elements[1].strip()
    points_x.append([float(elements[0])])
    points_y.append([float(elements[1])])


stacked_points = np.column_stack((points_x, points_y))
polygon1 = plt.Polygon(stacked_points, edgecolor="red", fill = None)


figure, axes = plt.subplots()

offset = 10.0

axes.add_artist(polygon1)
axes.set_xlim(np.amin(points_x)-offset, np.amax(points_x)+offset)
axes.set_ylim(np.amin(points_y)-offset, np.amax(points_y)+offset)

points = []
for i in range(len(stacked_points)):
    p = stacked_points[i]
    points.append(dt.Point(p[0], p[1]))


(triangles, diagonals) = triangulation.ear_clipping_method(points)
for t in triangles:
    triangle_plotter = t.to_plt_artist()
    axes.add_artist(triangle_plotter)

# axes.plot()
# plt.show()


result_file = open("diagonals2.txt", "w+")
for diagonal in diagonals:

    result_file.write(f'{diagonal[0].x} {diagonal[0].y} {diagonal[1].x} {diagonal[1].y} \n')
