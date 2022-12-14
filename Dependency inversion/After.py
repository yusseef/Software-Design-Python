#We will use an abstract class to achive the Dependency inversion Orincible
#Dependecy inversion is one of SOLID princible it stands as "D" in SOID
'''
It means that hig level moduls which provide complex logis (Electric swith here in our exampe)
should be easiy reusable and not afected of any change in low level modules ad here
we use abstraction method
'''
from abc import ABC, abstractmethod #AbstracBasedClass = ABC
class Swithable(ABC):
    
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Swithable): #lightBulb now is a subclass of Switchable
    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")

#another two change the light bulb status
class ElectricPowerSwitch:

    def __init__(self, c: Swithable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()