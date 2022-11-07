
def checker(year):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return str(year)("is leap year")
           else:
               return str(year)+"is not leap year"
       else: return str(year)+"is not leap year"
    else:
       return str(year)+ "is not leap year"


i