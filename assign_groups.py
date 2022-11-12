from random import sample
from math import ceil

sample_roster = ['James Hetfield', 'Dave Mustaine', 'Cliff Burton', 'Kirk Hammett', 'Lars Ulrich', 'Ron McGovney', 'Lloyd Grant', 'Steve Harris', 'Dave Murray', 'Clive Burr', 'Adrian Smith', 'Bruce Dickinson', 'Nicko McBrain']

def assign_groups(roster, group_size):

    number_of_groups = ceil(len(roster) / group_size)
    print(f'number_of_groups: {number_of_groups}\n\n')

    list_of_groups = []
    for i in range(number_of_groups):
        group = sample(roster, group_size)
        list_of_groups.append(group)
        for j in group:
            roster.remove(j)
        if len(roster) < group_size and len(roster) > 0:
            group_size = len(roster)

    name_of_group = 1
    for i in list_of_groups:
        print(f'Group {name_of_group}')
        for j in i:
            print(j)
        print('')
        name_of_group += 1
    
    return list_of_groups

print(assign_groups(sample_roster, 3))