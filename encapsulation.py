class Secret():
  def __init__(self,secret,password):
    self.__secret = secret
    self.__password = password






  def get_secret(self,password):
    if password == self.__password:
      print ("Password corret. Secret: {}".format(self.__secret))
      choice = input("would you like to change the password? ")

      if choice == "yes":
        new_password = input("What would you like to set password to? ")
        self.__password = new_password
        print(self.__dict__)

      else:
        return
    else:
      print("password is wrong")

andrew_secret = Secret("I am beautiful","truth")
andrew_secret.get_secret("truth")


# 1. Create a method that lets you change password given the current password


# 2. Hash the password when a secret is created