class CountryCatalogue:
    def __init__(self, catalogue = dict(), dictionary = dict()):
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
    def __repr__(self) :
        print(self._cDictionary)

c1 = CountryCatalogue()
c1.__repr__()
