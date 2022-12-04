from random import sample
from math import ceil, floor
import json
from rosters import thieves_105

sample_roster = ['James Hetfield', 'Dave Mustaine', 'Cliff Burton', 'Kirk Hammett', 'Lars Ulrich', 'Ron McGovney', 'Lloyd Grant', 'Steve Harris', 'Dave Murray', 'Clive Burr', 'Adrian Smith', 'Bruce Dickinson', 'Nicko McBrain']

def assign_groups(roster, group_size):

    number_of_groups = ceil(len(roster) / group_size)
    remainder = len(roster) % group_size
    print(f'remainder: {remainder}')
    print(f'number_of_groups: {number_of_groups}\n\n')

    list_of_groups = []
    for i in range(number_of_groups):
        group = sample(roster, group_size)
        list_of_groups.append(group)
        for j in group:
            roster.remove(j)
        if len(roster) < group_size and len(roster) > 0:
            group_size = len(roster)

    if len(list_of_groups[-2]) > len(list_of_groups[-1]):
        list_of_groups[-1].append(list_of_groups[-2].pop())

    name_of_group = 1
    for i in list_of_groups:
        print(f'Group {name_of_group}')
        for j in i:
            print(j)
        print('')
        name_of_group += 1
    
    return list_of_groups

# print(assign_groups(sample_roster, 3))
# print(assign_groups(sample_roster, 4))

def assign(roster, number_of_groups):
    group_size = len(roster) / number_of_groups
    print('group size: ', group_size)
    print('ceil: ', ceil(group_size))
    print('floor: ', floor(group_size))
    group_modulo = len(roster) % number_of_groups
    print('group modulo: ', group_modulo)
    group_floor_division = len(roster) // number_of_groups
    print('group floor division: ', group_floor_division)

    group_dict = {}

    group_number = 0
    for i in range(number_of_groups):
        if group_modulo == 0:
            group = sample(roster, floor(group_size))
        else:
            group = sample(roster, ceil(group_size))
            group_modulo -= 1
        for j in group:
            roster.remove(j)
        group_dict[group_number] = group
        group_number += 1
        print(f'Group Number {group_number}\n{group}')

    return group_dict

# assign(sample_roster, 3)
# assign(sample_roster, 2)
# assign(sample_roster, 3)

def make_json(py_dict):
    filename = input('Please enter the filename you wish to create:')
    print(f'Creating json for Python Dictionary: {py_dict}')

    with open(f'{filename}.json', 'w') as fp:
        json.dump(py_dict, fp, indent=4)

# make_json(assign(sample_roster, 3))

assign(thieves_105,1)

# make_json(assign(thieves_105,1))