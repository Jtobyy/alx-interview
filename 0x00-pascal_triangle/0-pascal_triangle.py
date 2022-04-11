def pascal_triangle(n):
    pascal_list = []
    if (n <= 0):
        return pascal_list
    else:
        if n == 1:
            pascal_list.append([1])
        elif n == 2:
            pascal_list.append([1, 1])
        else:
            for counter in range(1, n + 1):
                if counter == 1:
                    sub_list = [1]
                elif counter == 2:
                    sub_list = [1, 1]
                else:
                    temp = [1]
                    j = 0
                    while j < counter - 2:
                        temp.append(pascal_list[counter - 2][j]
                                    + pascal_list[counter - 2][j+1])
                        j += 1
                    temp.append(1)
                    sub_list = temp
                pascal_list.append(sub_list)
    return pascal_list
