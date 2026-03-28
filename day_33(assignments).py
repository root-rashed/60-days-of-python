def sum_of_lists(input_lists):
    sum =0
    for i in range(len(input_lists)):
        sum = input_lists[i]+sum
    return sum


input_numbers= [1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("Sum of lists: {}".format(sum_of_lists(input_numbers)))





def list_reverse(input_lists):
    reverse_list =[]
    length = len(input_lists)

    for i in range(length):
        reverse_list.append(input_lists[length-1-i])
    return reverse_list

print("List reverse: {}".format(list_reverse(input_numbers)))





def list_even(input_lists):
    even =[]
    for item in range(len(input_lists)):
        if ( input_lists[item]%2==0 ):
            even.append(input_lists[item])
    return even
print("Even check: {}".format(list_even(input_numbers)))




def duplicates(input_lists):
    unique = []

    for i in input_lists:
        if i not in unique:
            unique.append(i)

    return unique

print("Unique check: {}".format(duplicates(input_numbers)))





def con(list1,list2):
    con =[]
    for i in range(len(list1)):
        con.append(list1[i])

    for j in range(len(list2)):
        con.append(list2[j])
    return con

num1 =[1,2,3,4,5]
num2 =[6,7,8,9,10]
print("After concatenation: {}".format(con(num1,num2)))