from data.urls import get_barMenu, get_kitchenMenu
request = ""

async def set_barMenu_link():
    global request
    request = "bar"

async def set_kitchenMenu_link():
    global request
    request = "kitchen"

async def get_needed_menu():
    global request
    if request == "bar":
        return await get_barMenu()
    elif request == "kitchen":
        return await get_kitchenMenu()