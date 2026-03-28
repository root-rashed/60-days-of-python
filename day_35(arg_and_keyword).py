def personal_data(name,**arg):
    print(name)
    print(arg)
personal_data("Rashed",varsity="SEU",city="Dhaka")



def personal_data(name,*arg):
    print(name)
    print(arg)
personal_data("Rashed","SEU","Dhaka")