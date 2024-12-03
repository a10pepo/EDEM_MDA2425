año = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014]


for i in año:
    if(i%4 == 0 and (i%100 !=0 or i%400 == 0)):
        print(f'{i} es bisiesto')
    else:
        print(f'{i} no es bisiesto')
