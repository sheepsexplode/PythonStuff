usrscore = raw_input ("Enter a score between 0.0 and 1.0: ")

try:
    score = float(usrscore)
except:
    print 'Error, incorect entry'
    quit ()
    
if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
elif score < 0.6:
    grade = 'F'

print grade 