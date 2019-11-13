from constant import c,m1
def asteroid(m,v):
    Q1= m*v/2
    T=Q1/(c*m)
    Q2= c*m1*T
    if T>50:
        print('все умерли')
    elif 50>T>30:
        print('осталось 90%')
    else:
        print('БОЛЬНО')
        
asteroid(3*(10**21),56)
    