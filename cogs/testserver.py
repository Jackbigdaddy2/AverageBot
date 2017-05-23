import discord
from discord.ext import commands
from discord.ext.commands import Bot
import threading
import os
import random
from random import shuffle, choice
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from cogs.utils.chat_formatting import pagify
from urllib.parse import urlparse
from __main__ import send_cmd_help, settings
from json import JSONDecodeError
import re
import logging
import collections
import copy
import asyncio
import math
import time
import inspect
import subprocess
from .utils.dataIO import dataIO
from .utils import checks
import sys
from urllib import FancyURLopener
import urllib2
import simplejson
client = discord.Client()


try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False


class AverageCogs:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, user: discord.Member):
        """This command if for testing purposes for 𝓜𝓬𝓝𝓾𝓰𝓰𝓮𝓽"""
        Name = user.mention
        Id = user.id

        info = "{}'s Discord id is: {}".format(Name, Id)
        
        await self.bot.say(info)


    @commands.command()
    async def id(self, user: discord.Member):
        """Use this command to get someone's Discord id ~ Dylan"""
        Name = user.mention
        Id = user.id

        info = "{}'s Discord id is: {}".format(Name, Id)
        
        await self.bot.say(info)


    @commands.command(aliases=['sp'],pass_context=True, no_pm=True)
    async def schoolphoto(self, ctx, Year, LunchNumber):
        """Use this command to look up any kids school photo in PASCO Florida ~ Dylan"""
        try:
            url = "https://pasco.focusschoolsoftware.com/uploaded-assets/{}/{}.jpg".format(Year, LunchNumber)
            import urllib.request
            urllib.request.urlretrieve (url, "school.jpg")
            await self.bot.send_file(ctx.message.channel, 'school.jpg')
        except:
            text = "The school number {} belongs to nobody :c".format(LunchNumber)
            await self.bot.say(text)
            
            

    @commands.command()
    async def rape(self, user: discord.Member, Amount):
        """Use this command to annoy someone C: ~ Dylan"""
        x = Amount
        y = 0
        z = int(x) + y

        for x in range(1, z  + 1):
            text = "{} Has been raped {} times".format(user.mention, x)
            await self.bot.say(text)


    @commands.command(pass_context=True, no_pm=True)
    async def HappyBirthday(self, ctx, user: discord.Member, age: str):
        """Use this command to send a Happy Birthday message to someone C: ~ Dylan"""
        sender = ctx.message.author.mention
        ageint = int(age)

        text = ":confetti_ball: :gift: :cake: :balloon: Happy Birthday to you, Happy Birthday to you,\nHappy Birthday dear {}! Happy Birthday to you,\nHappy {}th Birthday! From {}! :balloon: :cake: :gift: :confetti_ball:".format(user.mention, ageint, sender)
        await self.bot.say(text)


    @commands.command(pass_context=True, no_pm=True)
    async def tts(self, ctx, *, text):
        """Use this command to send tts messages through the bot ~ Dylan"""
        sender = ctx.message.author
        sendText = text

        await self.bot.purge_from(ctx.message.channel, limit=1, check=None, before=None, after=text, around=None)
        await self.bot.send_message(ctx.message.channel, sendText, tts=True)

    @commands.command(aliases=['purge','prune'], pass_context=True, no_pm=True)
    async def clear(self, ctx, AmountToDelete):
        """Used To Clear/Prune Chat Messages ~ Dylan"""
        deleteAmount = int(AmountToDelete) + 2
        await self.bot.purge_from(ctx.message.channel, limit=deleteAmount, check=None, before=None, after=None, around=None)
        text = "Deleted {} messages in {}".format(deleteAmount - 2,ctx.message.channel.mention)
        await self.bot.say(text)


    @commands.command(pass_context=True, no_pm=True)
    async def Shuga(self, ctx):
        text = "╭━━━┳╮╱╭┳╮╱╭┳━━━┳━━━╮\n┃╭━╮┃┃╱┃┃┃╱┃┃╭━╮┃╭━╮┃\n┃╰━━┫╰━╯┃┃╱┃┃┃╱╰┫┃╱┃┃\n╰━━╮┃╭━╮┃┃╱┃┃┃╭━┫╰━╯┃\n┃╰━╯┃┃╱┃┃╰━╯┃╰┻━┃╭━╮┃\n╰━━━┻╯╱╰┻━━━┻━━━┻╯╱╰╯\n"
        await self.bot.say(text)

    @commands.command(pass_context=True, no_pm=True)
    async def McNugget(self, ctx):
        text = "╭━╮╭━╮╱╱╭━╮╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮\n┃┃╰╯┃┃╱╱┃┃╰╮┃┃╱╱╱╱╱╱╱╱╱╱╭╯╰╮\n┃╭╮╭╮┣━━┫╭╮╰╯┣╮╭┳━━┳━━┳━┻╮╭╯\n┃┃┃┃┃┃╭━┫┃╰╮┃┃┃┃┃╭╮┃╭╮┃┃━┫┃\n┃┃┃┃┃┃╰━┫┃╱┃┃┃╰╯┃╰╯┃╰╯┃┃━┫╰╮\n╰╯╰╯╰┻━━┻╯╱╰━┻━━┻━╮┣━╮┣━━┻━╯\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
        await self.bot.say(text)


    @commands.command(pass_context=True, no_pm=True)
    async def em(self, ctx, EmbedTitle, *, EmbedContent):
        ChosenColor = discord.Colour.dark_purple()
        em = discord.Embed(title=EmbedTitle, description=EmbedContent, colour=ChosenColor)
        em.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
        await self.bot.send_message(ctx.message.channel, embed=em)
        
        
        
        
        
   @commands.command(aliases=['gi'], pass_context=True, no_pm=True)
   async def googleimage(self, ctx, SearchTerm):
        # Define search term
        searchTerm = SearchTerm

        # Replace spaces ' ' in search term for '%20' in order to comply with request
        searchTerm = searchTerm.replace(' ','%20')


        # Start FancyURLopener with defined version 
        class MyOpener(FancyURLopener): 
            version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
        myopener = MyOpener()

        # Set count to 0
        count= 0

        for i in range(0,10):
            # Notice that the start changes for each iteration in order to request a new set of images for each loop
            url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
            print url
            request = urllib2.Request(url, None, {'Referer': 'testing'})
            response = urllib2.urlopen(request)

            # Get results using JSON
            results = simplejson.load(response)
            data = results['responseData']
            dataInfo = data['results']

            # Iterate for each result and get unescaped url
            for myUrl in dataInfo:
                count = count + 1
                print myUrl['unescapedUrl']

                #myopener.retrieve(myUrl['unescapedUrl'],str(count)+'.jpg')
                await self.bot.send_file(ctx.message.channel, myUrl['unescapedUrl'],str(count)+'.jpg')

            # Sleep for one second to prevent IP blocking from Google
            time.sleep(1)
        
    





def setup(bot):
    if soupAvailable:
        bot.add_cog(AverageCogs(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")
