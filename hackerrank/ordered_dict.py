from collections import OrderedDict

def append(dic, key, value):
    if key in dic :
        dic[key] += value
    else:
        dic[key] = value

dic = OrderedDict()
append(dic, 'a', 3)
append(dic, 'b', 2)
append(dic, 'a', 4)
print(dic)