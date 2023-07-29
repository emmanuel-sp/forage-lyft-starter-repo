from tire import Tire

class Octoprime(Tire):
    def __init__(self, tiresArray):
        self.tiresArray = tiresArray
    def needs_service(self):
        sum = 0
        for num in self.tiresArray:
            sum += num
        return sum >= 3
