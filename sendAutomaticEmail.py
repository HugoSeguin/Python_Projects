import smtplib
smtObj = smtplib.SMTP('smtp.example.com', 587)
smtObj.elo()
smtpObj.starttls()
smtpObj.login('email' , 'password')
smtpObj.sendemail('email', 'email', 'suject:') {}
smtpObj.quit()
