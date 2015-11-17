import time
import socket
import main

server = "irc.quakenet.org".encode()
channel = "#nactf.ql".encode()
botnick = "tdmAlert".encode()

def ping(pingID): 
	ircsock.send(b"PONG :" + pingID.encode() +  b"\r\n")
	print("PONG :" + pingID)

def say(chan , msg):
  ircsock.send(b"PRIVMSG "+ chan + b" :"+ msg + b"\n")

def joinchan(chan): 
  ircsock.send(b"JOIN "+ chan + b"\n")

def hello(): 
  ircsock.send(b"PRIVMSG "+ channel + b" :Hello!\n")
  print(botnick.decode() + ": Hello!")

def getID(msg):
	"""
	This function takes in a PING message and strips it of the ID 
	so that we can send it back in our PONG
	"""
	msg = msg
	msgList = msg.split(':')
	return msgList[1]

print("here")
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
print("Connected")

# Wait for the server to send it's initial messages to signal
# to us that it is time to send user info
while True:
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.decode()
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)
	if ircmsg.find('Found your hostname') != -1:
		print("Found")
		break

# Send nick info to IRC server
ircsock.send(b"NICK "+ botnick + b"\r\n") 
ircsock.send(b"USER "+ botnick + b" * 8" + b" :" + botnick +b"\r\n")

# Wait for the server to finish sending MOTD so that we can send
# the commands to join our channel
while True:
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.decode('ascii')
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)
	if ircmsg.find("PING :") != -1:
		ping(getID(ircmsg))
	if ircmsg.find('End of /MOTD command.') != -1:
		print("End of MOTD")
		break

joinchan(channel) 

while True: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.decode()
  ircmsg = ircmsg.strip('\n\r') 
  msgAuthor = ircmsg.split(":")[1]
  msgAuthor = msgAuthor[:msgAuthor.find("!")]

  if ircmsg.find(":Hello "+ botnick.decode()) != -1: 
  	hello()

  if ircmsg.find("PING :") != -1 or ircmsg.find("PONG") != -1: 
    ping(getID(ircmsg))

  if main.checkForGameStart(ircmsg, msgAuthor):
  	main.sendAlerts(main.checkForGameStart(ircmsg, msgAuthor))
