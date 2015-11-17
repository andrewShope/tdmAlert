import mail
import info

def checkForGameStart(msg, author):
	keyPhrase = "4v4 TDM game ready to start!"
	keyAuthor = "SUCKLORD5000"
	if keyPhrase in msg and author == keyAuthor:
		players = msg.split(":")[3]
		playerNames = players[:players.find("-")]
		playerNames = playerNames.split(",")
		for i, player in enumerate(playerNames):
			playerNames[i] = player.strip()
		return (playerNames)

def sendAlerts(playerNames):
	print("In sendAlerts, this is playerNames:")
	print(playerNames)
	playersContactInfo = []
	for player in playerNames:
		if player in info.playersInfo:
			playerTuple = (player, info.playersInfo[player][0],
				info.playersInfo[player][1])
			playersContactInfo.append(playerTuple)
	print("This is playersContactInfo")
	print(playersContactInfo)
	# playersContactInfo will now be an array of two-indexed
	# tuples. The first index is the player's name and the
	# second index is the player's email address for their
	# corresponding phone number and carrier gateway
	playerContactInfo = mail.makeEmailAddresses(playersContactInfo, info.gateways)
	mail.sendEmails(playerContactInfo)