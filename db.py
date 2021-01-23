from telethon import functions
import __main__
import ast
import traceback


class db:
    """Database class"""
    def __init__(self, id):
        """Pass in message.id where you want to store the data"""
        self.id = id

    async def repr(self):
        """Get database representation"""
        message = await __main__.client(functions.messages.GetMessagesRequest(id=[self.id]))
        d = ast.literal_eval(message.messages[0].message)
        return str(d)

    async def get(self, mod, field, default=None):
        """Set get <field> in <mod> form database. Return <default> if it doesn't exist"""
        message = await __main__.client(functions.messages.GetMessagesRequest(id=[self.id]))
        d = ast.literal_eval(message.messages[0].message)
        try:
            return d[mod][field]
        except KeyError:
            return default

    async def set(self, mod, field, value):
        """Set <field> in <mod> to <value>"""
        message = await __main__.client(functions.messages.GetMessagesRequest(id=[self.id]))
        m = message.messages[0]
        d = ast.literal_eval(m.message)
        try:
            d[mod][field] = value
        except KeyError:
            d[mod] = {}
            d[mod][field] = value
        await __main__.client(functions.messages.EditMessageRequest(m.peer_id, m.id, message=str(d)))

    async def keys(self, mod, default=None):
        message = await __main__.client(functions.messages.GetMessagesRequest(id=[self.id]))
        m = message.messages[0]
        d = ast.literal_eval(m.message)
        try:
            return d[mod].keys()
        except KeyError:
            return default
