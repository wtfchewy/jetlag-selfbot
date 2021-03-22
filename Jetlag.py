#!/usr/bin/env python
# -*- coding: utf-8 -*-

from discord import Embed
from discord.ext.commands import bot
from discord.ext import commands
import discord.guild
import requests
import discord
import asyncio
import random
import json
import time
import datetime
import os
import smtplib, ssl
import discord_webhook
import colorama

from discord_webhook import DiscordWebhook, DiscordEmbed

# Config.json
with open('config.json', 'r') as handle:
    config = json.load(handle)
    token = (config["token"])
    key = (config["key"])
    prefix = (config["prefix"])
    version = (config["version"])
    thumbnail = (config["thumbnail"])
    footer = (config["footer"])
    webhookurl = (config["webhook"])
    mailname = (config["mailname"])
    mailpass = (config["mailpass"])
    phonenumber = (config["phonenumber"])

deletetimer = 100
errorcolor = 0x9933ff
color = 0x9933ff


# Bot establishment
bot = commands.Bot(description="Jetlag", command_prefix=prefix, self_bot=True)
bot.remove_command('help')
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# Connect event
@bot.event
async def on_connect():
    print("")
    print("	                )  (              ")
    print("	   (     (   ( /(  )\    )  (  (  ")
    print("	   )\   ))\  )\())((_)( /(  )\))( ")
    print("	  ((_) /((_)(_))/  _  )(_))((_))\ ")
    print("	 _ | |(_))  | |_  | |((_)_  (()(_)")
    print("	| || |/ -_) |  _| | |/ _` |/ _` | ")
    print("	 \__/ \___|  \__| |_|\__,_|\__, | ")
    print("	                           |___/  ")
    print("")
    print("      ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
    print("                Connected as: " + bot.user.name)
    print("         ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯   ")
    print("                      [" + version + "]        ")
    print("")

# Main Command
@bot.command(aliases=['help'])
async def mirage(ctx):
    embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ𝕁𝔼𝕋𝕃𝔸𝔾", description=
    "─────────────────────────────────────── \n"
    "**Prefix** » " + prefix + "\n"
    "**Version** » " + version + "\n"
    "─────────────────────────────────────── \n"
    "\n"
    "**IP COMMANDS** (5) \n"
    "This category will have a mixture of ip related commands. \n"
    " \n"
    "**GENERAL COMMANDS** (6) \n"
    "This category will consist of normal commands to use. \n"
    " \n"
    "**FUN COMMANDS** (6) \n"
    "This category will consist of fun commands like memes etc.. \n"
    " \n"
    "**MASSACRE COMMANDS** (5) \n"   
    "fucking massacre children \n"
    " \n"
    "───────────────────────────────────────", color=0x9933ff, )
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()


@bot.command(aliases=['IP', "Ip", "ip"])
async def IPTools(ctx):
    embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤIP Tools", description=
    "─────────────────────────────────────── \n"
    "**Prefix:** " + prefix + "\n"
    "─────────────────────────────────────── \n"
    "\n"
    "**IPLOOKUP [IP/HOST]** \n"
    "Geo locates an IP Address \n"
    "\n"
    "**PORTSCAN [IP/HOST]** \n"
    "Scans for ports on an IP or HOST \n"
    "\n"
    "**RESOLVE [IP/HOST]** \n"
    "Resolves IP Address from HOST \n"
    "\n"
    "**PROXYCHECKER [IP/HOST]** \n"
    "Checks proxys on an IP Address \n"
    "\n"
    "**DOMAINCHECK [DOMAIN]** \n"    
    "Will check if the domain you enter is avaliable \n"
    "\n"
    "───────────────────────────────────────", color=0x9933ff, )
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()


@bot.command(aliases=['General', "general"])
async def GeneralTools(ctx):
    embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤGeneral Tools", description=
    "─────────────────────────────────────── \n"
    "**Prefix:** " + prefix + "\n"
    "─────────────────────────────────────── \n"
    "\n"
    "**SCREENSHOT [WEBSITE URL]** \n"
    "This will take a screenshot of a website (https/http) \n"
    "\n"
    "**COVID** \n"
    "Displays the worldwide stats for covid-19 \n"
    "\n"
    "**URLSHORTEN [URL]** \n"        
    "This will Shorten urls \n"
    "\n"
    "**QUESTION/ASK [QUESTION IN QUOTATIONS]** \n"
    "Will try to answer any question \n"
    "\n"
    "**USERINFO [@USER]** \n"
    "Checks information of users discord account \n"
    "\n"
    "**AVATAR [@USER]** \n"
    "Displays profile picture of user \n"
    "\n"
    "**2MINERSETC [ETC TOKEN]** \n"
    "Shows mining stats of the token provided \n"
    "\n"
    "───────────────────────────────────────", color=0x9933ff, )
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()


@bot.command(aliases=['Fun', "fun"])
async def FunTools(ctx):
    embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤFun Tools", description=
    "─────────────────────────────────────── \n"
    "**Prefix:** " + prefix + "\n"
    "─────────────────────────────────────── \n"    
    "\n"
    "**PENIS [@USER]** \n"
    "Looks down there pants \n"
    "\n"
    "**DADJOKE** \n"
    "Generates a shit joke \n"
    "\n"
    "**8BALL [QUESTION]** \n"
    "Gives you a random awnser \n"
    "\n"
    "**GIF [KEYWORD]** \n"
    "Search for a gif \n"
    "\n"
    "**DEFINE [WORD]** \n"      
    "Will give you the definition of the word \n"
    "\n"
    "**REVERSE [PHRASE]** \n"    
    "Reverses text or phrase\n"
    "\n"
    "**TRUMPTWEET [PHRASE]** \n"
    "Makes trump tweet a word or phrase\n"
    "\n"
    "───────────────────────────────────────", color=0x9933ff, )
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()

@bot.command(aliases=['Massacre', "massacre"])
async def MassacreTools(ctx):
    embed = discord.Embed(title="ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤMassacre Tools", description=
    "─────────────────────────────────────── \n"
    "**Prefix:** " + prefix + "\n"
    "─────────────────────────────────────── \n"
    "\n"
    "**NUKE** \n"
    "Nukes a chat with blank characters\n"
    "\n"
    "**BANLIST** \n"
    "Displays all users banned in a server \n"
    "\n"
    "**EMOJILAGGER/ARABLAGGEr** \n"
    "Spams emojis or arab letters \n"
    "\n"
    "**SPAM [WORD OR PHRASE]** \n"    
    "Spams message or word\n"
    "\n"
    "**EMAILSPAMMER [EMAIL] [COUNT] [PHRASE]** \n"
    "Spams people inboxs with phrase or word\n"
    "\n"
    "───────────────────────────────────────", color=0x9933ff, )
    embed.set_footer(text=footer)
    embed.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()

#SMS START
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#SMS END


#DISCORD WEB HOOKS START
#--------------------------------------------------------------------------------------------------
@bot.event
async def on_message_delete(message):
    guild = message.guild
    if not guild:
        if message.author.id != bot.user.id:
            print(current_time + f' | {message.author} deleted a message | Channel: {message.channel} | Message: {message.content} | Guild: {message.guild}')
            webhook = DiscordWebhook(url=webhookurl)
            embed = DiscordEmbed(title=f'[MSG DELETE]', description=f""
                                                                 f"{message.author} deleted a message | Channel: {message.channel} | Message: {message.content} | Guild: {message.guild}"
                                                                 f"", color=color)
            embed.set_footer(text="Jetlag | Logged in as: " + bot.user.name)
            webhook.add_embed(embed)
            response = webhook.execute()
#--------------------------------------------------------------------------------------------------
def errorprint(message
               ):
    print(current_time + " | " + "[Warning]" + " | " + message)
    webhook = DiscordWebhook(url=webhookurl)
    embed = DiscordEmbed(title=f'[WARNING]', description=f""
                                                         f"{message}"
                                                         f"", color=errorcolor)
    embed.set_footer(text="Jetlag | Logged in as: " + bot.user.name)
    webhook.add_embed(embed)
    response = webhook.execute()
#--------------------------------------------------------------------------------------------------
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    guild = message.guild
    if not guild:
        if message.author.id != bot.user.id:
            print(
            current_time + f' | {message.author} sent a message | Channel: {message.channel} | Message: {message.content}')
            webhook = DiscordWebhook(url=webhookurl)
            embed = DiscordEmbed(title=f'[MSG SENT]', description=f""
                                                                     f"{message.author} sent a message | Channel: {message.channel} | Message: {message.content}"
                                                                    f"", color=color)
            embed.set_footer(text="Jetlag | Logged in as: " + bot.user.name)
            webhook.add_embed(embed)
            response = webhook.execute()     
#--------------------------------------------------------------------------------------------------
#DISCORD WEB HOOKS END

#IP COMMANDS START
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['whois'])
async def iplookup(ctx, *, ipaddress):
    print(current_time + " Command 'IP' has been used by " + bot.user.name)
    p = requests.post('http://ip-api.com/json/' + ipaddress)
    if '"status":"success"' in p.text:
        embed = discord.Embed(color=discord.Color.red())
        embed = discord.Embed(title=f" __**INFO**__ ",
                              description=f"IP | **{ipaddress}**\n"
                                          f" Country | **{p.json()['country']}**\n"
                                          f" Country Code | **{p.json()['countryCode']}**\n"
                                          f" Region | **{p.json()['region']}**\n"
                                          f" Region Name | **{p.json()['regionName']}**\n"
                                          f" City | **{p.json()['city']}**\n"
                                          f" Timezone | **{p.json()['timezone']}**\n"
                                          f" Zip | **{p.json()['zip']}**\n"
                                          f" ISP | **{p.json()['isp']}**",
                              color=0x9933ff)
        await ctx.send(embed=embed, delete_after=deletetimer)
    else:
        await ctx.send("Invalid IP address.")
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def portscan(ctx, ipadd: str):
    print(current_time + " Command 'portscan' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/portscanner?key=" + key + f"&host={ipadd}").text
    embed = discord.Embed(title=f" __**Port Scan For {ipadd}**__ ", color=0x9933ff)
    embed.add_field(name="Open Ports: ", value=f"{r}", inline=False)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def resolve(ctx, HOST):
    print(current_time + " Command 'resolve' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/dnsresolver?key=" + key + f"&host={HOST}").text
    embed=discord.Embed(title=f" __**IP for {HOST}**__ ", description="** **", color=0x9933ff)
    embed.add_field(name=f"**{r}**", value=f"** **", inline=False)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def proxycheck(ctx, IP):
    print(current_time + " Command 'ProxyCheck' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/proxydetector?key=&ip={IP}").text
    embed=discord.Embed(title=f" __**{IP} Check**__ ", description=f"{r}", color=0x9933ff)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['domaincheck'])
async def domain_checker(ctx, domain):
    print(current_time + " Command 'Domain Checker' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/domainchecker?key=" + key + f"&domain={domain}").text
    embed = discord.Embed(title=f" __**Domain Checker**__ ", description=f"{r}", color=0x9933ff)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
#IP COMMANDS END

#GERNAL COMMANDS START
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['ss'])
async def screenshot(ctx, domain):
    print(current_time + " Command 'Screenshot' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/createscreenshot?key=" + key + f"&url={domain}").text
    embed = discord.Embed(title=f" __**{domain} Screenshot**__ ", description=f"{r}", color=0x9933ff)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['corona'])
async def covid(ctx):
    print(current_time + " Command 'covid' has been used by " + bot.user.name)
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    embed = discord.Embed(title='Updated Just Now:', description=f"Deaths | **{res[totald]}**\nConfirmed | **{res[totalc]}**\nRecovered | **{res[totalr]}**") # create embed
    embed.colour = (0x000000)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['url'])
async def urlshorten(ctx, website):
    print(current_time + " Command 'URL Shortener' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/urlshortener?key=" + key + f"&url={website}").text
    embed = discord.Embed(title=f" URL Shortener ", description=f"{r}", color=0x9933ff)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['question'])
async def ask(ctx, question):
    print(current_time + " Command Question has been used by " + bot.user.name)
    r = requests.get(f"https://api.wolframalpha.com/v1/result?appid=85PTL6-9YEK2RE4HQ&i=" + question + f"%3F").text
    embed = discord.Embed(title=f" __**{question}?**__ ", description=f"{r}", color=0x9933ff)
    await ctx.send(embed=embed, delete_after=deletetimer)
#--------------------------------------------------------------------------------------------------
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    print(current_time + " Command 'userinfo' has been used by " + bot.user.name)
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.red(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    print(member.top_role.mention)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=["av"])
async def avatar(ctx, *,  avamember : discord.Member=None):
    print(current_time + " Command 'Avatar' has been used by " + bot.user.name)
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['2minersetc'])
async def twominersetc(ctx, wallet):
    await ctx.message.delete()
    print(current_time + " Command 'ETC Check' has been used by " + bot.user.name)
    r = requests.get(f"https://etc.2miners.com/api/accounts/{wallet}")
    res = r.json()
    workersoff = 'workersOffline'
    workerson = 'workersOnline'
    workers = 'workersTotal'
    curhash = 'currentHashrate'
    avghash = 'hashrate'

    embed = discord.Embed(title=f'2Miners ETC Pool', description=f"─────────────────────\nTotal Workers: **{res[workers]}**\nOnline Workers: **{res[workerson]}**\nOffline Workers: **{res[workersoff]}**\n ─────────────────────\nCurrent Hashrate: **{res[curhash]}** MH/s\nAverage Hashrate: **{res[avghash]}** MH/s\n─────────────────────")  # create embed
    embed.set_footer(text=f'{wallet}')
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/628246781045637160/775449724769402880/clipart2771936.png")
    embed.colour = (0xFC5C46)
    await ctx.send(embed=embed, delete_after=deletetimer)
#--------------------------------------------------------------------------------------------------
#GENERAL COMMANDS END

#FUN COMMANDS START
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['dong', 'penis', 'cock', 'winky', 'shlong'])
async def dick(ctx, *, user: discord.Member = None):
    print(current_time + " Command 'dick' has been used by " + bot.user.name)
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", color=0x9933ff)
    await ctx.send(embed=em, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['shitjoke'])
async def dadjoke(ctx):
    print(current_time + " Command 'joke' has been used by " + bot.user.name)
    await ctx.send(requests.get(url="https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()['joke'])
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    print(current_time + " Command '8ball' has been used by " + bot.user.name)
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=0x9933ff)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/720348929043988572/722447275561058314/1200px-8-Ball_Pool.svg.png")
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['gif'])
async def gif_finder(ctx, keyword):
    print(current_time + " Command 'gif finder' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/gif?key=" + key + f"&keyword={keyword}").text
    await ctx.send(f"{r}")
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(aliases=['define', 'word'])
async def dictionary(ctx, word):
    print(current_time + " Command 'dictionary' has been used by " + bot.user.name)
    r = requests.get(f"https://api.c99.nl/dictionary?key=" + key + f"&word={word}").text
    embed = discord.Embed(title=f" __**{word} definition**__ ", description=f"{r}", color=0x9933ff)
    await ctx.send(embed=embed, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def reverse(ctx, text):
    await ctx.send(text[::-1])
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def trumptweet(ctx, *, text):
    await ctx.message.delete()
    print(current_time + "Command 'trumptweet' has been used by " + bot.user.name)
    p = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}")

    embed=discord.Embed()
    embed.set_image(url = p.json()['message'])
    await ctx.send(embed=embed, delete_after=deletetimer)
#--------------------------------------------------------------------------------------------------
#FUN COMMANDS END

@bot.command()
async def cl(ctx, amount=999):  # /^\
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

#MASSACRE COMMANDS START
@bot.command()
async def emailspammer(ctx, target, counter: eval, *, message):
    await ctx.message.delete()
    try:
        _smpt = smtplib.SMTP('smtp.gmail.com', 587)
        _smpt.starttls()
        try:
            _smpt.login(mailname, mailpass)
        except:
            print(current_time + f"Incorrect Password or gmail account, make sure you've enabled less-secure apps access"+Fore.RESET)
            embed = discord.Embed(title=f"**ERROR:**", color=color)
            embed.add_field(name="**Incorrect Password or gmail account**", value="make sure you've enabled less-secure apps access \n", inline=False)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
        count = 0
        embed=discord.Embed(title=f"**EMAIL SPAMMER**", color=color)
        embed.add_field(name="**SPAMMING**", value=target + " \n", inline=False)
        embed.add_field(name="**AMOUNT**", value=(str(counter)) + " \n", inline=False)
        embed.add_field(name="**MESSAGE**", value=message + " \n", inline=False)
        embed.set_footer(text=footer)
        await ctx.send(embed=embed, delete_after=deletetimer)
        while count < counter:
            _smpt.sendmail(mailname, target, message)
            count += 1
           # eventprintnowebhook("Gmail Spammer | Email sent, total " + (str(count)))
           # eventprint("Gmail Spammer | Email sent, total " + (str(count)))
        if count == counter:
            embed = discord.Embed(title=f"**EMAIL SPAMMER | PROCESS COMPLETE**", color=color)
            embed.set_footer(text=footer)
            await ctx.send(embed=embed, delete_after=deletetimer)
    except Exception as error:
        errorprint("Exception ' {0} ', User not found ".format(error))
        em = discord.Embed(title="Exception Error:", description="Expected Exception: User not found \n Console Exception {0}".format(error), color=errorcolor)
        await ctx.send(embed=em, delete_after=deletetimer)
#--------------------------------------------------------------------------------------------------
@bot.command()
async def nuke(ctx):
    await ctx.send("‎\n" * 200)
    await ctx.send("‎\n" * 200)
    await ctx.send("‎\n" * 200)
    await ctx.send("‎\n" * 200)
    await asyncio.sleep(2)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def banlist(ctx):
    bans = await ctx.guild.bans()
    em = discord.Embed(title=f'List of Banned Members ({len(bans)}):')
    em.description = ', '.join([str(b.user) for b in bans])
    em.color=0xff0000
    await ctx.send(embed=em, delete_after=deletetimer)
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def spam(ctx, args1):
    await ctx.message.delete()
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await asyncio.sleep(2)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
    await ctx.send(args1)
#--------------------------------------------------------------------------------------------------
@bot.command()
async def emojilagger(ctx):
    await ctx.message.delete()
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await asyncio.sleep(3)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await asyncio.sleep(3)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
    await ctx.send(":v:" * 500)
#--------------------------------------------------------------------------------------------------
@bot.command()
async def arablagger(ctx):
    await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    await ctx.send("تاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكوتاكو بيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يمبيل تاكو بيل يم يم تاكو أنا أحب سندويشات التاكو يم يم يم تاكو يومتاكو بيل تاكو بيل يم يم تاكو أنا أحب التاكو يم يم يم تاكو يوم")
    await ctx.message.delete()
#--------------------------------------------------------------------------------------------------
@bot.command()
async def massban(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
#--------------------------------------------------------------------------------------------------
#MASSACRE COMMANDS END

#AUTO REPLY START
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#AUTO REPLAY END

bot.run(token, bot=False)