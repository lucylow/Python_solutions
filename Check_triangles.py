
# Check if a shape is a triangle 

class Triangle(object):
    
    number_of_sides = 3
    
    # init
    def __init__(self, angle1, angle2, angle3):
        
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    def check_angles(self):
        sumangles = self.angle1 + self.angle2 + self.angle3 
        if sumangles == 180:
            return True 
        else:
            return False
            
            
class Equilateral(Triangle):
    angle = 60 
    
    #init
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle 
        self.angle3 = self.angle 

# tester
my_triangle = Triangle(90,30,60)

print my_triangle.number_of_sides
print my_triangle.check_angles()
