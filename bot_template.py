import discord, random
from aioconsole import ainput
import BOTNAME_storage

client = discord.Client()

#On bot startup/ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    await client.change_presence(activity=discord.Game(name=f"use {BOTNAME_storage.PREFIX}help for help!"))

    while True:
        cmd = await ainput()
        await handleCline(cmd)

#On message received
@client.event
async def on_message(message):
    if message.author == client.user or message.content == None:
        return

    if message.guild == None:
        #Message is a dm
        print(f"DM received from {message.author}")

        #If not from dev, forward to dev
        if message.author.id != BOTNAME_storage.ADMIN_ID[0]:
            dmForward = f"Message from {message.author.name} (ID: {message.author.id}): {message.content}"
            dev = client.get_user(int(BOTNAME_storage.ADMIN_ID[0]))
            await sendMsg(dmForward,dev)

    #Check if admin command
    if message.author.id in BOTNAME_storage.ADMIN_ID:
        await adminCmd(message)

    #Check if prefixed command
    if message.content.startswith(BOTNAME_storage.PREFIX):
        await prefixed(message)
    else:
        await implicit(message)

async def prefixed(message):
    #### Message property variables ####
    cmd = msg.content[1:]
    args = cmd.split(' ')
    lower = cmd.lower()
    argsLower = lower.split(' ')
    author = msg.author
    channel = msg.channel
    guild = msg.guild
    ####################################

    if cmd == "help":
        await sendEmbed(BOTNAME_storage.HELP_EMBED, channel)

async def implicit(message):
    #### Message property variables ####
    text = msg.content
    lower = text.lower()
    channel = msg.channel
    author = msg.author
    ####################################

    if lower == "ping":
        await sendMsg("pong", channel)

#######################################################
################## Utility Functions ##################
#######################################################

#Parse and handle commands run from terminal
async def handleCline(cmd):
    clineArgs = cmd.split(' ')

    if clineArgs[0] == "announce":
        if len(clineArgs)<2:
            print("Must pass message to announce")
        else:
            try:
                #Try if channel ID was passed
                ancChan = client.get_channel(int(clineArgs[1]))
                ancMsg = ' '.join(clineArgs[2:])
            except:
                #If channel ID not passed
                ancChan = client.get_channel(BOTNAME_storage.MAIN_CHAT_ID)
                ancMsg = ' '.join(clineArgs[1:])
            await sendMsg(ancMsg,ancChan)

#Sends text to given channel
async def sendMsg(msg, channel):
    try:
        print(f"Sending message to {channel.name}: \n\t-\"{msg}\"")
        return await channel.send(msg)
    except:
        print(f"Error while attempting to send message to {channel.name}")

#Sends embed to given channel, Optional: pass content to go with it
async def sendEmbed(msg, channel, cntnt=None):
    try:
        await channel.send(content=cntnt,embed=msg)
        print(f"Sent embed to {channel.name}: {msg.title}")
    except:
        print(f"Error while attempting to send embed to {channel.name}")

#Sends a file from an absolute local path
async def sendFile(fp, channel, cntnt=None):
    imgFile = discord.File(fp)
    try:
        await channel.send(content=cntnt,file=imgFile)
        print(f"Sent file to {channel.name}: {fp}")
    except:
        print(f"Error while attempting to send {fp} to {channel.name}")

#Return url string of most recently posted image
async def getLastImg(chan):
    async for message in chan.history(limit=100):
        if len(message.attachments) >= 1:
            return message.attachments[0].url
    return None

client.run(BOTNAME_storage.TOKEN)
