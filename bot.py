import discord, asyncio, datetime, os, main, db

from matplotlib.pyplot import title
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


client = discord.Client(command_prefix=':', case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Online"), status=discord.Status.idle)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!help'):
        embeded = discord.Embed(title="Help information", description="How to use the bot", color=0xffffff)
        embeded.add_field(name="`!register <username> <password>`", value="Registration for your account")
        embeded.add_field(name="`!feed`", value="Feeding your cat")
        embeded.add_field(name="`!timeset <--:--> or disable`", value="Set time your cat feeder or you cat disable it \n note: use 24 hours format")
        embeded.add_field(name="`!name <your cat name>`", value="Give name for your cat")
        await message.channel.send(embed=embeded)
        
    

    if message.content.lower().startswith('!register'):
        if not message.guild:
            x = message.content.lower().split(" ")
            username = x[1]
            password = x[2]
            id = message.author.id
            check = db.show_user(id)
            check2 = db.show_user2(username)
            if check:
                await message.channel.send(f"Your account already exists")
            elif check2:
                await message.channel.send(f"Account with that username already exists")
            else:
                db.register(username, password, id)
                await message.channel.send(f"Registration complete for `{message.author}` \nType `!name <cat name>` for give name your cat")
        else:
            await message.channel.send(f"Registration only on dm")

    if message.content.lower().startswith('!feed'):
        id = message.author.id
        check = db.show_user(id)
        if check:
            catname = ''.join(db.show_cat_name(id))
            db.status_set2("On", id)
            x = await message.channel.send(f'Feeding {catname} \n■□□□□')
            await asyncio.sleep(1)
            await x.edit(content=f"Feeding {catname} \n■■□□□")
            await asyncio.sleep(1)
            await x.edit(content=f"Feeding {catname} \n■■■□□")
            await asyncio.sleep(1)
            await x.edit(content=f"Feeding {catname} \n■■■■□")
            await asyncio.sleep(1)
            await x.edit(content=f"Feeding {catname} \n■■■■■")
            await asyncio.sleep(1)
            db.status_set2("Off", id)
            await x.edit(content=f"Done feeding {catname}")
            await asyncio.sleep(1)
        else:
            await message.channel.send(f"You dont have account, please register first")
            
    elif message.content.lower().startswith('!timeset'):
        id = message.author.id
        check = db.show_user(id)
        if check:
            x = message.content.lower().split(" ")
            if x[1] == "disable":
                db.time_set2("", id)
                await message.channel.send("Timeset disable")
            else:
                res = True
                try:
                    res = bool(datetime.strptime(x[1], "%H:%M"))
                except ValueError:
                    res = False
                if res:
                    db.time_set2(x[1], id)
                    catname = ''.join(db.show_cat_name(id))
                    await message.channel.send(f"Timeset to {x[1]} for {catname}")
                else:
                    await message.channel.send(f"Wrong format use `!timeset --:-- or disable`")
        else:
            await message.channel.send(f"You dont have account, please register first")
    elif message.content.lower().startswith('!name'):
        id = message.author.id
        check = db.show_user(id)
        if check:
            x = message.content.lower().split(" ")
            catname = ''.join(str(e) for e in (x[1:]))
            db.set_cat_name(catname, id)
            await message.channel.send(f"your cat name now is `{catname}`")
        else:
            await message.channel.send(f"You dont have account, please register first")
    
main.starter()
client.run(os.getenv('TOKEN'))