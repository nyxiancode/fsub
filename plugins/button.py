from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2, FORCE_MSG
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
                InlineKeyboardButton(text="CHANNEL", url=client.invitelink),
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


def force_button(client, message):
    buttons = []

    if FORCE_SUB_CHANNEL2:
        buttons.append([
            InlineKeyboardButton(text="FORCE_SUB_CHANNEL2", callback_data="force_sub_channel2"),
        ])

    if FORCE_SUB_CHANNEL:
        buttons.append([
            InlineKeyboardButton(text="FORCE_SUB_CHANNEL", callback_data="force_sub_channel"),
        ])

    if FORCE_SUB_GROUP:
        buttons.append([
            InlineKeyboardButton(text="FORCE_SUB_GROUP", callback_data="force_sub_group"),
        ])

    buttons.extend([
        [
            InlineKeyboardButton(text="HELP", callback_data="help"),
            InlineKeyboardButton(text="CLOSE", callback_data="close"),
        ],
    ])

    return buttons


@Bot.on_message(filters.command("start") & filters.private)
async def not_joined(client: Bot, message: Message):
    buttons = fsub_button(client, message)
    await message.reply_text(
        text=f"{FORCE_MSG}\n\n<b>Ini adalah teks tambahan di luar tombol.</b>",
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )
