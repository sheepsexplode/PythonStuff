hourswork = raw_input ("Enter hours worked: ")

try:
    fhourswork = float(hourswork)
except:
    print 'Error, incorect entry'
    quit ()
    
payrate = raw_input ("Enter the rate of pay: ")

try:
    fpayrate = float(payrate)
except:
    print 'Error, incorect entry'
    quit ()
    
if fhourswork > 40:
    othours = fhourswork - 40
    otpay = (fpayrate * 1.5) * othours 
    reghour = fpayrate * 40
    totpay = reghour + otpay
else:
    totpay = fhourswork * fpayrate

print totpay
