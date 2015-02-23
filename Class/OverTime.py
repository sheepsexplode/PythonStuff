hourswork = raw_input ("Enter hours worked: ")
fhourswork = float(hourswork)

payrate = raw_input ("Enter the rate of pay: ")
fpayrate = float(payrate)

if fhourswork > 40:
    othours = fhourswork - 40
    otpay = (fpayrate * 1.5) * othours 
    reghour = fpayrate * 40
    totpay = reghour + otpay
else:
    totpay = fhourswork * fpayrate

print totpay
