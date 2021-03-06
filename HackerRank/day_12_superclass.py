
class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(self, firstName, lastName)
    #   scores - An array of integers denoting the Person's test scores.
        self.scores = scores

    # Write your constructor here
    def calculate(self):
        average = sum(self.scores)/len(self.scores)
        if average >= 90:
            return 'O'
        elif average >= 80 and average < 90:
            return 'E'
        elif average >= 70 and average < 80:
            return 'A'
        elif average >= 55 and average < 70:
            return 'P'
        elif average >= 40 and average < 55:
            return 'D'
        else:
            return 'T'




    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

# ----------------------------------

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
    #   scores - An array of integers denoting the Person's test scores.
        self.scores = scores

    # Write your constructor here
    def calculate(self):
        average = sum(self.scores)/len(self.scores)
        if average >= 90:
            return 'O'
        elif average >= 80 and average < 90:
            return 'E'
        elif average >= 70 and average < 80:
            return 'A'
        elif average >= 55 and average < 70:
            return 'P'
        elif average >= 40 and average < 55:
            return 'D'
        else:
            return 'T'


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
