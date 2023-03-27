from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

stop = False
api_id = "Paste your API ID here"
api_hash = "Paste your API Hash here"
times = 0

def check_for_number(str):
    try:
        str = int(str)
        return True
    except ValueError:
        return False

client = Client('user_login', api_id, api_hash)

client.start()
client.stop()
print('Succefull login')

@client.on_message(filters.command('spam', prefixes="/") & filters.me)
def message_handler(client, message):
    global stop
    global times
    args = message.text.split(' ')
    try:
        if args[1] in '1234567890':
            if check_for_number(args[1]) == True: times = int(args[1])
    except IndexError:
        client.edit_message_text(message.chat.id, message.id, 'Use: /spam <amount of messages> <message>\nBy @shineforever2.')
        args.append('None')
    if args[1] == 'stop':
        stop = True
        client.send_message(message.chat.id, 'Succesfully disabled spam.')
    args.pop(0)
    args.pop(0)
    if times >= 1:
        client.edit_message_text(message.chat.id, message.id, 'Spam Starts!')
        while times >= 1:
            try:
                if stop == True:
                    times = 0
                    stop = False
                    break
                client.send_message(message.chat.id, ' '.join(args))
                sleep(1/15)
            except FloodWait as e:
                sleep(e.x)
            times -= 1

@client.on_message(filters.command('status', prefixes='/') & filters.me)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, 'Bot Works✅')

client.run()