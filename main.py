import discord
import asyncio
import requests
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup 
from discord.utils import get
import os


client = discord.Client()

@client.event
async def on_ready():
  print('Online')
  print(client.user.name)
  print(client.user.id)


@client.event
async def on_message(message):
  baseurl = "https://lostark.game.onstove.com/Profile/Character" + "/" + parse.quote(message.content[2:])
  html = urlopen(baseurl).read()
  bsObject = BeautifulSoup(html, "html.parser")
  job = bsObject.select("img")[0]['alt']
  checkserver = bsObject.select_one('.profile-character-info__server').get_text()
  server = checkserver[1:]
  checkitemlevel = bsObject.select_one('.level-info2__expedition').get_text()
  #checkcombatlevel = bsObject.find_all("div", {"class": "level-info__item"})[0].find_all("span")[1].text 전투레벨 LV00.닉네임
  checkguild = bsObject.select_one('.game-info__guild').get_text()
  checknickname = bsObject.find_all("div", {"class": "profile-character-info"})[0].find_all("span")[1].text
  guild = checkguild[2:]
  itemlevel = checkitemlevel.split('장착 아이템 레벨Lv.')
  if message.content.startswith(". n"):
    await client.channel.send(f"서버 : {server} \n 직업 : {job} \n 닉네임 : {checknickname} \n 템렙 : {itemlevel[1]} \n 길드 : {guild} " ) 
  else:
    await client.channel.send("잘못된 입력 입니다.")






# baseurl = "https://lostark.game.onstove.com/Profile/Character" + "/" + parse.quote(id)
# html = urlopen(baseurl).read()
# bsObject = bs(html, "html.parser")

# job = bsObject.select("img")[0]['alt']
# checkserver = bsObject.select_one('.profile-character-info__server').get_text()
# server = checkserver[1:]
# checkitemlevel = bsObject.select_one('.level-info2__expedition').get_text()
# checkcombatlevel = bsObject.find_all("div", {"class": "level-info__item"})[0].find_all("span")[1].text
# checkguild = bsObject.select_one('.game-info__guild').get_text()
# checknickname = bsObject.find_all("div", {"class": "profile-character-info"})[0].find_all("span")[1].text
# guild = checkguild[2:]
# itemlevel = checkitemlevel.split('장착 아이템 레벨Lv.')







access_token = os.environ["BOT_TOKEN"]
client.run(access_token) 



    
# (f"서버 : {server}")
# (f"직업 : {job}")
# (f"닉네임 : {checknickname}")
# (f"템렙 : {itemlevel[1]}")
# (f"길드 : {guild}")
    
