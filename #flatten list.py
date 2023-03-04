#flatten list

def flatten(mylist):
    return(one_element 
            for one_sublist in mylist
            for one_elemnt in one_sublist)
print(flatten([1,2], [3,2]))