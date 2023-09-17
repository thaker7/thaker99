from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message, ReplyKeyboardMarkup,\
    KeyboardButton
from config import prefix, get_bot_information
from database import get_db_botname
from localization import use_chat_lang
from plugins.commands import command2
from plugins.general import confirm_user
from utils import commands
from config import developer ,tokenBot


@Client.on_message(filters.command("thakert", prefix) & filters.user(developer))
@use_chat_lang()
async def startsudo(c: Client, m: Message, strings):
    if m.chat.type == "private":
        t = """💌╖اهلا بيك حبيبي آلمـطـور
⚙️╢ تقدر تتحكم باوامر البوت عن طريق
🔍╢ الكيبور اللي ظهرلك تحت ↘️
🔰╜ للدخول لقناة السورس [دوس هنا](https://t.me/FTTUTY)"""
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton("تعطيل التواصل 🔰")] +
            [KeyboardButton("تفعيل التواصل ⚡️")],
            [KeyboardButton("اضف قناة اشتراك اجباري")] +
            [KeyboardButton("حذف قناه الاشتراك")],
            [KeyboardButton("تعطيل الاذاعه 🔕")] +
            [KeyboardButton("تفعيل الاذاعه 🔔")],
            [KeyboardButton("تعطيل اليوتيوب 🛠")] +
            [KeyboardButton("تفعيل اليوتيوب ⚙️")],
            [KeyboardButton("المطورين 🔱")],
            [KeyboardButton("اذاعه خاص 🔊")] +
            [KeyboardButton("اذاعه بالمجموعات 📡")],
            [KeyboardButton("اذاعه بالتوجيه خاص 👤")] +
            [KeyboardButton("اذاعه بالتوجيه للمجموعات ⁦♻️⁩")],
            [KeyboardButton("اذاعه موجهه بالتثبيت ⁦♻️⁩")] +
            [KeyboardButton("اذاعه بالتثبيت 📎")],
            [KeyboardButton("الاحصائيات 📊")],
            [KeyboardButton("المشتركين ⁦🗣️⁩")] +
            [KeyboardButton("الجروبات 📢")],
            [KeyboardButton("حذف الاعضاء الفيك ⚡️")] +
            [KeyboardButton("حذف الجروبات الفيك ⚡️")],
            [KeyboardButton("حذف رد عام 🚫")] +
            [KeyboardButton("اضف رد عام 💬")],
            [KeyboardButton("الردود العامه 📝")],
            [KeyboardButton("قائمه الكتم العام 🛑")] +
            [KeyboardButton("قائمه الحظر العام 🚫")],
            [KeyboardButton("ضع اسم للبوت 🤖")],
            [KeyboardButton("معلومات السيرفر ℹ️")] +
            [KeyboardButton("سرعه السيرفر 🚀️")],
            [KeyboardButton("جلب نسخه احتياطيه اساسيه 📬")],
            [KeyboardButton("رفع نسخه احتياطيه ⛓")],
            [KeyboardButton("الاصدار ⁦⚙️⁩")] +
            [KeyboardButton("تحديث السورس 📥")],
            [KeyboardButton("رستر البوت 🕹")],
            [KeyboardButton("الغاء ⁦🛠️⁩")],
        ],
            resize_keyboard=True,
            one_time_keyboard=False
        )
        await m.reply_text(t, reply_markup=keyboard, parse_mode="Markdown")
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("start_chat"), url=f"https://t.me/{get_bot_information()[1]}?start=start")]
        ])
        await m.reply_text(strings("group"),
                           reply_markup=keyboard)

bot_id = tokenBot.split(":")[0]

app = Client("N00",api_id=api_id,api_hash=api_hash,bot_token=token)

try:
	open(f"channel{bot_id}.json","r")
except FileNotFoundError:
	open(f"channel{bot_id}.json","w")
	
def is_user(id):
		result = False
def show_channel() -> str:
	with open(f"channel{bot_id}.json","r") as file:
		return file.readline()
	
@Client.on_message(filters.command("start")&filters.private)
async def app_start(c:Client,m:Message):
	do = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{show_channel()}&user_id={m.from_user.id}").text
	user = m.from_user.id
	
	if do.count("left") or do.count("Bad Request: user not found") or is_user(id=user) and not is_band(user):
          await m.reply_text(f"**Join [this channel](t.me/{show_channel()}) first to be able to use the bot**",disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
[[
InlineKeyboardButton("Join Channel",
url=f'https://t.me/{show_channel()}'),
],
]))
	
	else:
	    await app.send_message(text=f"""
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
🎤╖ أهلآ بك عزيزي أنا بوت ماريا
⚙️╢ وظيفتي حماية المجموعات
✅╢ لتفعيل البوت عليك اتباع مايلي 
🔘╢ أضِف البوت إلى مجموعتك
⚡️╢ ارفعهُ » مشرف
⬆️╜ سيتم ترقيتك مالك في البوت
ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("commands_btn"), callback_data="commandss")] +
            [InlineKeyboardButton(strings("infos_btn"), callback_data="infos")],
            [InlineKeyboardButton(strings("language_btn"), callback_data="chlang")],
            [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅",
                                  url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        ])
        async for photo in c.iter_profile_photos(get_bot_information()[0], limit=1):
            await m.reply_photo(photo.file_id, caption=x,
                                reply_markup=keyboard)

        await confirm_user(c, m)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("start_chat"), url=f"https://t.me/{get_bot_information()[1]}?start=start")]
        ])
        await m.reply_text(strings("group"),
                           reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^start_back$"))
@use_chat_lang()
async def start_back(c: Client, m: CallbackQuery, strings):
    if m.message.chat.type == "private":
        if get_db_botname() is None:
            botname = "سيمو"
        else:
            botname = get_db_botname()
        x = f"""
    ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
    🎤╖ أهلآ بك عزيزي أنا بوت {botname}
    ⚙️╢ وظيفتي حماية المجموعات
    ✅╢ لتفعيل البوت عليك اتباع مايلي 
    🔘╢ أضِف البوت إلى مجموعتك
    ⚡️╢ ارفعهُ » مشرف
    ⬆️╜ سيتم ترقيتك مالك في البوت
    ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
            """
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("commands_btn"), callback_data="commandss")] +
            [InlineKeyboardButton(strings("infos_btn"), callback_data="infos")],
            [InlineKeyboardButton(strings("language_btn"), callback_data="chlang")],
            [InlineKeyboardButton(strings("add_chat_btn"),
                                  url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        ])
        async for photo in c.iter_profile_photos(get_bot_information()[0], limit=1):
            await m.message.edit_text(x, reply_markup=keyboard)

    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(strings("start_chat"), url=f"https://t.me/{get_bot_information()[1]}?start=start")]
        ])
        await m.message.reply_text(strings("group"),
                                   reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^infos$"))
@use_chat_lang()
async def infos(c: Client, m: CallbackQuery, strings):
    res = """
╭──── • ◈ • ────╮
么 [َ المطور](t.me/T_4IJ)

么 [قناة البوت](t.me/mane5u)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(strings("back_btn", context="general"), callback_data="start_back")]
    ])
    await m.message.edit_text(res, reply_markup=keyboard, disable_web_page_preview=True, parse_mode="Markdown")


@Client.on_callback_query(filters.regex("^commandss$"))
async def commandsss(c: Client, m: CallbackQuery):
    await command2(c, m)


@Client.on_callback_query(filters.regex("^start@" + str(get_bot_information()[0]) + "$"))
async def startsend(c: Client, m: CallbackQuery):
    await m.message.delete()
    await m.message.reply_text("◍ نعم حبيبى المطور 🥺❤️\n√")

commands.add_command("start", "general")
