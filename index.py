from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

stop = False
api_id = "Paste your App ID here"
api_hash = "Paste your App Hash here"
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
print('Succesfully login into your account.')

@client.on_message(filters.command('spam', prefixes="/") & filters.me)
def message_handler(client, message):
    global stop
    global times
    args = message.text.split(' ')
    if args[1] == 'stop':
        stop = True
        client.send_message(message.chat.id, 'You succesfully disabled spam.')
    if check_for_number(args[1]) == True: times = int(args[1])
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

@client.on_message(filters.command('help', prefixes="/") & filters.me)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, 'Use: /spam <amount of messages> <message>\nBy @shineforever2.')

@client.on_message(filters.command('status', prefixes='/') & filters.me)
def message_handler(client, message):
    client.edit_message_text(message.chat.id, message.id, 'Bot Works✅...')

client.run()