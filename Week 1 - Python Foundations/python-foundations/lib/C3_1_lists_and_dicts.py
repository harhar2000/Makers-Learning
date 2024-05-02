
# == EXERCISES ==

# Method name: fourth_element
# Purpose: returns the fourth element of the given list
# Arguments: one list
# Example:
#   Call:    fourth_element([1, 2, 3, 4, 5])
#   Returns: 4

list = [1, 2, 3, 4, 5]
def fourth_element(list):
   return list[3]

print(fourth_element(list))


# Method name: average
# Purpose: returns the average (the mean) of the given list
# Arguments: one list
# Example:
#   Call:    average([3, 1, 44, 1])
#   Returns: 12.25

list = [3, 1, 44, 1]
def average(list):
    total = sum(list)
    return total / len(list)

print(average(list))


# Method name: lowest_squared
# Purpose: returns the lowest number squared
# Arguments: one list
# Example:
#   Call:    lowest_squared([5, 3, 44, 7])
#   Returns: 9

list = [5, 3, 44, 7]
def lowest_squared(list):
    lowest_num = min(list)
    return lowest_num * lowest_num
    
print(lowest_squared(list))


# Method name: highest_squared
# Purpose: returns the highest number squared
# Arguments: one list
# Example:
#   Call:    highest_squared([5, 3, 44, 7])
#   Returns: 1936

list = [5, 3, 44, 7]
def highest_squared(list):
    highest_num = max(list)
    return highest_num * highest_num
    
print(highest_squared(list))
    

# Method name: starts_with_a
# Purpose: returns only elements starting with 'a'
# Arguments: one list
# Example:
#   Call:    starts_with_a(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'avocado']

list = ['banana', 'apple', 'orange', 'avocado']

def starts_with_a(list):
    new_list = []
    for item in list:
        if item[0] == 'a':
          new_list.append(item)
    return new_list
    
print(starts_with_a(list))


# Method name: starts_with_a_vowel
# Purpose: returns only the elements that start with a vowel
# Arguments: one list
# Example:
#   Call:    starts_with_a_vowel(['banana', 'apple', 'orange', 'avocado'])
#   Returns: ['apple', 'orange', 'avocado']

list = ['banana', 'apple', 'orange', 'avocado']
def starts_with_a_vowel(list):
    new_list = []
    vowel = ['a', 'e', 'i', 'o', 'u']
    for item in list:
        if item[0].lower() in vowel:
          new_list.append(item)
    return new_list
    
print(starts_with_a_vowel(list))


# Method name: reverse_each_element
# Purpose: reverses each string in the given list
# Arguments: one list
# Example:
#   Call:    reverse_each_element(['one', 'two'])
#   Returns: ['eno', 'owt']

list = ['one', 'two']
def reverse_each_element(list):
    reversed_list = []
    for i in list:
        reversed_list.append(i[::-1])
    return reversed_list
    
print(reverse_each_element(list))


# Method name: greater_than_5
# Purpose: returns only numbers greater than 5
# Arguments: one list
# Example:
#   Call:    greater_than_5([9, 3, 44, 7])
#   Returns: [9, 44, 7]

list = [9, 3, 44, 7]
def greater_than_5(list):
    new_list = []
    for i in list:
        if i > 5:
            new_list.append(i)
    return new_list 

print(greater_than_5(list))


# Method name: greater_than
# Purpose: returns only the elements that are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    greater_than([9, 3, 6, 44, 7, 7], 6)
#   Returns: [9, 44, 7, 7]

list = [9, 3, 6, 44, 7, 7]
int = 6
def greater_than(list, int):
    new_list = []
    for i in list:
        if i >int:
            new_list.append(i)
    return new_list 

print(greater_than(list, int))


# Method name: less_than
# Purpose: returns only the elements that are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    less_than([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: [3, 1]

list = [9, 3, 6, 44, 1, 7, 7]
int = 6
def less_than(list, int):
    new_list = []
    for i in list:
        if i <int:
            new_list.append(i)
    return new_list 

print(less_than(list, int))


# Method name: words_shorter_than
# Purpose: returns only the elements that have fewer characters than the number provided
# Arguments: one list and one number
# Example:
#   Call:    words_shorter_than(['banana', 'apple', 'orange', 'nut', 'avocado'], 6)
#   Returns: ['apple', 'nut']

list = ['banana', 'apple', 'orange', 'nut', 'avocado']
int = 6

def words_shorter_than(list, int):
    new_list = []
    for i in list:
        if len(i) < 6:
            new_list.append(i)
    return new_list

print(words_shorter_than(list, int))


# Method name: all_above
# Purpose: returns True if all elements are greater than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_above([9, 3, 6, 44, 1, 7, 7], 0)
#   Returns: True

list = [9, 3, 6, 44, 1, 7, 7]
int = 6

def all_above(list, int):
    for i in list:
        if i <= int:
            return False
    return True

print(all_above([9, 3, 6, 44, 1, 7, 7], 6))
print(all_above([9, 3, 6, 44, 1, 7, 7], 0))


# Method name: all_below
# Purpose: returns True if all elements are less than the number provided
# Arguments: one list and one number
# Example:
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 6)
#   Returns: False
#   Call:    all_below([9, 3, 6, 44, 1, 7, 7], 100)
#   Returns: True

list = [9, 3, 6, 44, 1, 7, 7]
int = 6

def all_below(list, int):
    for i in list:
        if i >= int:
            return False
    return True

print(all_below([9, 3, 6, 44, 1, 7, 7], 6))
print(all_below([9, 3, 6, 44, 1, 7, 7], 100))


# Method name: multiply_each_by
# Purpose: returns a new list with each element multiplied by the number provided
# Arguments: one list and one number
# Example:
#   Call:    multiply_each_by([9, 3, 6, 44, 1, 7, 7], 2)
#   Returns: [18, 6, 12, 88, 2, 14, 14]

list = [9, 3, 6, 44, 1, 7, 7]
int = 2

def multiply_each_by(list, int):
    new_list = []
    for i in list:
        i = i * int
        new_list.append(i)
    return new_list

print(multiply_each_by([9, 3, 6, 44, 1, 7, 7], 2))


# == DICTIONARY EXERCISES ==

# Method name: values_summed
# Purpose: returns the total of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    values_summed({'cat': 4, 'person': 2, 'centipede': 100})
#   Returns: 106

dict = {'cat': 4, 'person': 2, 'centipede': 100}
def values_summed(dict):
    total = 0
    for value in dict.values():
        total += value
    return total

print(values_summed({'cat': 4, 'person': 2, 'centipede': 100}))


# Method name: add_key_value_pair
# Purpose: returns the dictionary with the new key and value added
# Arguments: one dictionary, one key and one value
# Example:
#   Call:    add_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4)
#   Returns: {'cat': 4, 'person': 2, 'centipede': 100, 'dog': 4}

dict = {'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4
def add_key_value_pair(dict, key, value):
    dict[key] = value
    return dict

print(add_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'dog', 4))


# Method name: remove_key_value_pair
# Purpose: returns the dictionary with the key and value removed
# Arguments: one dictionary and one key
# Example:
#   Call:    remove_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'cat')
#   Returns: {'person': 2, 'centipede': 100}

def remove_key_value_pair(dict, key):
    if key in dict:
        del dict[key]
    return dict

print(remove_key_value_pair({'cat': 4, 'person': 2, 'centipede': 100}, 'cat'))


# Method name: where_value_below
# Purpose: returns key value pairs where the value is less than the number provided
# Arguments: one dictionary and one number
# Example:
#   Call:    where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5)
#   Returns: {'cat': 4, 'person': 2}

def where_value_below(old_dict, number):
    new_dict = {}
    for key, value in old_dict.items():  
        if value < number:  
            new_dict[key] = value 
    return new_dict  

print(where_value_below({'cat': 4, 'person': 2, 'centipede': 100}, 5))


# Method name: where_key_starts_with
# Purpose: returns key value pairs where the key starts with the letter provided
# Arguments: one dictionary and one letter
# Example:
#   Call:    where_key_starts_with({'cat': 4, 'person': 2, 'centipede': 100}, 'c')
#   Returns: {'cat': 4, 'centipede': 100} 

def where_key_starts_with(old_dict, letter):
    new_dict = {}  
    for key, value in old_dict.items():
        if key.startswith(letter):
            new_dict[key] = value 
    return new_dict 

print(where_key_starts_with({'cat': 4, 'person': 2, 'centipede': 100}, 'c'))