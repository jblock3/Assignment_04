##
# This program was written by Jamie Block (Student #: 250777666)
#

# Task 1: Implementation of Country class

class Country :
    def __init__(self, name, pop, area, continent = '') :
        self._name = name
        self._population = pop
        self._area = area
        self._continent = continent
    def __repr__(self) :
        return ('{} is in {} with a population density of {}').format(self._name, self._continent, self._population / self._area)
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


class CountryCatalogue:
    def __init__(self, filename):
        self._catalogue = {}
        self._cDictionary = {}

        continentFile = open('continent.txt', 'r')
        continentFile.readline()
        for line in continentFile :
            stripLine = line.rstrip('\n')
            splitLine = stripLine.split(',')
            self._cDictionary[splitLine[0]] = splitLine[1]

        userFile = open(filename, 'r')
        userFile.readline()
        for line2 in userFile :
            stripLine2 = line2.rstrip('\n')
            splitLine2 = stripLine2.split('|')
            commaStrip1 = splitLine2[1].replace(',', '')
            commaStrip2 = splitLine2[2].replace(',', '')
            num1 = int(commaStrip1)
            num2 = float(commaStrip2)
            self._catalogue[splitLine2[0]] = Country(splitLine2[0], num1, num2)

        userFile.close()

    def filterCountriesByContinent(self) :
        continentInput = input('Please enter the continent name: ')
        for key in self._cDictionary :
            if self._cDictionary[key] == continentInput :
                print(key)
        else :
            print('That continent does not have any stored countries in the catalogue')

    def printCountryCatalogue(self) :

    def findCountry(self) :
        countryInput = input('Please enter the name of the country you are looking for: ')
        if countryInput in self._catalogue :
            return self._catalogue[countryInput]
        else :
            print('That country does not exist in the catalogue')

    def deleteCountry(self) :
        countryInput = input('Please enter the name of the country you wish to delete: ')
        if countryInput in self._catalogue :
            self._cDictionary.pop(countryInput)
            self._catalogue.pop(countryInput)
            print('Country was deleted')
        else :
            print('That country does not exist in the catalogue')

    def addCountry(self) :
        valid = False
        while not valid :
            countryInput = input('Please enter the name of the country you wish to add: ')
            if countryInput in self._catalogue :
                print('That country already exists in the catalogue!')
            else :
                valid = True
                populationInput = int(input('What is the population of the country? '))
                areaInput = float(input('Area of the country is: '))
                continentInput = input('What continent is the country in? ')
                self._catalogue[countryInput] = populationInput, areaInput
                self._cDictionary[countryInput] = continentInput

    def setPopulationOfASelectedCountry(self) :
        countryInput = input('Please enter the country name: ')
        if countryInput in self._catalogue :
            newPopulation = int(input('Enter the new population: '))
            self._catalogue[countryInput].replace(countryInput(1), newPopulation)
            print('The new population is {}'.format(newPopulation))
        else :
            print('That country does not exist in the catalogue')

    def saveCountryCatalogue(self, filename) :

    def findCountryWithLargestPop(self) :
        largest = 0
        for key in self._catalogue :
            if self._catalogue[key[1]] > largest :
                largest = self._catalogue[key[1]]
        print(largest)

    def findCountryWithSmallestArea(self) :
        smallest = 40000000000000000.0    # Just picked an arbitrarily large number to compare to
        for key in self._catalogue :
            if self._catalogue[key[2]] < smallest :
                smallest = self._catalogue[key[2]]
        print(smallest)

    def findMostPopulousContinent(self) :

    def filterCountriesByPopDensity(self) :
