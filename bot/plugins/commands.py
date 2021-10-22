#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🍿MAIN CHANNEL🍿', url="https://t.me/joinchat/ISZ9R5CdkgBlMzNl"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🍿MAIN CHANNEL🍿', url='https://t.me/joinchat/ISZ9R5CdkgBlMzNl'),
        InlineKeyboardButton('Source Code 🧾', url ='https://github.com/Alanstalinvellimon/Test')
    ],[
        InlineKeyboardButton('🎸UPDATE CHANNEL🎸', url='https://t.me/joinchat/axutdh3kmhExZjg1')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    else:
        await cmd.reply_photo(

            photo="https://telegra.ph/file/ddbd9b6322e5241394167.jpg",
    caption=f"<b>Hai</b> {cmd.from_user.mention}  Guys!🙋,\n\n<b>I'm[☞ 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 🤖](https://t.me/Movies_Squad_bot) or you can call me as Auto-Filter Bot You Can Use Me As A Auto-filter in Your Group</b> ....\n\n<b>Its Easy To Use Me; Just Add Me To Your Group As Admin, Thats All, i will Provide Movies There</b>...🤓\n\n<b>©️𝑴𝒂𝒊𝒏𝒕𝒂𝒊𝒏𝒆𝒅 𝒃𝒚</b>   <a href=tg://user?id=1959558775> Alan Stalin♨</a>",

            reply_markup=InlineKeyboardMarkup(


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
