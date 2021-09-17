# Created by Marcin "Cozoob" Kozub 22.08.2021
import cv2
import numpy as np

class Polygon:

    def __init__(self, points):
        self.points = points

    def get_centroid(self):
        x, y = 0, 0
        n = len(self.points)
        for point in self.points:
            x += point[0]
            y += point[1]
        return x/n, y/n

    def is_in_area(self, x_cord, y_cord):
        contour = np.array(self.points)
        value = cv2.pointPolygonTest(contour, (x_cord, y_cord), measureDist=False)
        if value == -1:
            return False
        return True

    def get_area(self):
        contour = np.array(self.points)
        return cv2.contourArea(contour)     # It doesn't work and I don't know why

if __name__ == '__main__':
    rectangle = Polygon([[2,4],[2,2],[8,4],[8,2]])
    print(rectangle.get_area())
    print(rectangle.is_in_area(1,1))
    print(rectangle.is_in_area(2,3))
    print(rectangle.get_centroid())