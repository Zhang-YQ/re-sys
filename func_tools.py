def mfunc_str_to_list(my_string):
    str_list=my_string.strip(',').split(',')
    print(str_list)
    print(type(str_list))

def mfunc_list_to_str(list1):
#list转str
    list_str=','.join(list1)
    return list_str

def mfunc_list_to_tuple(list1):
    tuple1=tuple(list1)
    return tuple