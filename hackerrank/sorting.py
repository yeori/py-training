chars = {'a': 2, 'b': 2, 'c': 5, 'd': 3}

itr = iter(chars.items())
entries = list(itr)
entries.sort(key=lambda item: item[1], reverse=True)
for e in entries:
  print(e[0], e[1], e)
# print(*entries)