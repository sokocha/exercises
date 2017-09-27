import time

class Bus():
  def __init__(self,drivers = [],students=[]):
    self.drivers = drivers
    self.students = students
    print("Let's board the damn bus")

  def drive(self,students):
    if len(students) == 10 and len(self.drivers) == 1:
      print("Let's goooooooooooooo class")
      return
    elif len(students) > 10:
      difference = len(students) - 10
      print("there are {} too many students".format(difference))
    elif len(students) < 10:
      required_students = 10 - len(students)
      print("Add {} more students to drive.".format(required_students))
    else:
      print("you've not met the conditions. You currently have {} students and {} driver(s)".format(len(students),len(self.drivers)))
      return


  def board_students(self,quantity):
    for _ in range(quantity):
      self.students.append(Student)
      print ("{} students on board".format(len(self.students)))


  def remove_students(self,quantity):
    for _ in range(quantity):
      self.students.pop()
      remaining_students = len(self.students)
      
      print("Removing {} students".format(_+1))
      time.sleep(1)
      print("There are now {} students".format(remaining_students))


  def add_driver(self,quantity):
    for _ in range(quantity):
      new_driver = Driver()
      self.drivers.append(new_driver)
      print("There are {} drivers".format(len(self.drivers)))

  def remove_driver(self,quantity):
    for _ in range(quantity):
      if len(self.drivers) > quantity:
        self.drivers.pop()
        remaining_drivers = len(self.drivers)

        print("Removing {} drivers".format(_+1))
        time.sleep(0.5)
        print("There are now {} drivers".format(remaining_drivers))
      else:
        print("You can't remove more people than are on the bus")
        return





  def loop(self):
    
    new_driver = Driver()

    while True:

      # Bus(new_driver)
      primary_choice = input("Would you like to edit 'driver' or 'student' or just 'drive' ? ")
      if primary_choice == "student":
        add_remove_choice = input("would you like to add students or remove students? ")
        if add_remove_choice == "add":
          student_quantity = int(input("How many students do you want to add? "))
          self.board_students(student_quantity)
        elif add_remove_choice == "remove":
          student_quantity = int(input("How many would you like to remove? "))
          self.remove_students(student_quantity)
      elif primary_choice == "driver":
        add_remove_choice = input("would you like to add driver or remove driver? ")
        if add_remove_choice == "add":
          driver_quantity = int(input("How many drivers would you like to add ? "))
          self.add_driver(driver_quantity)
        elif add_remove_choice == "remove":
          driver_quantity = int(input("How many drivers would you like to remove ? "))
          self.remove_driver(driver_quantity)
      elif primary_choice == "drive":
        self.drive(self.students)



      



class Student():
  def __init__(self):
    print ("I'm alive and well.")

class Driver():
  counter = 0
  def __init__(self):
    self.counter += 1
    # print("I'm a driver. There are {} drivers".format(self.counter))


# students = []


# for _ in range(10):
#   students.append(Student())


ms_frizzle = Driver()

example = Bus()
example.loop()




