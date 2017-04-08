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
            self._catalogue[splitLine2[0]] = [num1, num2]
        userFile.close()
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
    def tester(self):
        return self._catalogue

c1 = CountryCatalogue('data.txt')
c1.addCountry()
print(c1.tester())
