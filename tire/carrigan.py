from tire import Tire

class Carrigan(Tire):
    def __init__(self, tiresArray):
        self.tiresArray = tiresArray
    
    def needs_service(self):
        for num in self.tiresArray:
            if num >= .9:
                return True
        return False