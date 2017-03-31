##
# This program was written by Jamie Block (Student #: 250777666)
#

# Task 1: Implementation of Country class

class Country :
    def __init__(self, name, pop, area, continent) :
        self._name = name
        self._population = pop
        self._area = area
        self._continent = continent
    def __repr__(self) :
        print(self._name, 'is in', self._continent, 'with a population density of', self._population / self._area)
    def setPopulation(self, pop) :
        self._population = pop
    def getName(self) :
        return self._name
    def getArea(self) :
        return self._area
    def getPopulation(self) :
        return self._population
    def getContinent(self) :
        return self._continent
    def getPopDensity(self) :
        return self._population / self._area

c1 = Country('China', 1000000000, 9.597, 'Asia')
print(c1.setPopulation(1000000000))
print(c1.getName())
print(c1.getArea())
print(c1.getPopulation())
print(c1.getContinent())
print(c1.getPopDensity())
c1.__repr__()

class CountryCatalogue :
    def __init__(self, filename) :
    def filterCountriesByContinent(self) :
    def printCountryCatalogue(self) :
    def findCountry(self) :
    def deleteCountry(self) :
    def addCountry(self) :
    def setPopulationOfASelectedCountry(self) :
    def saveCountryCatalogue(self, filename) :
    def findCountryWithLargestPop(self) :
    def findCountryWithSmallestArea(self) :
    def findMostPopulousContinent(self) :
    def filterCountriesByPopDensity(self) :
