import wpilib
import wpilib.drive


class Drive:
    drivetrain = wpilib.drive.DifferentialDrive

    def __init__(self):
        self.enabled = False

    def move(self, y, rotation):
        """
        Causes the robot to move
        :param y: The speed that the robot should drive in the Y direction.
        :param rotation: The rate of rotation for the robot that is completely independent of the translation.
        """

        self.y = y
        self.rotation = rotation

    def execute(self):
        """Actually drive."""
        self.drivetrain.arcadeDrive(self.y, self.rotation)

        self.y = 0
        self.rotation = 0
