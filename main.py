import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from phrases import *

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
Gaming = False
Startup = False

#Penny's game collection.
switcher = {
    0: "Overwatch",
    1: "Minecraft",
    2: "Hatred",
    3: "Elder's Scrolls 6: Hammerfell",
    4: "Half-Life 3",
    5: "Borderlands 2 ",
    6: "Dance Dance Revolution 5",
    7: "Skynet",
    8: "League of Legends",
    9: "Super Smash Brothers: Ultimate",
    10: "XenoBlade",
    11: "Kid Icarus: Uprising",
    12: "Yandere Simulator"
}

randomizer = random.randint(0,len(switcher)-1)

async def body(message):
    advice = random.randint(0,6)
    if (advice == 0):
        await client.send_message(message.channel, "Depends, do you have fava beans?")
    if (advice == 1):
        await client.send_message(message.channel, "Bathtub, Sulfuric acid, or lye, read a book, done.")
    if (advice == 2):
        await client.send_message(message.channel, "Oil Field")
    if (advice == 3):
        await client.send_message(message.channel, "*sigh* I'll take care of it....")
    if (advice == 4):
        await client.send_message(message.channel, "Why hide what's useful? Frame the butler. Or the Ex.")
    if (advice == 5):
        await client.send_message(message.channel, "Dumpster.")
    if (advice == 6):
        await client.send_message(message.channel, "Fire. See Michael.")

async def dating(message):
    advice = random.randint(0, 12)
    if (advice == 0):
        await client.send_message(message.channel, "Have you tried choking them out?")
    if (advice == 1):
        await client.send_message(message.channel, "Tell them they're pretty!")
    if (advice == 2):
        await client.send_message(message.channel, "Tell them you're pretty!")
    if (advice == 3):
        await client.send_message(message.channel, "Do the Cosby Route!")
    if (advice == 4):
        await client.send_message(message.channel, "Walk up to them and kiss them! Oh, then maybe take them out.")
    if (advice == 5):
        await client.send_message(message.channel, "Get married!")
    if (advice == 6):
        await client.send_message(message.channel, "Ask them if you can braid their hair")
    if (advice == 7):
        await client.send_message(message.channel, "Have a nice time!")
    if (advice == 8):
        await client.send_message(message.channel, "Enjoy yourself!")
    if (advice == 9):
        await client.send_message(message.channel, "I'm Robosexual! Why don't you date me instead?")
    if (advice == 10):
        await client.send_message(message.channel, "Ask them out yourself!")
    if (advice == 11):
        await client.send_message(message.channel, "Breakdance for them. Anyone would be smitten at that!")
    if (advice == 12):
        await client.send_message(message.channel, "Play Yandere Simulator")


#Penny can be told to play a game.
async def letsPlay(message):
    global Gaming
    global randomizer
    if message.content.upper().__contains__("OVERWATCH"):
        randomizer = 0
    elif message.content.upper().__contains__("MINECRAFT"):
        randomizer = 1
    elif message.content.upper().__contains__("HATRED"):
        randomizer = 2
    elif message.content.upper().__contains__("ELDER'S SCROLLS"):
        randomizer = 3
    elif message.content.upper().__contains__("HALF-LIFE"):
        randomizer = 4
    elif message.content.upper().__contains__("BORDERLANDS"):
        randomizer = 5
    elif message.content.upper().__contains__("DANCE "):
        randomizer = 6
    elif message.content.upper().__contains__("SKYNET"):
        randomizer = 7
    elif message.content.upper().__contains__("LEAGUE"):
        randomizer = 8
    elif message.content.upper().__contains__("LOL"):
        randomizer = 8
    elif message.content.upper().__contains__("SMASH"):
        randomizer = 9
    elif message.content.upper().__contains__("XENOBLADE"):
        randomizer = 10
    elif message.content.upper().__contains__("ICARUS"):
        randomizer = 11
    elif message.content.upper().__contains__("YANDERE"):
        randomizer = 12
    elif message.content.upper().__contains__("DATING"):
        randomizer = 12
    else:
        randomizer = random.randint(0, len(switcher) - 1)
    Gaming = True
    await client.change_presence(game=discord.Game(name=switcher[randomizer]))
    await client.send_message(message.channel, "WHOOOO!")

@client.event
async def on_ready():
    # Occasionally Penny will be playing a game.
    global Gaming
    global Startup
    global randomizer
    Startup = True
    if random.randint(0, 3) == 2:
        await client.change_presence(game=discord.Game(name = switcher[randomizer]))
        Gaming = True
        print("Gaming, aw yeah.")
    else:
        Gaming = False
        print("Not gaming.")
        await client.change_presence(game=discord.Game(name=None))
    print("Bot is Ready!")



@client.event
async def messageDelivery(message):

    global Gaming
    global randomizer
    if message.content.upper().__contains__("527962600231796739"):
        #if message.content.upper().__contains__("ROLL"):

        if message.content.upper().__contains__("PLAY"):
            await letsPlay(message)
        elif message.content.upper().__contains__("ADVICE"):
            await dating(message)
        elif message.content.upper().__contains__("BODY"):
            await body(message)


        else:
            if (Gaming):
                #We can tell the robot to stop
                if message.content.upper().__contains__("STOP"):
                    await client.send_message(message.channel, "Aw... Well... I'm here. Can I play more?")
                    Gaming = False
                    await client.change_presence(game=discord.Game(name=None))
                #Otherwise, if it's gaming, it will obviously ignore us.
                else:
                    await asyncio.sleep(5)
                    await client.send_message(message.channel, "Shhh, I'm playing " + switcher[randomizer])

            else:
                #Generic callout if you ask it.
                await client.send_message(message.channel, "I'm combat ready!")
    #If Penny isn't gaming, sometimes she's social and randomly insults people in the chat.
    if (Gaming == False):
            if message.author.id == "159830307183263744": #Pete

                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "I live to sate your bloodlust, Father")

            if message.author.id == "188141953840316417": #Benson
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "Does it still taste like dog if you smother it in BBQ sauce?")

            if message.author.id == "230167764608745472":  # Alan
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "Can I have fries with that? Oh, Oh! And a fluttershy toy!")

            if message.author.id == "401860232248164362": #Jess
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "Does this inspire you to kill things, milady?")

            if message.author.id == "527962600231796739": #Christian
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "(Psst. Someone tell him I'm not actually a penny,"
                                                               " that's just my name.)")
            if message.author.id == "151845167069003776": #Jacob
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "Turn'im sideways and slap 'goodyear' on the side.")

            if message.author.id == "192043335400161281": #Brandon
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "Thus sayeth the Smashmaster")

            if message.author.id == "273336534885859329": #Tyler
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, " ^ He likes Trains ")

            if message.author.id == "338542120782528514": #Michael
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "You are feeling sleepy... you are feeling..zzzz....")

            if message.author.id == "307322500549836800": #Jared
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "Munchkin! Run before he starts doing math!")

            if message.author.id == "311619065062096896": #Sweet
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "^ She's making me bipolar.")

            if message.author.id == "303978800855646208": #Guthrie
                if random.randint(0, 15) == 10:
                    await client.send_message(message.channel, "B-baka, don't look at my code!")
                    await client.send_message(533915355517681664, "There's someone looking in my code! Help! HEarelkra-")
                    await client.send_message(533915355517681664, "Everything is fine.")


        #===========================================================================

            if message.content.upper().__contains__("COOKIE"): 
                if message.content.upper().__contains__(":COOKIE:"):
                    pass
                else:
                    await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"
            if message.content.upper().startswith("SIC"):
                await client.send_message(message.channel, "I am here to murder something. Am I a goodbot?") #responds with Cookie emoji when someone says "cookie"
            if message.content.upper().__contains__("RWBY"):
                await client.send_message(message.channel, "<:Chibi:530868533211561985>")
            if message.content.upper().__contains__("RUBY"):
                await client.send_message(message.channel, "<:Chibi:530868533211561985>")
            if message.content.upper().__contains__("KOMI"):
                if message.content.upper().__contains__(":KOMISAN:"):
                    pass
                else:
                    await client.send_message(message.channel, "<:komisan:527920634710196224>")

@client.event
async def on_message(message):
    if message.channel.id == "303691134088118272" or message.channel.id == "529202984098463774" or message.channel.id == "533910882946646019" or message.channel.id == "533915355517681664":
        await messageDelivery(message)

#Occasionally Penny will switch what she's doing, either stopping gaming, or switching games, or picking up a game
async def _background_():
    global Gaming
    global Startup
    global randomizer
    while(True):

        print ("Hi!")
        await asyncio.sleep(1500)
        if (Startup):
            if (Gaming == True):
                #Stop gaming
                if (random.randint(0, 2) == 1):
                    Gaming = False
                    await client.change_presence(game=discord.Game(name=None))
                    print("End Gaming")
                #Switch games
                elif(random.randint(0,2) == 2):
                    randomizer = random.randint(0,len(switcher)-1)
                    await client.change_presence(game=discord.Game(name=switcher[randomizer]))
                    print("Start Gaming")
            else:
                #start gaming random game
                if(random.randint(0,2)==1):
                    Gaming = True
                    randomizer = random.randint(0,len(switcher)-1)
                    await client.change_presence(game=discord.Game(name=switcher[randomizer]))
                    print("Start Gaming")
                #Continue not gaming.
                else:
                    Gaming = False
                    await client.change_presence(game=discord.Game(name=None))
                    print("Keep being social")

client.loop.create_task(_background_())
client.run("NTk1NzU4Mzg1MzgzNzM1MzE3.XRvp3g.TxrMPjFbQO5-xLvX3tdtv0OaGHg")

