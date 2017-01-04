class Human(object):
    def __init__(self, input_gender):
        self.gender = input_gender
    def printGender(self):
        print self.gender

li_lei = Human('male')
print li_lei.gender
li_lei.printGender()

