# © @AvishkarPatil [ Telegram ]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

START_TEXT = """
<i>Hᴇʏ 🙋,</i>{}\n
<i>𝐼'𝑚 𝑡𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝑓𝑖𝑙𝑒𝑠 𝑠𝑡𝑟𝑒𝑎𝑚𝑖𝑛𝑔 𝑏𝑜𝑡 𝑎𝑠 𝑤𝑒𝑙𝑙 𝑑𝑖𝑟𝑒𝑐𝑡 𝑙𝑖𝑛𝑘𝑠 𝑔𝑒𝑛𝑒𝑟𝑎𝑡</i>\n
<i>𝐶𝑙𝑖𝑐𝑘 𝑜𝑛 🤖 𝙷𝙴𝙻𝙿 𝑡𝑜 𝑔𝑒𝑡 𝑚𝑜𝑟𝑒 𝑖𝑛𝑓𝑜𝑟𝑚𝑎𝑡𝑖𝑜𝑛</i>\n
<i><u>𝗪𝗔𝗥𝗡𝗜𝗡𝗚 ⚠️</u></i>\n
<b>🚨 P🔞RN 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐋𝐞𝐚𝐝𝐬 𝐓𝐨 𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏 𝘽𝘼𝙉 𝙔𝙊𝙐 🚨</b>\n\n
<i><b>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :</b>@MD_OWNER</i>"""

HELP_TEXT = """
<i>- 𝙎𝙚𝙣𝙙 𝙢𝙚 𝙖𝙣𝙮 𝙛𝙞𝙡𝙚 (𝙊𝙍) 𝙢𝙚𝙙𝙞𝙖 𝙛𝙧𝙤𝙢 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢.</i>
<i>- 𝙄 𝙬𝙞𝙡𝙡 𝙥𝙧𝙤𝙫𝙞𝙙𝙚 𝙚𝙭𝙩𝙚𝙧𝙣𝙖𝙡 𝙙𝙞𝙧𝙚𝙘𝙩 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙡𝙞𝙣𝙠 !.</i>
<i>- 𝘼𝙙𝙙 𝙢𝙚 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙛𝙤𝙧 𝙙𝙞𝙧𝙚𝙘𝙩 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙡𝙞𝙣𝙠𝙨 𝙗𝙪𝙩𝙩𝙤𝙣𝙨</i>
<i>- 𝙏𝙝𝙞𝙨 𝙥𝙚𝙧𝙢𝙖𝙣𝙚𝙣𝙩 𝙡𝙞𝙣𝙠 𝙬𝙞𝙩𝙝 𝙛𝙖𝙨𝙩𝙚𝙨𝙩 𝙎𝙥𝙚𝙚𝙙</i>\n
<u>🔻𝗪𝗔𝗥𝗡𝗜𝗡𝗚 ⚠️</u>\n
<b>🚨 𝗣🔞𝗥𝗡 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐋𝐞𝐚𝐝𝐬 𝐓𝐨 𝙋𝙀𝙍𝙈𝘼𝙉𝙀𝙉𝙏 𝘽𝘼𝙉 𝙔𝙊𝙐 🚨</b>\n
<i>𝘾𝙤𝙣𝙩𝙖𝙘𝙩 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 (𝙊𝙍) 𝙧𝙚𝙥𝙤𝙧𝙩 𝗕𝗨𝗚𝗦</i> <b>: <a href='https://telegram.me/MD_OWNER'>♻️ 🙆 𝙘𝙡𝙞𝙘𝙠 𝙝𝙚𝙧𝙚 ♻️</a></b>"""

ABOUT_TEXT = """
<b>😉 𝑴𝒚 𝑵𝒂𝒎𝒆 : 𝑻𝑮 𝑭𝒊𝒍𝒆 𝑺𝒕𝒓𝒆𝒂𝒎 𝑳𝒊𝒏𝒌 𝑩𝒐𝒕</b>\n
<b>🌿 𝑴𝒚 𝒖𝒔𝒆𝒓 𝒏𝒂𝒎𝒆 : <a href='https://telegram.me/MD_FILE_STREAM_BOT'>@𝑴𝑫_𝑭𝑰𝑳𝑬_𝑺𝑻𝑹𝑬𝑨𝑴_𝑩𝑶𝑻</a></b>\n
<b>🌹 𝑽𝒆𝒓𝒔𝒊𝒐𝒏 : <a href='https://telegram.me/MD_OWNER'>3.0.1</a></b>\n
<b>🌱 𝑮𝒊𝒕𝑯𝒖𝒃 : <a href='https://GitHub.com/github1tg'>𝑭𝒐𝒍𝒍𝒐𝒘</a></b>\n
<b>☘ 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 : <a href='https://telegram.me/MD_OWNER'>𝑴𝑫 𝑶𝑾𝑵𝑬𝑹</a></b>\n
<b>🌴 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 : <a href='https://telegram.me/MD_BOTZ'>𝑴𝑫 𝑩𝑶𝑻𝒁</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 𝙷𝙴𝙻𝙿', callback_data='help'),
        InlineKeyboardButton('⚙ 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
        InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 𝙷𝙾𝙼𝙴', callback_data='home'),
        InlineKeyboardButton('⚙ 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
        InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 𝙷𝙾𝙼𝙴', callback_data='home'),
        InlineKeyboardButton('🤖 𝙷𝙴𝙻𝙿', callback_data='help'),
        InlineKeyboardButton('🔐 𝙲𝙻𝙾𝚂𝙴', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ__\n\n @AvishkarPatil **Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                )
                    return
            except UserNotParticipant:
                await StreamBot.send_photo(
                    chat_id=m.chat.id,
                    photo="https://telegra.ph/file/a788a12989e9d3784724e.jpg",
                    caption="<i>𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("𝐽𝑂𝐼𝑁 𝑁𝑂𝑊 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i> <b><a href='http://t.me/Avishkarpatil'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Qᴜɪᴄᴋʟʏ ᴄᴏɴᴛᴀᴄᴛ** @Avishkarpatil",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ**!\n\n**Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ** [Aᴠɪsʜᴋᴀʀ Pᴀᴛɪʟ](https://t.me/Avishkarpatil).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 🤷 !</u></i>\n
<b>📂 𝘍𝘪𝘭𝘦 𝘕𝘢𝘮𝘦 :</b> <i>{}</i>\n
<b>🗳 𝘍𝘪𝘭𝘦 𝘚𝘪𝘻𝘦 :</b> <i>{}</i>\n
<b>🟢 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 :</b> <i>{}</i>\n
<b>👌 𝗡𝗼𝘁𝗲 : 𝘓𝘪𝘯𝘬 𝘦𝘹𝘱𝘪𝘳𝘦𝘥 𝘪𝘯 24 𝘩𝘰𝘶𝘳𝘴</b>\n
<i>🤪 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :</i> <b>@MD_OWNER</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]])
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ__ [Aᴠɪsʜᴋᴀʀ Pᴀᴛɪʟ](https://t.me/Avishkarpatil).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )
