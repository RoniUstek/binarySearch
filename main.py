class BinarySearch:
    def __init__(self, values, target):
        self.__values = values
        self.__target = target

    def search(self):
        count = 1
        midValue = self.middleValue(self.__values)
        while not self.valueChecker(midValue, self.__target):
            newValues = self.removeWrong(self.__values, self.__target, midValue)
            midValue = self.middleValue(newValues)
            count = count + 1
        print("it took "+str(count)+" passes to find the number")

    def middleValue(self, values):
        lengthOfList = len(values)
        midOfList = int(lengthOfList / 2)
        return values[midOfList]

    def valueChecker(self, midValue, target):
        return midValue == target

    def removeWrong(self, values, target, midValue):
        if midValue > target:
            values = values[:values.index(midValue)]
            return values
        else:
            values = values[midValue:]
            return values


userNum = 6
b = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], userNum)
b.search()
