#
#   WebScraper
#
# I wrote this code for fun, do whatever you want with it.
# 
#

from ArcFinder import DriverAltamira
from ArcFinder import DriverBoe
from ArcFinder import DriverIdealista

class WebScrapper:
    drivers = []
    def __init__(self, boe=True, altamira = False, idealista = False):
        if boe:
            self.drivers.append(DriverBoe())
        if altamira:
            self.drivers.append(DriverAltamira())
        if idealista:
            self.drivers.append(DriverIdealista())


    def scrap(self):
        houses = []
        for driver in self.drivers:
            houses.append(driver.scrap())
        return houses

    