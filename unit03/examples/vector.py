class Vector:
    x: int
    y: int

    def __init__(self, x, y):
        # Initialize vector components
        self.x = x
        self.y = y

    def __str__(self):
        # Return a string representation of the vector
        return f"({self.x}, {self.y})"

    def __mul__(self, scalar):
        # Return a new vector scaled by the scalar
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other):
        # Return a new vector that is the sum of this vector and another vector
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        # Return a new vector that is the negation of this vector
        return Vector(-self.x, -self.y)

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, -1)

print(v1)          # Output: (2, 3)
print(v2)          # Output: (4, -1)

v3 = 3 * v1
print(v3)          # Output: (6, 9)

v4 = v1 + v2
print(v4)          # Output: (6, 2)

v5 = -v1
print(v5)          # Output: (-2, -3)
