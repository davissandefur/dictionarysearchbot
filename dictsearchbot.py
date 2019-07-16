import discord
from irish_dictionary import irish_dictionary, gaeilge_gaeilge

token = 'NTk4NjA5NTQ0MjM4NzI3MTcw.XSZIqQ.7Tx-2rrmyc7T2-_ihoC0g3YIYTM'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    entries = []
    if len(message.content.split()) > 1:
        word = message.content.split()[1].lower()

    if message.content.startswith('!eid'):
        entries, suggestions, grammatical, url = irish_dictionary(word,
                                        'English', 'english')

    if message.content.startswith('!fgb'):
        entries, suggestions, grammatical, url = irish_dictionary(word,
                                        'Irish', 'english')

    if message.content.startswith('!afb'):
        entries, suggestions, grammatical, url = irish_dictionary(word,
                                        'Irish', 'english')
        entries = gaeilge_gaeilge(word)

    if message.content.startswith('!help'):
        await client.send_message(message.channel, "!eid for English to Irish")
        await client.send_message(message.channel, "!fgb for Irish to English")
        await client.send_message(message.channel, "!afb for Irish to Irish")

    for entry in entries:
        too_long = False
        if(len(entry)>2000):
            entry = entry[:2000]
            too_long = True
        await client.send_message(message.channel,entry)
        if too_long:
            await client.send_message(message.channel, "**Entry shortened**. " +
                                        "Find original here: " + url)

    if not entries:
        if grammatical:
            await client.send_message(message.channel, grammatical)

        else:
            await client.send_message(message.channel, "No entry found.")
            await client.send_message(message.channel, suggestions)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(token)
