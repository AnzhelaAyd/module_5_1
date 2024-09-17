class Hous:
    def __init__(self, name, number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors


    def go_to(self,new_floors):
        if (new_floors < 0) or (new_floors > self.number_of_floors) :
            print('такого этожа не существует ')
        else:
            for i in range(1, new_floors+1):
                  print(i)


h1 = Hous('ЖК Горский', 18)
h2 = Hous('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
