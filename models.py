"""Models of geometric shapes."""
import math
from exceptions import InvalidCircleRadius


class Circle(object):
    """Class for the geometric figure circle."""

    DEGREE = 360

    def __init__(self, radius: float) -> None:
        """Creates a circle.

        Args:
            radius: float - radius of circle.

        Raises:
            InvalidCircleRadius: if new circle can'time exist.
        """
        self.__radius = radius
        if not self.check():
            raise InvalidCircleRadius(radius)

    @property
    def radius(self) -> float:
        """Get current value of radius.

        Returns:
            float - current value of radius.
        """
        return self.__radius

    @radius.setter
    def setter_radius(self, radius) -> None:
        """Setter for radius.

        Args:
            radius: float - new value for radius.

        Raises:
            InvalidCircleRadius: if new circle can'time exist.
            ValueError : if new value not be numeric.
        """
        try:
            self.__radius = float(radius)

        except ValueError:
            raise ValueError("Radius must be float, not {0}".format(type(radius)))

        if not self.check():
            raise InvalidCircleRadius(radius)

    def check(self) -> bool:
        """Checks the circle for existence.

        Returns:
            bool - true if the triangle can existence else false.
        """
        return isinstance(self.radius, (float, int)) and self.radius > 0

    def get_len_circle(self) -> float:
        """Counts and rounds to 2 decimal places the circumference of the circle.

        Returns:
            float - circumference of the circle.
        """
        return round(math.pi * 2 * self.radius, 2)


class Ball(Circle):
    """Class for ball."""

    def degree_to_meter(self) -> float:
        """Counts how many meters are in one degree of the ball.

        Returns:
             float - length in one degree.
        """
        return self.get_len_circle() / Circle.DEGREE

    def move(self, speed: float, time: float, acceleration=0):
        """Counts how many degrees the ball has turned while moving with uniform acceleration.

        Args:
            speed: float - initial speed in meters per second.
            time: float - movement time in seconds.
            acceleration: float - acceleration in meters per second squared.

        Returns:
            float - how many degrees did the ball spin.
        """
        path = speed * time + (acceleration * time * time) / 2
        return (path / self.degree_to_meter()) % Circle.DEGREE
