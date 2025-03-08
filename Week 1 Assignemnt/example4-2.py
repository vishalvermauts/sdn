from math import sin, cos, radians
class Droid:
    # Create a class
    def __init__(self, name, pos):
        # The class takes a name as a parameter
        self.name = name
        self.pos = pos  # Position as list of coordinates [x, y]
        self.head = radians(0)  # Angle

    def turn(self, rotation):
        # Rotate left or right
        if rotation == 'R':  # Rotate right
            self.head -= radians(90)  # Turn 90 right
        elif rotation == 'L':  # Rotate left
            self.head += radians(90)  # Turn 90 left
    def move(self, step):
        # Step forward or backward
        if step == 'F':  # Move forward by 1 step
            self.pos[0] = self.pos[0] + round(cos(self.head))
            self.pos[1] = self.pos[1] + round(sin(self.head))
        elif step == 'B':  # Move backward
            self.pos[0] = self.pos[0] + round(cos(self.head - radians(180)))
            self.pos[1] = self.pos[1] + round(sin(self.head - radians(180)))
    def current_pos(self):
        # Return the current position
        return self.pos

class Marvin(Droid):
    def __init__(self):
        self.eyes = 2
        self.arms = 2
        self.legs = 2
        Droid.__init__(self, 'marvin1', [2, 3])  # Inheriting from parent class
def main():
    r2d2 = Droid('r2d2', [0, 0])  # Creating an object with name argument as 'r2d2'
    marvin = Droid('marvin', [1, 1])
    marvin1 = Marvin()
    print(marvin1.current_pos())
    marvin1.turn('R')
    marvin1.move('F')
    print(marvin1.current_pos())
    print(marvin1.legs)
    print(r2d2.current_pos())

# Call the function main()
if __name__ == '__main__':
    main()