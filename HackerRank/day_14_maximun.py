a = [1, 2, 5]


class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(self.__elements)-min(self.__elements)

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

# otra: los ordenas y restas el mayor al menor
def computeDifference(self):
    sorted_elements = sorted(self.__elements)
    self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])
