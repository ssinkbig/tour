import pprint

class Matrix(object):
  def __init__(self, rows, cols, val = None):
   self.rows = rows
   self.cols = cols
   self.m = []
   for r in range(rows):
     self.m.append([val]*cols)

  def __str__(self):
    return pprint.pformat(self.m)

  def __getitem__(self, key):
    return self.m[key]
