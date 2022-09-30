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
  
  def draw(self, num_of_balls):
    if num_of_balls > len(self.contents):
      drawn_balls = copy.deepcopy(self.contents)
      self.contents.clear()
      return drawn_balls
    else:
      drawn_balls = []
      
      for i in range(num_of_balls):
        contents_len = len(self.contents)
        random_index = random.randrange(contents_len)
        drawn_ball = self.contents.pop(random_index)
        drawn_balls.append(drawn_ball)
        
      return drawn_balls
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  print("experiment")
