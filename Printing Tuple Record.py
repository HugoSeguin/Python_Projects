#

import operator

def format_sort_records(list_of_tuples):
    #create a array for all items
    output = []
    #creates a template for all items, how produce
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted (list_of_tuples):
        key=operator.itemgetter(1,0)):

        output.append(template.format(*person))
    return output
print('\n'.join(format_sort_records(PEOPLE)))