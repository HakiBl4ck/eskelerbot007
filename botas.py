import amino
import random
import json
import sqlite3

email= "asterixyt@yahoo.com"
password= "Volcan1000"
comid= "6872133"
chatid= "e2a9bb4b-69bf-4c1c-8418-d3e753b4daf3"
client=amino.Client()
client.login(email=email,password=password)
print("\nLogeando...")
subclient=amino.SubClient(comId=comid,profile=client.profile)
print("\n Uniendose...")
subclient.join_chat(chatId=chatid)
print("\nUnido al chat")

@client.event("on_text_message")
def carala(data):
	if data.comId==6872133:
		msg_1 = data.message.content
		command = msg_1.split(' ')
		index = command[1]
		command = command[0]
		if subclient.get_chat_threads().title!=None and command=='!':
		    if index.lower()=="carta":
		        try:
		          imgs = ["LisaFUT.png", "JennieFUT.png", "NingningFUT.png", "JisooFUT.png", "RoseFUT.png", "YgFUT.png", "KarinaFUT.png", 
		          "SmFUT.png", "JypFUT.png", "HeejinFUT.png", "JinsoulFUT.png"]
		          elec = random.choice(imgs)
		          regex = open(elec, "rb")
		          subclient.send_message(chatId=data.message.chatId, message="" + elec, file=regex, fileType="image", embedTitle="@" + data.message.author.nickname)
		          print(f"Carta sacada por {data.message.author.nickname}")
		        except:
		          print(f"Pues no funciono, ntp")

@client.event("on_text_message")
def caracola(data):
	if data.comId==6872133:
		msg_1 = data.message.content
		command = msg_1.split(' ')
		index = command[1]
		command = command[0]
		if subclient.get_chat_threads().title!=None and command=='!':
		    if index.lower()=="ping":
		        try:
		          subclient.send_message(chatId=data.message.chatId,message="Pong",replyTo=data.message.messageId)
		          print(f"Awa k suba")
		        except:
		          print(f"k suba")

@client.event("on_text_message")
def caracola(data):
	if data.comId==6872133:
		msg_1 = data.message.content
		command = msg_1.split(' ')
		index = command[1]
		purple = command[2]
		command = command[0]
		if subclient.get_chat_threads().title!=None and command=='!':
		    if index.lower()=="id":
		        try:
		        	axa = client.get_from_code(purple[24:29]).objectId
		        	subclient.send_message(chatId=data.message.chatId, message="UID:" + axa)
		        	print(f"yeah glow")
		        except:
		        	print(f"no brah")