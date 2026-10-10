import discord
intents = discord.Intents(messages=True)
import json
import asyncio
import difflib
import math

from discord.ext import commands

#command prefix
client = commands.Bot(command_prefix = '!', intents=intents)

#stat calculation function
def evoscale(stat, evos):
    for i in range(evos):
        stat = round(stat * 1.95)
    return stat

#create second embed. contains signature ability
def create_sa_embed(fighter):
    stats = fighter["stats"]
    
    evocount = {"bronze": 3, "silver": 2, "gold": 1, "diamond": 0}
    max_atk = math.ceil(evoscale(int(stats["atk"]), evocount[fighter["rarity"]]) * 19.2)
    max_hp = math.ceil(evoscale(int(stats["hp"]), evocount[fighter["rarity"]]) * 19.2)
    max_fs = math.ceil(round((6 * max_atk + max_hp) * 7 / 60, 3) * 1.688)
        
    if fighter["element"] == "fire":
        if fighter["rarity"] == "bronze":
            embed = discord.Embed(
            title = "<:Bronze:684192916314652744> Bronze <:ele_fire:684054625757954066> Fire " + fighter["character"],
            colour = discord.Colour.red()
            )
        elif fighter["rarity"] == "silver":
            embed = discord.Embed(
            title = "<:Silver:684192916314390579> Silver <:ele_fire:684054625757954066> Fire " + fighter["character"],
            colour = discord.Colour.red()
            )
        elif fighter["rarity"] == "gold":
            embed = discord.Embed(
            title = "<:Gold:684192916327235657> Gold <:ele_fire:684054625757954066> Fire " + fighter["character"],
            colour = discord.Colour.red()
            )
        else:
            embed = discord.Embed(
            title = "<:Diamond:684192916125778021> Diamond <:ele_fire:684054625757954066> Fire " + fighter["character"],
            colour = discord.Colour.red()
            )
    
    elif fighter["element"] == "water":
        if fighter["rarity"] == "bronze":
            embed = discord.Embed(
            title = "<:Bronze:684192916314652744> Bronze <:ele_water:684192958827855883> Water " + fighter["character"],
            colour = discord.Colour.blue()
            )
        elif fighter["rarity"] == "silver":
            embed = discord.Embed(
            title = "<:Silver:684192916314390579> Silver <:ele_water:684192958827855883> Water " + fighter["character"],
            colour = discord.Colour.blue()
            )
        elif fighter["rarity"] == "gold":
            embed = discord.Embed(
            title = "<:Gold:684192916327235657> Gold <:ele_water:684192958827855883> Water " + fighter["character"],
            colour = discord.Colour.blue()
            )
        else:
            embed = discord.Embed(
            title = "<:Diamond:684192916125778021> Diamond <:ele_water:684192958827855883> Water " + fighter["character"],
            colour = discord.Colour.blue()
            )
            
    elif fighter["element"] == "air":
        if fighter["rarity"] == "bronze":
            embed = discord.Embed(
            title = "<:Bronze:684192916314652744> Bronze <:ele_wind:684192959293685781> Air " + fighter["character"],
            colour = discord.Colour.green()
            )
        elif fighter["rarity"] == "silver":
            embed = discord.Embed(
            title = "<:Silver:684192916314390579> Silver <:ele_wind:684192959293685781> Air " + fighter["character"],
            colour = discord.Colour.green()
            )
        elif fighter["rarity"] == "gold":
            embed = discord.Embed(
            title = "<:Gold:684192916327235657> Gold <:ele_wind:684192959293685781> Air " + fighter["character"],
            colour = discord.Colour.green()
            )
        else:
            embed = discord.Embed(
            title = "<:Diamond:684192916125778021> Diamond <:ele_wind:684192959293685781> Air " + fighter["character"],
            colour = discord.Colour.green()
            )

    elif fighter["element"] == "light":
        if fighter["rarity"] == "bronze":
            embed = discord.Embed(
            title = "<:Bronze:684192916314652744> Bronze <:ele_light:684192959931088913> Light " + fighter["character"],
            colour = discord.Colour.from_rgb(255,255,130)
            )
        elif fighter["rarity"] == "silver":
            embed = discord.Embed(
            title = "<:Silver:684192916314390579> Silver <:ele_light:684192959931088913> Light " + fighter["character"],
            colour = discord.Colour.from_rgb(255,255,130)
            )
        elif fighter["rarity"] == "gold":
            embed = discord.Embed(
            title = "<:Gold:684192916327235657> Gold <:ele_light:684192959931088913> Light " + fighter["character"],
            colour = discord.Colour.from_rgb(255,255,130)
            )
        else:
            embed = discord.Embed(
            title = "<:Diamond:684192916125778021> Diamond <:ele_light:684192959931088913> Light " + fighter["character"],
            colour = discord.Colour.from_rgb(255,255,130)
            )

    elif fighter["element"] == "dark":
        if fighter["rarity"] == "bronze":
            embed = discord.Embed(
            title = "<:Bronze:684192916314652744> Bronze <:ele_dark:684192958936776754> Dark " + fighter["character"],
            colour = discord.Colour.purple()
            )
        elif fighter["rarity"] == "silver":
            embed = discord.Embed(
            title = "<:Silver:684192916314390579> Silver <:ele_dark:684192958936776754> Dark " + fighter["character"],
            colour = discord.Colour.purple()
            )
        elif fighter["rarity"] == "gold":
            embed = discord.Embed(
            title = "<:Gold:684192916327235657> Gold <:ele_dark:684192958936776754> Dark " + fighter["character"],
            colour = discord.Colour.purple()
            )
        else:
            embed = discord.Embed(
            title = "<:Diamond:684192916125778021> Diamond <:ele_dark:684192958936776754> Dark " + fighter["character"],
            colour = discord.Colour.purple()
            )

    else:
        if fighter["rarity"] == "bronze":
            embed = discord.Embed(
            title = "<:Bronze:684192916314652744> Bronze <:ele_neutral:684192958710546467> Neutral " + fighter["character"],
            colour = discord.Colour.from_rgb(255,110,199)
            )
        elif fighter["rarity"] == "silver":
            embed = discord.Embed(
            title = "<:Silver:684192916314390579> Silver <:ele_neutral:684192958710546467> Neutral " + fighter["character"],
            colour = discord.Colour.from_rgb(255,110,199)
            )
        elif fighter["rarity"] == "gold":
            embed = discord.Embed(
            title = "<:Gold:684192916327235657> Gold <:ele_neutral:684192958710546467> Neutral " + fighter["character"],
            colour = discord.Colour.from_rgb(255,110,199)
            )
        else:
            embed = discord.Embed(
            title = "<:Diamond:684192916125778021> Diamond <:ele_neutral:684192958710546467> Neutral " + fighter["character"],
            colour = discord.Colour.from_rgb(255,110,199)
            )

    embed.add_field(name = "**" + fighter["ability"] + " (SA1)**", value = fighter["SA1"], inline = False)
    embed.add_field(name = "**" + fighter["ability"] + " (SA2)**", value = fighter["SA2"], inline = False)
    embed.add_field(name = "**STATS**", value = "**Min** <:fs:684948643610230835>" + stats["fs"] + " <:attack:684198430775443524>" + stats["atk"] + " <:health:684198431040078150>" + stats["hp"] +
                        "\n**Max** <:fs:684948643610230835>" + str(max_fs) + " <:attack:684198430775443524>" + str(max_atk) + " <:health:684198431040078150>" + str(max_hp), inline = False)
    embed.set_thumbnail(url = fighter["image"])

    return embed


#print when bot is ready
@client.event
async def on_ready():
    print('Bot is ready.')

#fighter command. sends one embed (detailed abilites)
@client.command()
async def fighter(context, *, fighter_name):
    # load fighter database
    api_file = open("fighters.json")
    fighter_database = json.load(api_file)
    fighter_name = fighter_name.lower().replace(" ", "")
    if fighter_name in fighter_database:
        fighter = fighter_database[fighter_name]
        embed = create_sa_embed(fighter)
        await context.send('**__' + fighter["name"] + '__**',embed = embed)
    elif len(difflib.get_close_matches(fighter_name, fighter_database.keys(), 1, 0.9)) > 0:
        fighter = fighter_database[difflib.get_close_matches(fighter_name, fighter_database.keys(), 1)[0]]
        embed = create_sa_embed(fighter)
        await context.send('**__' + fighter["name"] + '__**', embed=embed)
    else:
        # load alias
        alias = open("alias.txt", "r")
        success = False
        aliaslist = alias.read().splitlines()
        for line in aliaslist:
            line = line.split(",")
            if fighter_name in line:
                fighter = fighter_database[line[0]]
                embed = create_sa_embed(fighter)
                await context.send('**__' + fighter["name"] + '__**', embed=embed)
                success = True
                break
        alias.close()
        if not success:
            if "@" in fighter_name:
                fighter_name = "that fighter"
            message = await context.send("unfortunately, " + fighter_name + " does not exist")
            await asyncio.sleep(3)
            await message.delete()
    api_file.close()


#alias command. sends a list of aliases of give fighter
@client.command()
async def alias(context, *, fighter_name):
    # load fighter database
    api_file = open("fighters.json")
    fighter_database = json.load(api_file)
    f = open("alias.txt", "r")
    fighter_name = fighter_name.lower().replace(" ", "")
    if fighter_name in fighter_database:
        fighter = fighter_database[fighter_name]
        aliaslist = f.read().splitlines()
        for line in aliaslist:
            line = line.split(",")
            if line[0] == fighter_name:
                if len(line) == 2:
                    await context.send(fighter["name"] + " is also known as " + line[1])
                elif len(line) > 2:
                    aka_str = ""
                    for i in range(1, len(line) - 1):
                        aka_str += line[i] + ", "
                    aka_str = aka_str + "and " + line[len(line) - 1]
                    await context.send(fighter["name"] + " is also known as " + aka_str)
                else:
                    await context.send(fighter["name"] + " has no aliases")
    else:
        message = await context.send("unfortunately, " + fighter_name + " does not exist")
        await asyncio.sleep(3)
        await message.delete()
    f.close()
    api_file.close()
    
#wiki command. sends a primative wiki link of the fighter specified
@client.command()
async def wiki(context, *, fighter_name):
    # load fighter database
    api_file = open("fighters.json")
    fighter_database = json.load(api_file)
    fighter_name = fighter_name.lower().replace(" ", "")
    if fighter_name in fighter_database:
        fighter = fighter_database[fighter_name]
        suffix = fighter["name"].replace(" ", "_")
        await context.send("https://skullgirlsmobile.fandom.com/wiki/" + suffix)
    elif len(difflib.get_close_matches(fighter_name, fighter_database.keys(), 1, 0.9)) > 0:
        fighter = fighter_database[difflib.get_close_matches(fighter_name, fighter_database.keys(), 1)[0]]
        suffix = fighter["name"].replace(" ", "_")
        await context.send("https://skullgirlsmobile.fandom.com/wiki/" + suffix)
    else:
        # load alias
        alias = open("alias.txt", "r")
        success = False
        aliaslist = alias.read().splitlines()
        for line in aliaslist:
            line = line.split(",")
            if fighter_name in line:
                fighter = fighter_database[line[0]]
                suffix = fighter["name"].replace(" ", "_")
                await context.send("https://skullgirlsmobile.fandom.com/wiki/" + suffix)
                success = True
                break
        alias.close()
        if not success:
            if fighter_name == "critless" or fighter_name == "critlessskilltree":
                await context.send("https://skullgirlsmobile.fandom.com/wiki/Critless_Skill_Tree")
            elif fighter_name == "fortune'sfavor" or fighter_name == "fortunesfavor":
                await context.send("https://skullgirlsmobile.fandom.com/wiki/Fortune's_Favor")
            elif "@" in fighter_name:
                fighter_name = "that fighter"
            message = await context.send("unfortunately, " + fighter_name + " does not exist")
            await asyncio.sleep(3)
            await message.delete()
    api_file.close()
    

#whitelist command. whitelists a channel for details and stats command
@client.command()
async def whitelist(context):
    if context.guild:
        if context.author.guild_permissions.ban_members:
            f = open("whitelist.txt", "r+")
            channel_list = f.read().replace("[", "").replace("]","").replace("\'","").split(", ")
            if str(context.channel.id) in channel_list:
                message = await context.send("This channel is already whitelisted!")
                await asyncio.sleep(3)
                await message.delete()
                f.close()
            else:
                f.write(", " + str(context.channel.id))
                await context.send("Channel whitelisted!")
                f.close()
        else:
            message = await context.send("Only Moderators can whitelist channels!")
            await asyncio.sleep(3)
            await message.delete()
    else:
        message = await context.send("You can only use this command in servers!")
        await asyncio.sleep(3)
        await message.delete()


#blacklist command. removes a channel from whitelist        
@client.command()
async def blacklist(context):
    if context.guild:
        if context.author.guild_permissions.ban_members:
            f = open("whitelist.txt", "r")
            channel_list = f.read().replace("[", "").replace("]","").replace("\'","").split(", ")
            if str(context.channel.id) in channel_list:
                for channel_index in range(0,len(channel_list)-1): 
                    if channel_list[channel_index] == str(context.channel.id):
                        del channel_list[channel_index]
                f.close()
                f = open("whitelist.txt", "w")
                f.write(str(channel_list))
                await context.send("This channel has been removed from the whitelist!")
                f.close()
                
            else:
                message = await context.send("This channel is not whitelisted!")
                await asyncio.sleep(3)
                await message.delete()
                f.close()
        else:
            message = await context.send("Only Moderators can blacklist channels!")
            await asyncio.sleep(3)
            await message.delete()
    else:
        message = await context.send("You can only use this command in servers!")
        await asyncio.sleep(3)
        await message.delete()


#credits
@client.command()
async def credits(context):
    embed = discord.Embed(
        title = "Credits",
        colour = discord.Colour.from_rgb(0,0,0)
        )
    embed.add_field(name = "Big Thanksies Wall",
                    value = "Created by Fel\nThank you to everyone who helped create this bot!\nKrazete: Images and Stats (https://sgm.netlify.com)\nSheik: Valentine, Fukua, Annie\nCriptobeta: Robo\nAnimetrix: Squigly\nLadders: Peacock\nEsdisi: Parasoul\nCpt. Weeabooo, Satyrical: Painwheel\nCribz users: Testing\nMsAkemi and Cade1: Data Collection\nLink to Privacy Policy: https://github.com/SGMFel/sgm/blob/master/StanleyPrivacyPolicy.txt"
                    )
    await context.send(embed = embed)

@client.event
async def on_command_error(context,error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        message = await context.send("This command does not exist!")
        await asyncio.sleep(3)
        await message.delete()
        
client.run('add bot code here')
