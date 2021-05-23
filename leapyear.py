def is_leapyear(year):
    if type(year) != int:
        return 0
    elif year%4 == 0 and year%100 != 0: 
        return 1
    elif year%100 == 0 and year%400 !=0:
        return -1
    elif year%400 == 0:
        return 1
    else:
        return -1