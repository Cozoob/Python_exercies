# Created by Marcin "Cozoob" Kozub 21.09.2021
import math
from math import sqrt, acos

# constant representing the ratio between degrees and radians
RAD_TO_DEF_COEFF = 360 / (2 * math.pi)


class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.length = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def cross(self, other):
        a = (self.y * other.z) - (self.z * other.y)
        b = (self.x * other.z) - (self.z * other.x)
        c = (self.x * other.y) - (self.y * other.x)
        return Vector3D(a, b, c)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def angle(self, other):
        angle_cos = self.dot(other) / (self.length + other.length)
        return math.acos(angle_cos)


class Plane:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.normal_vector = self._calc_normal_vector()

    def _calc_normal_vector(self):
        # create two vectors with the same start point
        # let A to be a start point
        vector1 = Vector3D(self.B[0] - self.A[0], self.B[1] - self.A[1], self.B[2] - self.A[2])
        vector2 = Vector3D(self.C[0] - self.A[0], self.C[1] - self.A[1], self.C[2] - self.A[2])
        # the cross product of these two vectors is the normal vector to the plane
        return vector1.cross(vector2)


def normalise_vector(vector):
    return Vector3D(vector.x / vector.length, vector.y / vector.length, vector.z / vector.length)

def rad_to_deg(rad_angle):
    return rad_angle * RAD_TO_DEF_COEFF

if __name__ == '__main__':
    vector = Vector3D(4,0,3)
    print(vector.length)
    print(normalise_vector(vector))
    plane = Plane((0, 0, 0), (1, 0, 0), (0, 1, 0))
    plane2 = Plane((0, 0, 0), (1, 0, 0), (0, 0, 1))
    norm = plane.normal_vector
    norm2 = plane2.normal_vector
    print(rad_to_deg(norm.angle(norm2)))
    print(norm)
    print(norm2)


