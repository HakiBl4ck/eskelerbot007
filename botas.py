import amino
import random
import json
import sqlite3

email= "***************"
password= "***"
comid= 6872133
chatid= "e2a9bb4b-69bf-4c1c-8418-d3e753b4daf3"
client=amino.Client()
client.login(email=email,password=password)
print("\nLogeando...")
subclient=amino.SubClient(comId=comid,profile=client.profile)
print("\n Uniendose...")
subclient.join_chat(chatId=chatid)
print("\nUnido al chat")

admins = ("cf5dbd9a-208a-4c10-a541-e86be8b6591", "fc83578c-706a-44ef-bc2a-e2c119f2fe92", "c438815b-9265-44ee-a104-e7297b6656e5",
	"81f8bacd-3c84-45f9-9d1c-5d069665b4e9")

@client.event("on_text_message")
def carala(data):
	if data.comId==6872133:
		msg_1 = data.message.content
		command = msg_1.split(' ')
		index = command[1]
		command = command[0]
		if subclient.get_chat_threads().title!=None and command=='!':
		    if index.lower()=="carta" and data.message.author.userId in admins:
		        try:
		          imgs = ["LisaFUT.png", "JennieFUT.png", "NingningFUT.png", "JisooFUT.png", "RoseFUT.png", "YgFUT.png", "KarinaFUT.png", 
		          "SmFUT.png", "JypFUT.png", "HeejinFUT.png", "JinsoulFUT.png"]
		          elec = random.choice(imgs)
		          regex = open(elec, "rb")
		          subclient.send_message(chatId=data.message.chatId, message="" + elec, file=regex, fileType="image", embedTitle="@" + data.message.author.nickname)
		          print(f"Carta sacada por {data.message.author.nickname}")
		        except:
		          subclient.send_message(chatId=data.message.chatId, message="Lo sentimos, comando exclusivo para el staff :)")
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
		        	axa = client.get_from_code(purple).objectId
		        	subclient.send_message(chatId=data.message.chatId, message="UID:" + axa)
		        	print(f"yeah glow")
		        except:
		        	print(f"no brah")
