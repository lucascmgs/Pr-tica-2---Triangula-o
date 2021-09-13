import math
import matplotlib.pyplot as plt

class ValuePair:
  def __init__(self, given_x, given_y):
    self.x = given_x
    self.y = given_y
  
  def __str__(self):
    return f"({self.x},{self.y})"

  def to_list(self):
    return [self.x, self.y]

class Vec(ValuePair):
  def size(self):
    return math.sqrt(self.x**2+self.y**2)
  def dot(self, other_vector):
    return self.x * other_vector.x + self.y * other_vector.y

  def __mul__(self, scalar:float):
    return Vec(self.x*scalar, self.y*scalar)

  def __truediv__(self, scalar:float):
    return Vec(self.x/scalar, self.y/scalar)

  def normalized(self):
    current_size = self.size()
    return self/current_size


class Point(ValuePair):
  def __add__(self, other_point):
    return Point(self.x + other_point.x, self.y + other_point.y)

  def __sub__(self, other_point):
    return Vec(self.x - other_point.x, self.y - other_point.y)

  def __truediv__(self, scalar:float):
    return Point(self.x/scalar, self.y/scalar)


class Circle:
  def __init__(self, given_center:Point, given_radius:float):
    self.center = given_center
    self.radius = given_radius

  def __str__(self):
    return f"(Center: {self.center}, Radius: {self.radius})"

  def is_point_inside(self, given_point):
    distance_to_point = (given_point-self.center).size()
    if distance_to_point <= self.radius:
      return True
    else:
      return False
  

        

class Triangle:
    def __init__(self, a, b, c) -> None:
        self.points = [a,b,c]
        self.a = a
        self.b = b
        self.c = c
        
    def is_point_inside(self, given_point):
        orient_ab = orient(self.a, self.b, given_point)
        orient_bc = orient(self.b, self.c, given_point)
        orient_ca = orient(self.c, self.a, given_point)

        return ((orient_ab > 0) and (orient_bc > 0) and (orient_ca) > 0)

    def to_list(self):
        return [self.a.to_list(), self.b.to_list(), self.c.to_list()] 

    def to_plt_artist(self, given_color="green"):

      return plt.Polygon(self.to_list(),color=given_color, fill = None)


def orient(p, q, r):
  return p.x*q.y +p.y*r.x + q.x*r.y -(q.x * p.y + r.x*q.y + r.y*p.x)