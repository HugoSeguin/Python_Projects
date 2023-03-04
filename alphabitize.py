#Import 
def Alphabetize_Name(list):
    list.Sorted(by="first")
    list.Sorted(by= "last")
    return list


def alphbitize_name(list_of_dicts):
    return sorted(list, key = operator.itemgetter('last', 'first'))