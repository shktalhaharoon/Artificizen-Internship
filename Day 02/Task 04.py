dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 40}




for key in dict1:
    if key in dict2:
        print(key, ":", dict1[key] + dict2[key])


# for key in dict2:
#     if key in dict1:
#         dict1[key] = dict1[key] + dict2[key]
#     else:
#         dict1[key] = dict2[key]
# print(dict1)