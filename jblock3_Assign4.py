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


class CountryCatalogue:
    def __init__(self, filename, catalogue=dict(), dictionary=dict()):
        self._catalogue = catalogue
        self._cDictionary = dictionary
        tempCountry = ''
        tempContinent = ''
        continentFile = open('continent.txt', 'r')
        continentLines = continentFile.readlines()[1:]
        for line in continentFile:
            splitLine = line.split(',')
            splitLine[0] = tempCountry
            splitLine[1] = tempContinent
            self._cDictionary[tempCountry] = tempContinent
        continentFile.close()

        tempCountry2 = ''
        tempPopulation = 0
        tempArea = 0.0
        userFile = open(filename, 'r')
        userFileLines = userFile.readlines()[1:]
        for line in userFile:
            splitLine2 = line.split('|')
            splitLine[0] = tempCountry2
            splitLine2[1] = tempPopulation
            splitLine2[2] = tempArea
            self._catalogue[splitLine[0]] = splitLine2[1], splitLine2[2]
        userFile.close()

    def filterCountriesByContinent(self) :
    def printCountryCatalogue(self) :
    def findCountry(self) :
    def deleteCountry(self) :
    def addCountry(self) :
        valid = False
        while not valid :
            countryInput = input('Please enter the name of the country you wish to add: ')
            if countryInput in self._catalogue :
                valid = True
                populationInput = int(input('What is the population of the country? '))
                areaInput = float(input('Area of the country is: '))
                continentInput = input('What continent is the country in? ')
                self._catalogue[countryInput] = populationInput, areaInput
                self._cDictionary[countryInput] = continentInput
            else :
                print('That country already exists in the catalogue!')


    def setPopulationOfASelectedCountry(self) :
    def saveCountryCatalogue(self, filename) :
    def findCountryWithLargestPop(self) :
    def findCountryWithSmallestArea(self) :
    def findMostPopulousContinent(self) :
    def filterCountriesByPopDensity(self) :
