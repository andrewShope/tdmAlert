import smtplib
import info

def sendEmails(playersInfo):
	"""
	Function will send an email to each person in the array that
	TDM is ready to begin.
	playersInfo should be an array of three indexed tuples where 
	the first index is the player's name, the second index is the 
	player's email address.
	"""
	fromaddr = 'natdmalert@gmail.com'
	username = 'natdmalert@gmail.com'
	password = info.emailPassword

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username, password)
	for player in playersInfo:
		msg = 'Hey, ' + player[0] + '! TDM is about to start.'
		server.sendmail(fromaddr, player[1], msg)
	server.quit()

def makeEmailAddresses(playerNumbers, gateways):
	'''
	playerNumbers should be a tuple containing the player's name,
	phone number, and carrier, respectively. Each of these should
	be a string.
	Gateways is a dictionary where the key is the name of the 
	carrier and the value is the email suffix to be used for that
	particular carrier. Each of these should be a string.
	The function should return a tuple where the first index is the
	player's name and the second index is the email address that 
	corresponds to their phone number through the SMS gateway. Each
	of these will be strings.
	'''

	playersEmails = []
	for i, player in enumerate(playerNumbers):
		email = playerNumbers[1]+gateways[playerNumbers[2]]
		playerEmails[i] = (playerNumbers[0], email)

	return playerEmails

