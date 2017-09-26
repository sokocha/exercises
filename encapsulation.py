class Secret():
  def __init__(self,secret,password):
    self.__secret = secret
    self.__password = password

  def get_secret(self,password):
    if password == self.__password:
      return self.__secret

andrew_secret = Secret("I am beautiful","truth")
andrew_secret.get_secret("truth")
