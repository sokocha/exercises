# Static Method - a method that 
# can be called without a class instance. Static Methods don't take self. 
# Static methods don't have access to variables within a class
import random
class StringHelper():
  @staticmethod  #this is a decorator and must be used for creating static methods. 
  # A decorator is a function that manipulates another function before calling it.

  def scramble(string):
    temp_str = ""

    for char in string:
      temp_str += char.upper() if random.randint(0,1) else char.lower()
      print (temp_str)

  @staticmethod
  
  def abbreviate(string,char_length):
    if char_length < len(string):
      print(string[0:char_length] + "...")
    else:
      print(string)



StringHelper.scramble("Andrew")
StringHelper.abbreviate("moo",3)

class UnitConverter():
  
  @staticmethod
  def cm_to_in(cm):
    inches = 0.393701*cm
    print(inches)

  @staticmethod
  def in_to_cm(inches):
    cm = 2.54*inches
    print(cm)

  @staticmethod
  def mi_to_km(miles):
    km = 1.60934*miles
    print(km)

  @staticmethod
  def km_to_mi(km):
    miles = 0.621371*km
    print(miles)

  @staticmethod
  def f_to_celsius(fah):
    celsius = (fah - 32)*(5/9)
    print(celsius)

  @staticmethod
  def celsius_to_f(celsius):
    fahrenheit = 1.8 * celsius + 32  
    print(fahrenheit)

  @staticmethod
  def gm_lbs(gm):
    lbs = gm * 0.00220462
    print(lbs)

  @staticmethod
  def lbs_to_gm(lbs):
    gm = lbs * 453.592
    print(gm)

  @staticmethod
  def li_floz(li):
    floz = li * 33.814
    print(floz)

  @staticmethod
  def floz_to_li(floz):
    li = floz * 0.0295735
    print(li)

UnitConverter.cm_to_in(5)
UnitConverter.in_to_cm(1)

UnitConverter.mi_to_km(5)
UnitConverter.km_to_mi(5)

UnitConverter.f_to_celsius(32)
UnitConverter.celsius_to_f(32)

UnitConverter.gm_lbs(10000)
UnitConverter.lbs_to_gm(10000)


UnitConverter.li_floz(1)
UnitConverter.floz_to_li(1)


