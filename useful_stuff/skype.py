import Skype4Py
client = Skype4Py.Skype()
client.Attach()
for chat in client.ActiveChats:
    chat.SendMessage('hello')