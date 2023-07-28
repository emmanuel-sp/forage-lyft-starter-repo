from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass