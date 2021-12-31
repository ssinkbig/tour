import timeit

def is_power_of_two(n):
  return (n != 0) and (n & (n-1) == 0)

def time_usage(func):
  def wrapper(*args, **kwargs):
    start_time = timeit.default_timer()
    retval = func(*args, **kwargs)
    elapsed = timeit.default_timer() - start_time
    print(f"[{func.__name__}] elapsed time: {elapsed}")
    return retval
  return wrapper

class Mersenne(object):
  def __init__(self, seed = 5489):
    self.state = [0]*624
    self.f = 1812433253
    self.m = 397
    self.u = 11
    self.s = 7
    self.b = 0x9D2C5680
    self.t = 15
    self.c = 0xEFC60000
    self.l = 18
    self.index = 624
    self.lower_mask = (1<<31)-1
    self.upper_mask = 1<<31

    # update state
    self.state[0] = seed
    for i in range(1,624):
      self.state[i] = self.int_32(
        self.f*(self.state[i-1]^(self.state[i-1]>>30)) + i
      )

  def twist(self):
    for i in range(624):
      temp = self.int_32(
        (self.state[i]&self.upper_mask)+(self.state[(i+1)%624]&self.lower_mask)
      )
      temp_shift = temp>>1
      if temp%2 != 0:
        temp_shift = temp_shift^0x9908b0df
      self.state[i] = self.state[(i+self.m)%624]^temp_shift
    self.index = 0

  def int_32(self, number):
    return int(0xFFFFFFFF & number)

  def random_int32(self, max=None):
    if self.index >= 624:
      self.twist()
    y = self.state[self.index]
    y = y^(y>>self.u)
    y = y^((y<<self.s)&self.b)
    y = y^((y<<self.t)&self.c)
    y = y^(y>>self.l)
    self.index+=1
    val = self.int_32(y)
    return val % (max + 1) if max is not None else val

  def random_uniform_float(self):
    return float(self.random_int32()) / float(0xFFFFFFFF)
