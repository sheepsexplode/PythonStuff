#To help understand IO in functions
def iotest(n1, n2):

    n1p = str(n1)
    n2p = str(n2)
    
    print n1p + '\n + \n' + n2p + ' = '
    
    sum = n1 + n2
    sum_mult = n1 * n2
    
    
    return sum, sum_mult

#Collects user input
first_num = raw_input('>')
first_num = float(first_num)
print ' + '
snd_num = raw_input('>')
snd_num = float(snd_num)

#Calling function with user input and storing the return in total
total = iotest(first_num, snd_num)

#print 
print total