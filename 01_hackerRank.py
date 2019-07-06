def is_leap(year):
    leap = False
    if(year/4)%2 == 0 and ((year/400)%2 !=0 or (year/400)%2 ==0):
        leap = True
    elif (year/100)%2 != 0 and (year/4)%2 == 0:
        leap = False
    #if (year/4)%2 == 0:
    #    if (year/400)%2 == 0:
    #        leap = True
    #    else:
    #        leap = False
    # Write your logic here
    
    return leap

#year = int(input())
#input result
#add new comment
print(is_leap(2400))