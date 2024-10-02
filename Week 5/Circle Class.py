class circle: #makes a class for circle
    def __init__ (self, radius, color, pi=3.1416): #initialize the properties for class circle
        self.radius = radius #defines the properties of class circle
        self.color = color
        self.pi = pi

    def getColor(self): #makes a function to print the circle's color
        print(self.color)

    def getCircum(self): #makes a function which calculates the circle's circumference
        Circum = 2*self.pi*self.radius
        print(Circum)
        
circletest = circle(2, "white") #defines the circle which we will test

#test run
circletest.getColor()

circletest.getCircum()
