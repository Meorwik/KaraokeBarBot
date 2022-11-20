message_id_to_del = 0

async def set_message_id_to_delete(message_id: int):
    global message_id_to_del
    message_id_to_del = message_id

async def get_message_id_to_delete():
    global message_id_to_del
    return message_id_to_del