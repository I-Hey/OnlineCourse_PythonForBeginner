def is_leap(year):
    if year % 4 != 0:
        return False
    elif  year % 100 != 0:
        return True
    elif  year % 400 != 0:
        return False
    elif year % 3200 != 0:
        return True
    else:
        return False

print (is_leap(2019))

def sum_of_list(numbers):
    return sum(numbers)
print(sum_of_list([1,2,3]))