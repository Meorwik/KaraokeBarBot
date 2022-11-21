from data.BarAndKitchenUrlLinks import get_barMenu, get_kitchenMenu

message_id_to_del = 0
request = ""

async def set_message_id_to_delete(message_id: int):
    global message_id_to_del
    message_id_to_del = message_id

async def get_message_id_to_delete():
    global message_id_to_del
    return message_id_to_del

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
    