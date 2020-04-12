import matplotlib.pyplot as plt
from randomWalk import RandomWalk

#if program is going, it will keep developing
while True:
    rw = RandomWalk()
    #create a example of random walk
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none', s=15)

    plt.scatter(0,0,c='green',edgecolor='none',s=100) #starting point
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100) #ending point

    plt.axes().get_xaxis().set_visible(False) #set x-axis invisible
    plt.axes().get_yaxis().set_visible(False) #set y-axis invisible

    plt.show()

    keep_running=input("Keep walking or not?(y/n)")
    if keep_running == 'n':
        break

