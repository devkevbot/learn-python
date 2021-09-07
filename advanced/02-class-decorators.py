class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


c = Circle(5)
print(f"Radius is: {c.radius}")
print(f"Area is: {c.area}")
print(f"Volume of cylinder with heigh 20 is: {c.cylinder_volume(20)}")

unit_circle = Circle.unit_circle()
print(f"Radius of unit circle is: {unit_circle.radius}")

print(f"Pi is approximately: {Circle.pi()}")
