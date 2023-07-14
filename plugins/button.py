from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    buttons = []

    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="CHANNEL2", url=client.invitelink3),
        ])

    if FORCE_SUB_CHANNEL:
        if FORCE_SUB_CHANNEL2:
            buttons[-1].append(
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink)
            )
        else:
            buttons.append([
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
            ])

    if FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    buttons.extend([
        [
            InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ],
    ])

    return buttons


def fsub_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ2", url=client.invitelink3),
        ])

    if FORCE_SUB_CHANNEL:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
        ])

    if FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])

    try:
        buttons.append([
            InlineKeyboardButton(
                text="ᴄᴏʙᴀ ʟᴀɢɪ",
                url=f"https://t.me/{client.username}?start={message.command[1]}",
            )
        ])
    except IndexError:
        pass

    return buttons
