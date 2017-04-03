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

        userFile = open('data.txt', 'r')
        userFile.readline()
        for line2 in userFile :
            stripLine2 = line2.rstrip('\n')
            splitLine2 = stripLine2.split('|')
            self._catalogue[splitLine2[0]] = [splitLine2[1], splitLine2[2]]
        userFile.close()
    def __repr__(self):
        print(self._cDictionary)
        print(self._catalogue)

c1 = CountryCatalogue('data.txt')
c1.__repr__()
