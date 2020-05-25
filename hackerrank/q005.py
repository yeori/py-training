def is_leap(year):
    div_by_four = lambda y: y % 4 == 0
    div_by_100  = lambda y: y % 100 == 0
    div_by_400 = lambda y: y % 400 == 0
    return (div_by_four(year) and not div_by_100(year) ) and div_by_400(year)

if __name__ == '__main__':
  year = int(input().strip())
  retval = is_leap(year)
  print(retval)