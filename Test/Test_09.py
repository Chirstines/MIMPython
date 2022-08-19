
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		return None

	def distance(self, other, metric):
		dx = self.x - other.x
		dy = self.y - other.y
		if metric == 'L1': #The Manhattan distance
			return abs(dx) + abs(dy)
		if metric == 'L2': #The Euclid distance
			return (dx**2 + dy**2)**(1/2)

	#Method for the point symmetry
	def point_symmetry(self):
		new_x = - self.x
		new_y = - self.y
		return Point(new_x, new_y)

	def __repr__(self):
	    return (f'Point({self.x!r}, '
	    	    f'{self.y!r})')