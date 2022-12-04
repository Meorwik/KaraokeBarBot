import json


with open('data/config.ini', 'r') as file:
    tg_data = json.load(file)

admins = []
for adm in tg_data["admins"].split():
    admins.append(adm)


BOT_TOKEN = tg_data["token"]
ADMINS = admins 


async def is_admin(id_for_check: str):
   return id_for_check in ADMINS


