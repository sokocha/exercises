class ElectricSocket():
  pass

class USSocket(ElectricSocket):
  pass

class UKSocket(ElectricSocket):
  pass

andrew= USSocket()
edem = UKSocket()

# print(isinstance(andrew, ElectricSocket))
# print(isinstance(edem, ElectricSocket))

class Person:
  def __init__(self,complaint="no internet"):
    self.complaint = complaint

  
  def complain(self):
    # print(self.complaint)

    if (isinstance(self,Person)):
      print(self.complaint)
    else:
      print("not allowed")

class EIT(Person):
  pass

class Fellow(Person):
  pass

class Cat():
  pass

people = list()

for _ in range(7):
  people.append(Fellow())

for _ in range(58):
  people.append(EIT())

people.append(Cat())

for person in people:
  person.complain()

