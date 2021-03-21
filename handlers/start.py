from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Music Bot, an bot that lets you play music in your groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤔️ How To Use Me 🤔️", url="https://telegra.ph/How-To-Use-Music-Nexa-Bot-03-16"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/{GROUP_NAME}"
                    ),
                    InlineKeyboardButton(
                        "🔰️ Bot Channel 🔰️", url="https://t.me/{CHANNEL_NAME}"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command(["search"]) & filters.private)
async def search(client, message):
    try:
        await message.reply_text(
        text=script.START_MSG.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                        ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

