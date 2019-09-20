"""
Author: Lee Kanghyo
Technical Adviser: Ogihara Ryo(https://ogihara-ryo.github.io/)
Create Date: 2019-09-15

[Use Tech]
Python Version : 3.7.4
API : discord (https://github.com/Rapptz/discord.py), 3on3 Ranking (http://3on3rank.fsgames.com)
"""

# -*- coding: utf-8 -*-
import discord
from discord.utils import find
import asyncio
import requests
import json
import random
from tabulate import tabulate

import controller.crewController as crew
import controller.userController as user
import controller.commonController as common

import constants as con

client = discord.Client()

#const========================
CONST_AVG_RATE = 10000
CONST_WIN_RATE = 100
EMBED_FRAME_COLOR = 0xff8080
#==============================
@client.event
async def on_ready():
    print("==========[  initial log     ]==========")
    print('bot login...')
    print('bot name - ', client.user.name)
    print('bot id   - ', client.user.id)
    print("==========[  initial log     ]==========")

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('初めまして！僕はRubyクルーの為のBotです。よろしくお願いいたします。')
        #break #only first room send message

@client.event
async def on_message(message):
    msg = message.content
    
    if message.author.bot:
        return None
    
    if msg[0] == '!':
        if message.content.startswith('!hi'):
            embed = discord.Embed(title="Hello! "+  message.author.name + " :smile: ", description="If you need help, order me [!help]", color = EMBED_FRAME_COLOR)
            await message.channel.send(embed=embed)
        
        if msg.find('!help') == 0:
            writeStr = ''
            writeStr += '**[User Command]**\n'
            writeStr += '`!score_t [user name]` - Users Total Score Search\n'
            writeStr += '`!score_n [user name]` - Users Now Session Score Search\n'
            writeStr += '`!score_p [user name]` - Users Past Session Score Search\n'
            writeStr += '`!matchlog [user name]` - Users Match Log Search\n\n'

            writeStr += '**[Crew Command]**\n'
            writeStr += '`!crew_score_t [crew name]` - Crew Total Score Search\n'
            writeStr += '`!crew_score_n [crew name]` - Crew Now Session Score Search\n'
            writeStr += '`!crew_score_p [crew name]` - Crew Past Session Score Search\n'
            writeStr += '`!crew_members [crew name]` - Crew Member List Search\n\n'

            writeStr += '**[Other]**\n'
            writeStr += '`!saikoro` - ????\n\n'
            
            embed = discord.Embed(title = "Ruby Style Guids :smile: ", color = EMBED_FRAME_COLOR)
            embed.add_field(name = "Commands...", value = writeStr, inline = False)
            
            await message.channel.send(embed=embed)

        if msg == '!saikoro':
            sai = [':one:',':two:',':three:',':four:',':five:',':six:']
            rndNum = random.randrange(0,6)
            await message.channel.send(message.channel, embed = discord.Embed(title = 'Your Number is...', description = ':game_die: ' + sai[rndNum]))

        #========== user score ==========
        if msg.find('!score') == 0:
            for usc in con.USER_SCORE_COMMAND:
                if msg.find(con.USER_SCORE_COMMAND[usc]['COMMAND']) == 0:
                    user_id = msg.replace(con.USER_SCORE_COMMAND[usc]['COMMAND'], '') #filter input user id
                    common.on_message_log(message, con.USER_SCORE_COMMAND[usc]['COMMAND']) # log print...
                    user_info = user.getUser_info(user_id) # request user_sn on 3on3rank site

                    if user_info != None: # if successful search user id...
                        embed = user_score_script_create(user_id, user.getUser_score(user_info['USER_SN'], usc), usc)# request user 3on3 freestyle socre info
                    else: #if no search user_sn
                        embed = discord.Embed(title = "Sorry I can't Find User Information! :grimacing:", description="Check The User ID", color = EMBED_FRAME_COLOR)
                    await message.channel.send(embed=embed)
                    break
        #========== user score ==========
        if msg.find('!matchlog') == 0:
            user_id = msg.replace('!matchlog ','') #filter input user id
            common.on_message_log(message, '!matchlog') # log print...
            user_info = user.getUser_info(user_id) # request user_sn on 3on3rank site
            
            if user_info != None: # if successful search user id...
                match_log = user.getUser_matchLog(user_info['USER_SN'])
                embed = discord.Embed(title=user_id +"'s Match Log... :sunglasses:", color=EMBED_FRAME_COLOR)

                headers=['#', 'Win/Lose', 'Ch1', 'Ch2','Ch3','Ch4']
                rows = [[logs['ORDER'], con.MATCH[logs['RESULT']],
                con.CHARACTER[logs['CHARACTER_CODE1']]['CHARACTER'],
                con.CHARACTER[logs['CHARACTER_CODE2']]['CHARACTER'],
                con.CHARACTER[logs['CHARACTER_CODE3']]['CHARACTER'],
                con.CHARACTER[logs['CHARACTER_CODE4']]['CHARACTER']] for logs in match_log]

                table = tabulate(rows, tablefmt = "fancy_grid", headers = headers)
                writeStr = '```\n'+ table + '\n```'
                await message.channel.send('**' + user_id +"'s Match Log... :sunglasses:" + '**\n\n' + writeStr)
        
        #========== crew score ==========
        if msg.find('!crew_score') == 0:
            for csc in con.CREW_SCORE_COMMAND:
                if msg.find(con.CREW_SCORE_COMMAND[csc]['COMMAND']) == 0:
                    crew_id = msg.replace(con.CREW_SCORE_COMMAND[csc]['COMMAND'], '')
                    common.on_message_log(message, con.CREW_SCORE_COMMAND[csc]['COMMAND']) # log print...
                    crew_info = crew.getCrew_info(crew_id)

                    if crew_info != None:
                        crew_score = crew.getCrew_score(crew_info['CREW_SN'], csc)

                        if csc == 2:
                            basic_profile = "Rank : "+ str(crew_score['CREW_SUM_SCORE_RANK'])  + ' (' + str(crew_info['RANK_UPDOWN']) + ')' + "\t/\tMembers : " + str(crew_score['CREW_MEMBER_COUNT'])
                        else:
                            basic_profile = "Rank : "+ str(crew_score['CREW_SUM_SCORE_RANK'])  + "\t/\tMembers : " + str(crew_score['CREW_MEMBER_COUNT'])

                        embed = crew_score_script_create(crew_id, crew_score, basic_profile, csc)# request user 3on3 freestyle socre info
                    else:
                        embed = discord.Embed(title = "Sorry I can't Find Crew Information! :grimacing:", description="Check The Crew ID", color = EMBED_FRAME_COLOR)
        
                    await message.channel.send(embed=embed)
        #========== crew score ==========

        if msg.find('!crew_members') == 0:
            crew_id = msg.replace('!crew_members', '')
            common.on_message_log(message, '!crew_members') # log print...
            crew_info = crew.getCrew_info(crew_id)

            if crew_info != None:
                member_list, totalCount = crew.getCrew_members(crew_info['CREW_SN'])
                embed = discord.Embed(title = crew_id + " Crew Member List... :sunglasses:", color = EMBED_FRAME_COLOR)
                
                headers=['#', 'Member Name']
                rows = [[member['DATA_ORDER'], member['USER_ID']] for member in member_list]
                table = tabulate(rows, tablefmt = "fancy_grid", headers = headers)
                writeStr = '```\n'+ table + '\n```'

                embed.add_field(name = "Members  (total : " + str(totalCount) + ")", value = writeStr, inline = True)
                await message.channel.send('**' + crew_id + ' Crew Member List... :sunglasses:**\n\n' + writeStr)
            else:
                embed = discord.Embed(title = "Sorry I can't Find Crew Information! :grimacing:", description="Check The Crew ID", color = EMBED_FRAME_COLOR)
                await message.channel.send(embed=embed)

#Write Chat Script Functions
def user_score_script_create(user_id, user_score, usc):
    embed = discord.Embed(title=user_id +"'s [" + con.USER_SCORE_COMMAND[usc]['SCRIPT'] +"] Score.... :sunglasses:", color=EMBED_FRAME_COLOR)
    embed.add_field(name = "Win Count", value = user_score['WIN_COUNT'], inline = True)
    embed.add_field(name = "Win Rate", value = str(round(float(user_score['WIN_RATE'] / CONST_WIN_RATE), 1)) +" %", inline = True)
    embed.add_field(name = "Play Count", value = user_score['PLAY_COUNT'], inline = True)
    embed.add_field(name = "AVG Score", value = str(round(float(user_score['AVG_SCORE'] / CONST_AVG_RATE), 1)) + " %", inline = True)
    embed.add_field(name = "AVG Rebound", value = str(round(float(user_score['AVG_REBOUND'] / CONST_AVG_RATE), 1)) + " %", inline = True)
    embed.add_field(name = "AVG Block", value = str(round(float(user_score['AVG_BLOCK'] / CONST_AVG_RATE), 1)) + " %", inline = True)
    embed.add_field(name = "AVG Steal", value = str(round(float(user_score['AVG_STEAL'] / CONST_AVG_RATE), 1)) + " %", inline = True)
    embed.add_field(name = "AVG Assist", value = str(round(float(user_score['AVG_ASSIST'] / CONST_AVG_RATE), 1)) + " %", inline = True)
    embed.add_field(name = "AVG LoosBall", value = str(round(float(user_score['AVG_LOOSEBALL'] / CONST_AVG_RATE),1)) + " %", inline = True)
    #create embed text.....
    return embed

def crew_score_script_create(crew_id, crew_score, basic_profile, csc):
    embed = discord.Embed(title = crew_id + " Crew ["+ con.CREW_SCORE_COMMAND[csc]['SCRIPT'] + "] Score... :sunglasses:", description = basic_profile, color = EMBED_FRAME_COLOR)
    embed.add_field(name = "Total Score", value = crew_score['CREW_SUM_SCORE'], inline = True)
    embed.add_field(name = "Match Score", value = crew_score['CREW_MATCH_SCORE'], inline = True)
    embed.add_field(name = "Attendance Score", value = crew_score['CREW_ATTENDANCE_SCORE'], inline = True)
    embed.add_field(name = "Posting Score", value = crew_score['CREW_POSTING_SCORE'], inline = True)
    return embed

client.run(con.TOKEN)