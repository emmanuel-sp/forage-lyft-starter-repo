from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery

from abc import ABC,abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass