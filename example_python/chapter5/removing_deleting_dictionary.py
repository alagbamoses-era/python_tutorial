#!/usr/bin/python3

crops_dict = {'cereals':'maize', 'fruits':'orange', 'veges': 'spinach'}

crops_dict['legumes'] = 'cowpea'

print(crops_dict)
crops_dict['veges'] = 'cocorus'

print(crops_dict)


crops_clear = crops_dict.clear()

print(crops_clear)


del crops_dict



