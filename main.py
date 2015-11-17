import mail
import info

channel = "#natdm.ql"
botName = "tdmAlert"

def checkForGameStart(msg):
	keyPhrase = "4v4 TDM game ready to start!"
	if keyPhrase in msg:
		players = msg.split(":")[1]
		playerNames = players[:players.find("-")]
		playerNames = playerNames.split(",")
		for i, player in enumerate(playerNames):
			playerNames[i] = player.strip()
		return (playerNames)

def sendAlerts(playerNames):
	playersContactInfo = []
	for player in playerNames:
		if player in info.playersInfo:
			playerTuple = (player, info.playersInfo[player][0],
				info.playersInfo[player][1])
			players.append(playerTuple)
	playerContactInfo = mail.makeEmailAddresses(playersContactInfo)
	mail.sendEmails(playerContactInfo)