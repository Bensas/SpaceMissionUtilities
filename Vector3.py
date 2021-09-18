import math

class Vector3:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def norm2(self):
    return math.sqrt(self.x**2 + self.y**2 + self.z **2)
  
  def normalize(self):
    norm = self.norm2()
    return Vector3(self.x / norm, self.y / norm, self.z / norm)

  @classmethod
  def normalize(cls, vec):
    norm = vec.norm2()
    return Vector3(vec.x / norm, vec.y / norm, vec.z / norm)
  
  def cross_product(v1, v2):
    x = v1.y * v2.z - v1.z * v2.y
    y = v1.z * v2.x - v1.x * v2.z
    z = v1.x * v2.y - v1.y * v2.x
    return Vector3(x, y, z)
  
  def dot_product(v1, v2):
    return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
  
  def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)
  
  def __eq__(self, obj):
    if type(self) == type(obj):
      return obj.x == self.x and obj.y == self.y and obj.z == self.z
    else:
      raise TypeError
  
  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    z = self.z + other.z
    return Vector3(x, y, z)
  
  def __sub__(self, other):
    x = self.x - other.x
    y = self.y - other.y
    z = self.z - other.z
    return Vector3(x, y, z)

  def __neg__(self):
    return Vector3(0, 0, 0) - self

class UnitVectorRequiredError(Exception):
    """Called when a function requires a unit vector (norm 1)"""
    def __init(self, message="The vector provided must be of norm 1"):
      self.message = message
      super().__init__(self.message)
