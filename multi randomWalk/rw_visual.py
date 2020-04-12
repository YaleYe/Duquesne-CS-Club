import matplotlib.pyplot as plt
from randomWalk import RandomWalk

rw = RandomWalk()
rw.get_step()
rw.fill_walk()
plt.plot(rw.x_values,rw.y_values,linewidth=0.5)
plt.show()
