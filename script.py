import math

def dist(x1, y1, x2, y2): # DISTANCE FUNCTION TO CALCULTE DISTANCE
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

print("WELCOME TO THE TRIANGLE PERIMETER PROGRAM") # GET INPUT
print("Enter the coordinates of the vertices of a triangle...")
print("\n")

print("VERTEX A")
x1 = int(input("Enter x-coordinate for Vertex A: "))
y1 = int(input("Enter y-coordinate for Vertex A: "))
print("\n")

print("VERTEX B")
x2 = int(input("Enter x-coordinate for Vertex B: "))
y2 = int(input("Enter y-coordinate for Vertex B: "))
print("\n")

print("VERTEX C")
x3 = int(input("Enter x-coordinate for Vertex C: "))
y3 = int(input("Enter y-coordinate for Vertex C: "))
print("\n")

Ab = dist(x1, y1, x2, y2) # CALCULATE DISTANCES
Ac = dist(x3, y3, x1, y1)
Bc = dist(x2, y2, x3, y3)

print("SIDE LENGTHS & PERIMETER:") # OUTPUT DISTANCES TO USER
print("AB = " + str(Ab))
print("AC = " + str(Ac))
print("BC = " + str(Bc))
print("Perimeter = " + str(Ab + Ac + Bc))
