from random import choice


class RandomWalk():
    #generate a randomWalk list
    def __init__(self, num_points=5000):

        self.num_points = num_points

        self.x_values = [0] #initialize starting point as [0,0]
        self.y_values = [0]

    def fill_walk(self):
        #computing all the points randomWalk has covered

        #keep walking until list reach the length of list
        while len(self.x_values) < self.num_points:

            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            #decide what direction to walk and distance to walk

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            #decide what direction to walk and distance to walk

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] +x_step
            next_y = self.y_values[-1] +y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


