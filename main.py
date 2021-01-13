# import requests
# from urllib import parse
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs


# # print("입력된 아이디:",id)
# id = "EnjoyDay"


# # +parse.quote(message.content[1:])

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
# # dill = bsObject.find_all("ul",{"class": "swiper-slide"})
# # dill = bsObject.select_one('ul.swiper-slide').get_text()
# # pa = bsObject.select_one("ul.swiper-slide swiper-slide-active").get_text()



# print(f"서버 : {server}")
# print(f"직업 : {job}")
# print(f"닉네임 : {checknickname}")
# print(f"템렙 : {itemlevel[1]}")
# print(f"길드 : {guild}")



# # if
# #   if guild == "위로":
# #     print(server)
# #     print(job)
# #     print(f"{checkcombatlevel} {checknickname}")
# #     print(f"아이템 레벨 : {itemlevel[1]}")
# #     print(f"길드 : {guild}")
# #     print("입주민입니다.")
# #   else:
# #     print(server)
# #     print(f"{checkcombatlevel} {checknickname}")
# #     print(f"아이템 레벨 : {itemlevel[1]}")
# #     print(f"길드 : {guild}")
# #     print("손님입니다.)
