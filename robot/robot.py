import magicbot
import wpilib

from robotpy_ext.control.button_debouncer import ButtonDebouncer
from wpilib.buttons import JoystickButton
from components import drive
import wpilib.drive


class Bot(magicbot.MagicRobot):
    drive: drive.Drive

    def createObjects(self):
        # Joysticks
        self.joystick = wpilib.Joystick(0)

        # Drive motor controllers
        #   Dig | 0/1
        #   2^1 | Left/Right
        #   2^0 | Front/Rear
        self.lf_motor = wpilib.Victor(0b00)  # =>0
        self.lr_motor = wpilib.Victor(0b01)  # =>1
        self.rf_motor = wpilib.Victor(0b10)  # =>2
        self.rr_motor = wpilib.Victor(0b11)  # =>3

        self.drivetrain = wpilib.drive.DifferentialDrive(wpilib.SpeedControllerGroup(self.lf_motor, self.lr_motor),
                                                         wpilib.SpeedControllerGroup(self.rf_motor, self.rr_motor))

    def autonomous(self):
        super().autonomous()

    def disabledPeriodic(self):
        pass

    def disabledInit(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # Normal joysticks
        self.drive.move(-self.joystick.getY(), self.joystick.getX())


if __name__ == '__main__':
    wpilib.run(Bot)
