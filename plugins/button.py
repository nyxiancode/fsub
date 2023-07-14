from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    buttons = [
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
        ],
    ]

    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ])

    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])
        buttons.append([
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ])

    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])
        buttons.append([
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ])

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
        ])
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])
    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="CHANNEL2", url=client.invitelink3),
        ])
        buttons.append([
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ])



    return buttons


def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink3),
        ])

    if not FORCE_SUB_CHANNEL2:
        try:
            buttons.append([
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}",
                )
            ])
        except IndexError:
            pass

    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    return buttons
