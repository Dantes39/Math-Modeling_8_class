def visakosni_god(a=2008):
    """присваеваем нужный год в аргумент a""" 
    if a%4!=0 and a%400!=0:
        print('не високосный')
    else:
        print('високосный')
        

visakosni_god(2101)