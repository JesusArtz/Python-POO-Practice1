import time

class Women:
    def __init__(self, name):
        self.name = name

    def getAnswer(self, answer = str(input("Emma, ¿Quieres ser mi novia? "))):

        return answer


class Men:
    def __init__(self, name):
        self.name = name

    def getMood(self, answer):
        seleccionarMood = (f"{self.name} esta Feliz", f"{self.name} esta Triste")

        if answer == 'No':
            return seleccionarMood[1]

        elif answer == 'Si':
            return seleccionarMood[0]

Name1 = Men("Name")
Name2 = Women("Name")

time.sleep(2)
print("")
print("")
print(Name1.getMood(Name2.getAnswer()))
