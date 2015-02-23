
total = 0
count = 0
while True:
    
    entnum = raw_input('Enter Number\n')
    
    if entnum == 'done' : break
    if len(entnum) < 1 :break
    
    try:
        num = float(entnum)
    except:
        print 'Bad Input!.\n'
        continue
    
    count = count + 1
    total = total + num
    
    print num, total, count
    
print 'Average:', total / count
    
        
    