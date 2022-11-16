"""A few exceptions."""


class InvalidCircleRadius(Exception):
    """Exception for unreal circles."""

    def __init__(self, radius: float) -> None:
        """Creates a custom exception.

        Args:
            radius: float - circle's radius
        """
        super().__init__("Circle with radius = {0} - can't exist".format(radius))
