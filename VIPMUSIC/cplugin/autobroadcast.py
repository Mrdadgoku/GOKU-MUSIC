import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "off"

START_IMG_URLS = "https://graph.org/file/eabfb1087a5508dbbb218.jpg"

MESSAGES = f"""**𝗙𝗨𝗟𝗟 𝗠𝗔𝗜𝗡 𝗜𝗗 𝗦𝗔𝗙𝗘 𝗛𝗔𝗖𝗞☑
❤️‍🔥𝗖𝗢𝗡𝗤𝗨𝗘𝗥𝗢𝗥 𝗚𝗔𝗥𝗥𝗘𝗡𝗧𝗬❤️‍🔥
Vᴇʀsɪᴏɴ - 3.3.0 💥
Aʀᴍ - 32x64Bɪᴛ ✨
Gᴀᴍᴇ - Bɢᴍɪ 🇮🇳

⭐️𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 3.3
➜Magic-Server Feel Like Bt 
➜No Any Rules Play With Enjoy 
➜000% Lag Issue Smooth Ui 
➜No Crush Play Continue Match
➜𝟭 𝗗𝗔𝗬 - 150
➜3 DAY - 300
➜7 DAY - 600
➜14 DAY - 1300
➜30 DAY - 2000

🛒 𝗕𝗨𝗬 KEY HERE🛒
➜ @GOKUxMODZbot✅
➜ @GOKUxEDITION✅ :- @GOKUxEDITION

𝗠𝗔𝗜𝗡 𝗜𝗗 𝗦𝗔𝗙𝗘 𝗛𝗔𝗖𝗞
𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿 𝗹𝗶𝗻𝗸 :- https://t.me/+Rl3bz-NiX5w2NTU1**"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ Click & Get BGMI HACK ๏",
                url=f"https://t.me/+Rl3bz-NiX5w2NTU1",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""


async def send_text_once(client):
    try:
        await client.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass


async def send_message_to_chats(client):
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(
                        20
                    )  # Sleep for 20 seconds between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_broadcast(client):

    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats(client)
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)


# Start the continuous broadcast loop if AUTO_GCASTS is True
if AUTO_GCASTS:
    asyncio.create_task(continuous_broadcast(client))
