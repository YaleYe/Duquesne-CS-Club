import matplotlib.pyplot as plt
from randomWalk import RandomWalk

rw = RandomWalk(20000)
rw.fill_walk()

point_numbers=list(range(rw.num_points))
plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
plt.scatter(rw.x_values[0],rw.y_values[0],s=10,c='Red')
plt.scatter(rw.x_values[-1],rw.y_values[-1],s=10,c='green')
plt.show()