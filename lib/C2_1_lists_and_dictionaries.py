
# == LIST EXERCISES ==

# Method name: first_element
# Purpose: returns the first element of the given list
# Arguments: one list
# Example:
#   Call:    first_element([1, 2, 3])
#   Returns: 1

def first_element(lst):
    return lst[0]

print(first_element([1, 2, 3]))


# Method name: second_element
# Purpose: returns the second element of the given list
# Arguments: one list
# Example:
#   Call:    second_element([1, 2, 3])
#   Returns: 2

def second_element(lst):
    return lst[1]

print(second_element([1, 2, 3]))


# Method name: last_element
# Purpose: returns the last element of the given list
# Arguments: one list
# Example:
#   Call:    last_element([1, 2, 3])
#   Returns: 3

def last_element(lst):
    return lst[-1]

print(last_element([1, 2, 3]))


# Method name: first_two_elements
# Purpose: returns the first two elements of the given list
# Arguments: one list
# Example:
#   Call:    first_two_elements([1, 2, 3])
#   Returns: [1, 2]

def first_two_elements(lst):
    return lst[0:2]

print(first_two_elements([1, 2, 3]))


# Method name: first_three_elements
# Purpose: returns the first three elements of the given list
# Arguments: one list
# Example:
#   Call:    first_three_elements([1, 2, 3, 4])
#   Returns: [1, 2, 3]

def first_three_elements(lst):
    return lst[0:3]

print(first_three_elements([1, 2, 3, 4]))


# Method name: total
# Purpose: returns the sum of all the elements in the given list
# Arguments: one list
# Example:
#   Call:    total([1, 2, 3])
#   Returns: 6

def total(lst):
    return sum(lst)
        
print(total([1, 2, 3]))


# Method name: lowest_number
# Purpose: returns the lowest number in the given list
# Arguments: one list
# Example:
#   Call:    lowest_number([4, 2, 6])
#   Returns: 2

def lowest_number(lst):
    return min(lst)

print(lowest_number([4, 2, 6]))


# Method name: highest_number
# Purpose: returns the highest number in the given list
# Arguments: one list
# Example:
#   Call:    highest_number([4, 6, 2])
#   Returns: 6

def highest_number(lst):
    return max(lst)

print(highest_number([4, 6 ,2]))


# Method name: the_beatles
# Purpose: returns the list ['john', 'paul', 'george', 'ringo']
# Arguments: none
# Example:
#   Call:    the_beatles()
#   Returns: ['john', 'paul', 'george', 'ringo']

def the_beatles():
    return ['john', 'paul', 'george', 'ringo']

print(the_beatles())


# Method name: i_joined_the_beatles
# Purpose: adds the given name to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one string
# Example:
#   Call:    i_joined_the_beatles('yoko')
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko']

def i_joined_the_beatles(new_member):
    lst = ['john', 'paul', 'george', 'ringo']
    return lst + [new_member]

print(i_joined_the_beatles("yoko"))


# Method name: we_joined_the_beatles
# Purpose: adds the given names to the list ['john', 'paul', 'george', 'ringo']
# Arguments: one list
# Example:
#   Call:    we_joined_the_beatles(['yoko', 'stuart'])
#   Returns: ['john', 'paul', 'george', 'ringo', 'yoko', 'stuart']

original_beatles = ['john', 'paul', 'george', 'ringo']
def we_joined_the_beatles(lst):
    beatles = original_beatles.copy()
    beatles.extend(lst)
    return beatles
print(we_joined_the_beatles(['yoko', 'stuart']))
    

# Method name: remove_nones_from_list
# Purpose: removes all the None values from the given list
# Arguments: one list
# Example:
#   Call:    remove_nones_from_list([1, None, 2, None, 3])
#   Returns: [1, 2, 3]

lst = [1, None, 2, None, 3]
def remove_nones_from_list(lst):
    return [item for item in lst if item is not None]
        
print(remove_nones_from_list([1, None, 2, None, 3]))
    

# Method name: double_list
# Purpose: returns a list with all the elements of the given list repeated twice
# Arguments: one list
# Example:
#   Call:    double_list([1, 2, 3])
#   Returns: [1, 2, 3, 1, 2, 3]

def double_list(lst):
    return lst *2
print(double_list([1, 2, 3]))


# Method name: unique_elements
# Purpose: returns a list with all the unique elements of the given list
# Arguments: one list
# Example:
#   Call:    unique_elements([1, 2, 1, 3, 2, 3])
#   Returns: [1, 2, 3]

def unique_elements(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(unique_elements([1, 2, 1, 3, 2, 3]))


# Method name: add_to_list
# Purpose: adds the given element to the given list
# Arguments: one list and one element
# Example:
#   Call:    add_to_list(["a", "b", "c"], "d")
#   Returns: ["a", "b", "c", "d"]

def add_to_list(lst, item):
    lst.append(item)
    return lst

print(add_to_list(["a", "b", "c"], "d"))


# == DICTIONARY EXERCISES ==

# Method name: new_band_member
# Purpose: merges a given dictionary into an existing dictionary
# Arguments: one dictionary
# Note: {"vocalist": "miss piggy", "lead_guitar": "scooter"}
# Example:
#   Call:    new_band_member({"bass": "flea"})
#   Returns: {"vocalist": "miss piggy", "lead_guitar": "scooter", "bass": "flea"}

band_members = {"vocalist": "miss piggy", "lead_guitar": "scooter"}

def new_band_member(new_member):
    band_members.update(new_member)
    return band_members

print(new_band_member({"bass": "flea"}))


# Method name: all_values
# Purpose: returns a list of all the values in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_values({"a": 1, "b": 2, "c": 3})
#   Returns: [1, 2, 3]

def all_values(dct):
    return list(dct.values())

print(all_values({"a": 1, "b": 2, "c": 3}))


# Method name: all_keys
# Purpose: returns a list of all the keys in the given dictionary
# Arguments: one dictionary
# Example:
#   Call:    all_keys({"a": 1, "b": 2, "c": 3})
#   Returns: ["a", "b", "c"]

def all_keys(dct):
    return list(dct.keys())

print(all_keys({"a": 1, "b": 2, "c": 3}))


# Method name: remove_nones_from_dictionary
# Purpose: removes all pairs from a given dictionary where the value is None
# Arguments: one dictionary
# Example:
#   Call:    remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
#   Returns: {"a": 1, "c": 3}

def remove_nones_from_dictionary(dct):
    new_dct = {}
    for key, value in dct.items():
        if value is not None:
            new_dct[key] = value
    return new_dct

result = remove_nones_from_dictionary({"a": 1, "b": None, "c": 3})
print(result)


# Method name: touch_in
# Purpose: creates a dictionary from a given tube station and time
# Arguments: two strings, one for the tube station and one for the time
# Example:
#   Call:    touch_in('Aldgate East', '2022/01/30 17:12')
#   Returns: {'entrypoint': 'Aldgate East', 'time': '2022/01/30 17:12'}

def touch_in(station, time):
    new_dct = {'entrypoint': station, 'time': time}
    return new_dct
result = touch_in('Aldgate East', '2022/01/30 17:12')
print(result)