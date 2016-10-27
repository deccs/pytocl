from pytocl.car import Command, State
from shockwave.accelerator import Accelerator
from shockwave.gearer import Gearer
from shockwave.steerer import Steerer


class Stability:
    def __init__(self, plan):
        self.plan = plan
        self.steerer = Steerer(self.plan)
        self.accelerator = Accelerator(self.plan)
        self.gearer = Gearer(self.plan)

    def get_command(self, carstate: State) -> Command:
        command = Command()
        command.steering = 0
        command.accelerator = 0
        command.gear = 0
        command.brake = 0
        command.focus = 0
        return command



