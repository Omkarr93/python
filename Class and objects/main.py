import tkinter as tk

class Circle(object):    #the constructor ,the is called when someone creates new circle , this assingment cretes attributes 
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self,canvas,colour):  # this is method that uses attributes to draw circle
        rad = self.radius
        x1 = self.center[0] - rad
        y1 = self.center[1] - rad
        x2 = self.center[0] + rad
        y2 = self.center[1] + rad
        canvas.create_oval(x1, y1, x2, y2, fill=colour)

    def move(self, x, y):
        # Update the center coordinates by adding x and y
        self.center = (self.center[0] + x, self.center[1] + y)


# Create a Tkinter window
root = tk.Tk()
root.title("Circle Example")

# Create a canvas to draw the circle on
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Create an instance of the Circle class
mycircle = Circle([300, 400], 75)
mycircle_1 = Circle([0, 400], 75)
mycircle_3 = Circle([400,400],100)


# Draw the circle on the canvas
mycircle.draw(canvas,'red')
mycircle_1.draw(canvas,'blue')
mycircle_3.draw(canvas,'green')

print(mycircle)
mycircle.radius = 10

# Start the Tkinter event loop
root.mainloop()
