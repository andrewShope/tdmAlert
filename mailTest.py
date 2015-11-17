import smtplib
import info

fromaddr = 'natdmalert@gmail.com'
toaddr = 'someAddress@some.com'
msg = 'Hey, TDM is about to start!'
username = 'natdmalert@gmail.com'
password = info.emailPassword

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
