def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_list = [1,2,3,45,2,1,3,4,24,7,9]
remove_duplicates(input_list)


print(input_list)
print(sorted(remove_duplicates(input_list)))