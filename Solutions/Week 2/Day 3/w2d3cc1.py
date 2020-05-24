# Solution 1


def iterate(dict_):
    for key, value in dict_.items():
        print('key : ', key, ' --> type : ', type(key), end='\n')
        print('value : ', value, ' --> type : ', type(value), end='\n\n')


new_dict = {'name': 'John', 1: [2, 4, 3], 'dict': {1: 'apple', 2: 'ball'}, 2.0: 'version', 'age': 30, 'score': 98}

iterate(new_dict)


# Solution 2


def iterate(dict_):
    for item in dict_.items():
        print('key : ', item[0], ' --> type : ', type(item[0]), end='\n')
        print('value : ', item[1], ' --> type : ', type(item[1]), end='\n\n')


new_dict = {'name': 'John', 1: [2, 4, 3], 'dict': {1: 'apple', 2: 'ball'}, 2.0: 'version', 'age': 30, 'score': 98}

iterate(new_dict)


# Solution 3


def iterate(dict_):
    for key in dict_:
        print('key : ', key, ' --> type : ', type(key), end='\n')
        print('value : ', dict_[key], ' --> type : ', type(dict_[key]), end='\n\n')


new_dict = {'name': 'John', 1: [2, 4, 3], 'dict': {1: 'apple', 2: 'ball'}, 2.0: 'version', 'age': 30, 'score': 98}

iterate(new_dict)


# Solution 4


def iterate(dict_):
    for key in dict_.keys():
        print('key : ', key, ' --> type : ', type(key), end='\n')
        print('value : ', dict_[key], ' --> type : ', type(dict_[key]), end='\n\n')


new_dict = {'name': 'John', 1: [2, 4, 3], 'dict': {1: 'apple', 2: 'ball'}, 2.0: 'version', 'age': 30, 'score': 98}

iterate(new_dict)


# Solution 5


def iterate(dict_):
    for value in dict_.values():

        # could be used to get all the keys with the same value
        key = [k for (k, v) in dict_.items() if v == value][0]

        print('key : ', key, ' --> type : ', type(key), end='\n')
        print('value : ', value, ' --> type : ', type(value), end='\n\n')


new_dict = {'name': 'John', 1: [2, 4, 3], 'dict': {1: 'apple', 2: 'ball'}, 2.0: 'version', 'age': 30, 'score': 98}

iterate(new_dict)


# Solution 6


def iterate(dict_):

    # creating an enumerable or iterable object
    newDict = enumerate(dict_)

    for _ in range(len(dict_)):
        key = newDict.__next__()[1]
        value = dict_[key]
        print('key : ', key, ' --> type : ', type(key), end='\n')
        print('value : ', value, ' --> type : ', type(value), end='\n\n')


new_dict = {'name': 'John', 1: [2, 4, 3], 'dict': {1: 'apple', 2: 'ball'}, 2.0: 'version', 'age': 30, 'score': 98}

iterate(new_dict)


# -------------------------------------------------------------------------------------------------------------------------


# Output :

# key :  name  --> type :  <class 'str'>
# value :  John  --> type :  <class 'str'>
#
# key :  1  --> type :  <class 'int'>
# value :  [2, 4, 3]  --> type :  <class 'list'>
#
# key :  dict  --> type :  <class 'str'>
# value :  {1: 'apple', 2: 'ball'}  --> type :  <class 'dict'>
#
# key :  2.0  --> type :  <class 'float'>
# value :  version  --> type :  <class 'str'>
#
# key :  age  --> type :  <class 'str'>
# value :  30  --> type :  <class 'int'>
#
# key :  score  --> type :  <class 'str'>
# value :  98  --> type :  <class 'int'>
