import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, green=None, red=None, orange=None, black=None, blue=None, pink=None, striped=None):
    self.contents = []
  
    balls = {
      "green": green,
      "red": red, 
      "orange": orange, 
      "black": black, 
      "blue": blue, 
      "pink": pink, 
      "striped": striped
    }

    for key, value in balls.items():
      if value is not None:
        for i in range(value):
          self.contents.append(key)
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  print("experiment")
