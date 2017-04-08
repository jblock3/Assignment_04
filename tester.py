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

    def tester(self):
        return self._catalogue

c1 = CountryCatalogue('data.txt')
print(c1.tester())
