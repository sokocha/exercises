class Venue():
  def __init__(self, guest_list={}):
    self.guest_list = guest_list

  def add_to_list(self,guest,email):
    self.guest = guest
    self.email = email

    self.guest_list[guest] = email
    print("{} added to guest list".format(guest))
    print ("there are now {} guests on the list".format(len(self.guest_list.keys())))

  def find_guest(self,name):
    if name in self.guest_list:
      self.name = name
      print("{} exists in the list".format(self.guest_list[name]))
    else:
      print("{} does not exitst".format(name))

  def loop(self):
    while True:

      choice = input("would you like to add guest or check guest list?  ")

      if choice == "add guest" or choice == "add":
        new_name = input("Who would you like to add to the list? ")
        new_email = input("What is {}'s email address?  ".format(new_name))
        self.add_to_list(new_name,new_email)
      elif choice == "check guest list" or choice == "check" or choice == "check list":
        list_query = input("What name would you like to check? ")
        self.find_guest(list_query)
      elif choice == "exit":
        return
  
        

  


mest = Venue()
mest.add_to_list('sadiq','sokocha@gmail.com')
mest.add_to_list('james','james@gmail.com')
mest.add_to_list('fred','fred@gmail.com')
mest.add_to_list('bob','bob@gmail.com')

mest.loop()

# mest.find_guest('sadiq')
# mest.find_guest('sfsadiq')


# mest.register_guest("james","james@gmail.com")
# mest.register_guest("paul","paul@gmail.com")
# mest.register_guest("sadiq","sadiq@gmail.com")