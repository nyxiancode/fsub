from pyrogram.types import InlineKeyboardButton
from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_CHANNEL2

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
        ])
        buttons.append([
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ])

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
        ])
        buttons.append([
            InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
        ])

    if FORCE_SUB_CHANNEL2:
        buttons.insert(0, [
            InlineKeyboardButton(text="CHANNEL2", url=client.invitelink3),
        ])

    return buttons

def fsub_button(client, message):
    buttons = []

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
        ])

    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
        ])
        buttons.insert(0, [
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
        ])

    return buttons

def get_all_buttons(client, message):
    start_buttons = start_button(client)
    fsub_buttons = fsub_button(client, message)

    if FORCE_SUB_CHANNEL2:
        user_id = message.from_user.id
        if user_id not in ADMINS:
            try:
                member = await client.get_chat_member(
                    chat_id=FORCE_SUB_CHANNEL2, user_id=user_id
                )
                if member.status not in [
                    ChatMemberStatus.OWNER,
                    ChatMemberStatus.ADMINISTRATOR,
                    ChatMemberStatus.MEMBER,
                ]:
                    start_buttons.insert(0, [
                        InlineKeyboardButton(
                            text="Join CHANNEL2",
                            url=client.invitelink3,
                        ),
                    ])
            except UserNotParticipant:
                start_buttons.insert(0, [
                    InlineKeyboardButton(
                        text="Join CHANNEL2",
                        url=client.invitelink3,
                    ),
                ])

    all_buttons = start_buttons + fsub_buttons

    return all_buttons
