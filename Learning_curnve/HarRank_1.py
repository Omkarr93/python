list_per = [ [0, 0, 0], [0, 0, 1], [0, 0, 2],
    [0, 1, 0], [0, 1, 1], [0, 1, 2],
    [0, 2, 0], [0, 2, 1], [0, 2, 2],
    [1, 0, 0], [1, 0, 1], [1, 0, 2],
    [1, 1, 0], [1, 1, 1], [1, 1, 2],
    [1, 2, 0], [1, 2, 1], [1, 2, 2],
    [2, 0, 0], [2, 0, 1], [2, 0, 2],
    [2, 1, 0], [2, 1, 1], [2, 1, 2],
    [2, 2, 0], [2, 2, 1], [2, 2, 2] ]

funct = [(lambda my_list : my_list if  my_list[0] +my_list[1]+ my_list[2] != 3 else None) (lst) for lst in list_per]



# funct = map(lambda my_list : my_list if  my_list[0] +my_list[1]+ my_list[2] != 3 else None,list_per)


print(funct)