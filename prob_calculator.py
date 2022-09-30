import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []

    for key, value in kwargs.items():
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

def has_expected_outcome(expected_balls, drawn_balls):
  for key, value in expected_balls.items():
    count_of_balls = drawn_balls.count(key)
    if count_of_balls < value:
      return False
    
  return True
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_of_expected_outcomes = 0
  
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    if has_expected_outcome(expected_balls, drawn_balls):
      num_of_expected_outcomes += 1

  return num_of_expected_outcomes / num_experiments
      
