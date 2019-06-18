class Line(object):
    
    def __init__(self,coor1,coor2):
    	self.coor1 = coor1
    	self.coor2 = coor2
    
    def distance(self):
        return ( ( ( (self.coor1[0]) - (self.coor1[1]) ) ** 2) + ( ( (self.coor2[0]) - (self.coor2[1]) ) ** 2 ) ) ** (1/2)
    
    def slope(self):
        pass


xa = 2
xb = 4
ya = -3
yb = 5
x = Line((xa,xb), (ya,yb))

print(x.distance())