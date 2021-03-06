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

# Task 2: creation of the CountryCatalogue class
class CountryCatalogue:
    def __init__(self, filename):   # Constructor
        self._catalogue = {}
        self._cDictionary = {}

        continentFile = open('continent.txt', 'r')
        continentFile.readline()
        for line in continentFile :
            stripLine = line.rstrip('\n')
            splitLine = stripLine.split(',')
            self._cDictionary[splitLine[0]] = splitLine[1]

        userFile = open(filename, 'r')      # Will be used to open the data.txt file
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
        for key in self._catalogue :
            tempCountry = Country(key, self._catalogue[key][0], self._catalogue[key][1], self._cDictionary[key])
            tempCountry.__repr__()

    def findCountry(self) :     # Finds country in catalogue, if it exists
        countryInput = input('Please enter the name of the country you are looking for: ')
        if countryInput in self._catalogue :
            return self._catalogue[countryInput]
        else :
            print('That country does not exist in the catalogue')

    def deleteCountry(self) :       # Deletes an already existing country in catalogue
        countryInput = input('Please enter the name of the country you wish to delete: ')
        if countryInput in self._catalogue :
            self._cDictionary.pop(countryInput)
            self._catalogue.pop(countryInput)
            print('Country was deleted')
        else :
            print('That country does not exist in the catalogue')

    def addCountry(self) :      # Adds new country to catalogue if it doesn't exist yet
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
        catalogueFile = open(filename, 'w')
        for key in self._catalogue :
            name = key
            continent = self._cDictionary[key]
            population = self._catalogue[key][0]
            populationDens = round(self._catalogue[key][0] / self._catalogue[key][1], 2)
            catalogueFile.write('{}|{}|{}|{}'.format(name, continent, population, populationDens))

        catalogueFile.close()

    def findCountryWithLargestPop(self) :
        largest = 0
        for key in self._catalogue :
            if self._catalogue[key][0] > largest :
                largest = self._catalogue[key][0]
        print(largest)

    def findCountryWithSmallestArea(self) :
        smallest = 40000000000000000.0    # Just picked an arbitrarily large number to compare to other values
        for key in self._catalogue :
            if self._catalogue[key][1] < smallest :
                smallest = self._catalogue[key][1]
        print(smallest)

    def findMostPopulousContinent(self) :
        largest = 0
        for key in self._catalogue :
            if self._catalogue[key][0] > largest :
                largest = self._catalogue[key][0]
                country = key
        continent = self._cDictionary[country]
        print(continent)

    def filterCountriesByPopDensity(self) :
        lowerBound = input('Enter the lower bound for the population density range: ')
        upperBound = input('Enter the upper bound for the population density range: ')
        for key in self._catalogue :
            if self._catalogue[key][1] > int(lowerBound) and self._catalogue[key][1] < int(upperBound) :
                print(key)

# End of assignment
