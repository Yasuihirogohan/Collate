import time, sys




    
'''
    def Odd():
        global anyNumber
        print ((anyNumber+1) *3 )
        anyNumber = anyNumber + 1
    
    def Even():
        global anyNumber
        print ((anyNumber / 2))
        anyNumber = anyNumber + 1
'''
print ('Enter number:')
anyNumber = int(input())

def collatz():

   # try:

    global anyNumber
    time.sleep(0.5)
    if anyNumber % 2 == 0:
        print ((int(anyNumber / 2)))
        anyNumber = anyNumber / 2
    elif anyNumber % 2 == 1:
        print (int(anyNumber * 3 + 1))
        anyNumber = anyNumber * 3 + 1    
    elif anyNumber == 0:
        print (int(anyNumber * 3 + 1))
        anyNumber = anyNumber + 1

def nonIntString():
    try:
        global anyNumber
        if anyNumber != int(anyNumber):
            print('Nope')
    except ValueError:
        sys.exit()


        
"""      
    except:
        if anyNumber != int(anyNumber):
            print ('Cant read')
            sys.exit()
"""
while anyNumber != 1:    
    collatz()






    



    
    
