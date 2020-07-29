import discord
from irish_dictionary import irish_dictionary, gaeilge_gaeilge

token = 'NTk4NjA5NTQ0MjM4NzI3MTcw.XSZIlA.ufghXhgZFTNVqF6cQIXAgUhHpHA'

client = discord.Client()

@client.event
async def on_message(message):
    grammatical = ''
    suggestions = ''
    if message.author == client.user:
        return

    entries = []
    if len(message.content.split()) > 1:
        word = ' '.join(message.content.split()[1:]).lower()

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
        await message.channel.send("!eid for English to Irish")
        await message.channel.send("!fgb for Irish to English")
        await message.channel.send("!afb for Irish to Irish")

    for entry in entries:
        too_long = False
        if(len(entry)>2000):
            entry = entry[:2000]
            too_long = True
        await message.channel.send(entry)
        if too_long:
            await message.channel.send("**Entry shortened**. " +
                                        "Find original here: " + url)

    if not entries:
        if grammatical:
            await message.channel.send(grammatical)

        if message.content.split()[0] in ['!eid', '!fgb', '!afb']:
            await message.channel.send("No entry found")

        if suggestions:
            await message.channel.send(suggestions)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------')

client.run(token)
