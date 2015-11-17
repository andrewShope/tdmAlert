import time
import socket

server = "irc.quakenet.org".encode() # Server
channel = "#nactf.ql".encode() # Channel
botnick = "bigPoppa".encode() # Your bots nick


def ping(pingID): # This is our first function! It will respond to server Pings.
	ircsock.send(b"PONG :" + pingID.encode() +  b"\r\n")
	print("PONG :" + pingID)

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send(b"PRIVMSG "+ chan + b" :"+ msg + b"\n")

def joinchan(chan): # This function is used to join channels.
  ircsock.send(b"JOIN "+ chan +b"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send(b"PRIVMSG "+ channel + b" :Hello!\n")
  print(botnick.decode() + ": Hello!")

def getID(msg):
	msg = msg
	msgList = msg.split(':')
	return msgList[1]

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # Here we connect to the server using the port 6667
ircsock.connect((server, 6667))
print("Connected")

while(True):
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.decode()
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)
	if ircmsg.find('Found your hostname') != -1:
		print("Found")
		break

#Here we actually assign the nick to the bot		
ircsock.send(b"NICK "+ botnick + b"\r\n") 
ircsock.send(b"USER "+ botnick + b" * 8" + b" :" + botnick +b"\r\n")

while(True):
	ircmsg = ircsock.recv(2048)
	ircmsg = ircmsg.decode('ascii')
	ircmsg = ircmsg.strip('\n\r')
	print(ircmsg)
	if ircmsg.find("PING :") != -1:
		ping(getID(ircmsg))
	if ircmsg.find('End of /MOTD command.') != -1:
		print("End of MOTD")
		break

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.decode()
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find(":Hello "+ botnick.decode()) != -1: # If we can find "Hello Mybot" it will call the function hello()
  	hello()

  if ircmsg.find("PING :") != -1 or ircmsg.find("PONG") != -1: # if the server pings us then we've got to respond!
    ping(getID(ircmsg))
