import smtplib
import info

fromaddr = 'natdmalert@gmail.com'
toaddr = '5133773157@txt.att.net'
msg = 'Hey, TDM is about to start!'
username = 'natdmalert@gmail.com'
password = info.emailPassword

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()
