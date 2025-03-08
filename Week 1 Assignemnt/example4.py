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

def main():
    r2d2 = Droid('r2d2', [0, 0])  # Creating a Droid named 'r2d2'
    marvin = Droid('marvin', [1, 1])  # Creating a Droid named 'marvin'
    c3po = Droid('c3po', [3, 1])  # Creating a Droid named 'c3po'
    
    r2d2.move('F')
    r2d2.move('B')
    r2d2.turn('R')
    r2d2.move('F')
    r2d2.turn('L')
    r2d2.move('B')
    
    print(r2d2.current_pos())
    print(marvin.current_pos())

# Call the function main()
if __name__ == '__main__':
    main()