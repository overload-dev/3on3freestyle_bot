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
import math
import random
client = discord.Client()

token ="your bot token"

#const========================
URL_RANK ='http://3on3rank.fsgames.com/rank'
URL_DETAIL = 'http://3on3rank.fsgames.com/rank/detail'
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
            writeStr += '`!score [user name]` - Users Score Search\n\n'
            writeStr += '`!crew_score [crew name]` - Crew Total Score Search\n\n'
            writeStr += '`!crew_members [crew name]` - Crew Member List Search\n\n'
            writeStr += '`!saikoro` - ????\n\n'
            
            embed = discord.Embed(title = "Ruby Style Guids :smile: ", color = EMBED_FRAME_COLOR)
            embed.add_field(name = "Commands...", value = writeStr, inline = False)
            
            await message.channel.send(embed=embed)

        if msg == '!saikoro':
            sai = [':one:',':two:',':three:',':four:',':five:',':six:']
            rndNum = random.randrange(0,6)
            await message.channel.send(message.channel, embed = discord.Embed(title = 'Your Number is...', description = ':game_die: ' + sai[rndNum]))

        if msg.find('!score ') == 0:
            user_id = msg.replace('!score ','') #filter input user id
            on_message_log(message, '!score') # log print...
            user_info = getUser_info(user_id) # request user_sn on 3on3rank site

            if user_info != None: # if successful search user id...
                user_score = getUser_score(user_info['USER_SN']) # request user 3on3 freestyle socre info
                
                #create embed text.....
                embed = discord.Embed(title=user_id +"'s Info... :sunglasses:", color=EMBED_FRAME_COLOR)
                embed.add_field(name = "WIN_COUNT", value = user_score['WIN_COUNT'], inline = True)
                embed.add_field(name = "WIN_RATE", value = str(round(float(user_score['WIN_RATE'] / CONST_WIN_RATE), 1)) +" %", inline = True)
                embed.add_field(name = "PLAY_COUNT", value = user_score['PLAY_COUNT'], inline = True)
                embed.add_field(name = "AVG_SCORE", value = str(round(float(user_score['AVG_SCORE'] / CONST_AVG_RATE), 1)) + " %", inline = True)
                embed.add_field(name = "AVG_REBOUND", value = str(round(float(user_score['AVG_REBOUND'] / CONST_AVG_RATE), 1)) + " %", inline = True)
                embed.add_field(name = "AVG_BLOCK", value = str(round(float(user_score['AVG_BLOCK'] / CONST_AVG_RATE), 1)) + " %", inline = True)
                embed.add_field(name = "AVG_STEAL", value = str(round(float(user_score['AVG_STEAL'] / CONST_AVG_RATE), 1)) + " %", inline = True)
                embed.add_field(name = "AVG_ASSIST", value = str(round(float(user_score['AVG_ASSIST'] / CONST_AVG_RATE), 1)) + " %", inline = True)
                embed.add_field(name = "AVG_LOOSEBALL", value = str(round(float(user_score['AVG_LOOSEBALL'] / CONST_AVG_RATE),1)) + " %", inline = True)
                #create embed text.....

            else: #if no search user_sn
                #return fail message
                embed = discord.Embed(title = "Sorry I can't Find User Information! :grimacing:", description="Check The User ID", color = EMBED_FRAME_COLOR)

            await message.channel.send(embed=embed)

        if msg.find('!crew_score ') == 0:
            crew_id = msg.replace('!crew_score', '')
            on_message_log(message, '!crew_score') # log print...
            crew_info = getCrew_info(crew_id)

            if crew_info != None:
                crew_score = getCrew_score(crew_info['CREW_SN'])
                
                basic_profile = "Rank : "+ str(crew_score['CREW_SUM_SCORE_RANK'])  + ' (' + str(crew_info['RANK_UPDOWN']) + ')' + "\t/\tMembers : " + str(crew_score['CREW_MEMBER_COUNT'])

                embed = discord.Embed(title = crew_id + " Crew Info... :sunglasses:", description = basic_profile, color = EMBED_FRAME_COLOR)
                embed.add_field(name = "Total Score", value = crew_score['CREW_SUM_SCORE'], inline = True)
                embed.add_field(name = "Match Score", value = crew_score['CREW_MATCH_SCORE'], inline = True)
                embed.add_field(name = "Attendance Score", value = crew_score['CREW_ATTENDANCE_SCORE'], inline = True)
                embed.add_field(name = "Posting Score", value = crew_score['CREW_POSTING_SCORE'], inline = True)

            else:
                embed = discord.Embed(title = "Sorry I can't Find Crew Information! :grimacing:", description="Check The Crew ID", color = EMBED_FRAME_COLOR)

            await message.channel.send(embed=embed)

        if msg.find('!crew_members') == 0:
            crew_id = msg.replace('!crew_members', '')
            on_message_log(message, '!crew_members') # log print...
            crew_info = getCrew_info(crew_id)

            if crew_info != None:
                member_list, totalCount = getCrew_members(crew_info['CREW_SN'])

                embed = discord.Embed(title = crew_id + " Crew Member List... :sunglasses:", color = EMBED_FRAME_COLOR)
                
                writeStr = ''
                for i in member_list:
                    writeStr +=  '' + i['USER_ID'] + '' +'\n'

                embed.add_field(name = "Members  (total : " + str(totalCount) + ")", value = writeStr, inline = True)
                
            else:
                embed = discord.Embed(title = "Sorry I can't Find Crew Information! :grimacing:", description="Check The Crew ID", color = EMBED_FRAME_COLOR)

            await message.channel.send(embed=embed)

#common fn for get basic data ============================
def getBasic_apiData(url, params):
    res_data = api_call(url, params)
    
    try:
        data = res_data['data'][0] #get crew_sn on data param
    except KeyError: # if no search user id, return none
        return None

    return data
#============================================================
def api_call(url, params):
    res = requests.post(url, data = params) #request Post
    res_data = json.loads(res.text) #transform json
    return res_data
#============================================================
def getUser_info(user_id):
    #request user info on basic user param
    params = {
        'type' : 1,
        'searchValue': user_id
    }
    #api call
    user_info = getBasic_apiData(URL_RANK, params)

    return user_info

def getUser_score(user_sn):
    #request detail user info on basic user param
    params = {
        'type' : 2,
        'userSN' : user_sn
        }

    #api call
    res_data = api_call(URL_DETAIL, params)
    user_score = res_data['data'][0] #filter param in 'data'

    return user_score
#============================================================
def getCrew_info(crew_id):
    #request crew info on basic crew param
    params = {
        'type' : 4,
        'searchValue': crew_id
    }
    #api call
    crew_info = getBasic_apiData(URL_RANK, params)

    return crew_info

def getCrew_score(crew_sn):
    params = {
        'type' : 5,
        'crewSN' : crew_sn
        }
    
    #api call
    res_data = api_call(URL_DETAIL, params)
    user_score = res_data['data'] #filter param in 'data'
    return user_score

def getCrew_members(crew_sn):
    params = {
        'type' : 8,
        'crewSN' : crew_sn,
        'curPage' : 1
        }
        
    res_data = api_call(URL_DETAIL, params)
    
    totalCount = res_data['totalCount']

    endPage = math.ceil(res_data['totalCount'] / 10)
    member_list =  res_data['data']
    for i in range(2, endPage + 1):
        params = {
            'type' : 8,
            'crewSN' : crew_sn,
            'curPage' : i
        }
        #api call
        res_data = api_call(URL_DETAIL, params)
        for j in res_data['data']:
            member_list.append(j)

    return member_list, totalCount

#=====logging...=====
def on_message_log(message, keyword):
    print('==========[  on_message log  ]==========')
    print('request user     - ', message.author)
    print('request keyword  - ', keyword)
    print('==========[  on_message log  ]==========')
#=====logging...=====

client.run(token)
