from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

################################
## Dev By: @WWWL5 & @MRv7x ##
################################

@Client.on_callback_query(filters.regex("^command (\\d+)$"))
async def command(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م7", callback_data="m7 " + str(m.from_user.id))],
        
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("""
⚙️╖⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
🥳╢ ❬ م2 ❭ اوامر التسليه ⇊
💫╢ ❬ م3 ❭ اوامر الاعضاء ⇊
👮‍♂️╢ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
🎵╢ ❬ م5 ❭ اوامر الموسيقي ⇊
💎╢ ❬ م6 ❭ اوامر المطورين ⇊
💎╜ ❬ م7 ❭ اوامر الالعاب ⇊

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^command2 (\\d+)$"))
async def command2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(m.from_user.id))],

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⚙️╖⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
🥳╢ ❬ م2 ❭ اوامر التسليه ⇊
💫╢ ❬ م3 ❭ اوامر الاعضاء ⇊
👮‍♂️╢ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
🎵╢ ❬ م5 ❭ اوامر الموسيقي ⇊
💎╢ ❬ م6 ❭ اوامر المطورين ⇊
💎╜ ❬ م7 ❭ اوامر الالعاب ⇊ 

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m1 (\\d+)$"))
async def m1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⚙️⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
═══════『♡』═══════ٴ
🔐 ╖ قفل «» فتح + الامر 
⁦♻️⁩ ╜ قفل «» فتح ❬ الكـــل ❭ 
═══════『♡』═══════ٴ
📮╖ الدردشه
📜╢ المعرفات
📸╢ الصور
📽️╢ الفيديوهات
🎟╢ الاستيكر
📂╢ الملفات
🎥╢ المتحركه
⏏️╢ الرفع
🔊╢ الريكورد
🎧╢ الصوت
📞╢ الجهات
🔊╢ الترحيب
🚫╢ المغادره
🎧╢ الاغاني
🏨╢ الزخرفه
🍿╢ الافلام
🎬╢ اليوتيوب
💱╢ الترجمه
🔄╢ الردود
🚿╢ التوجيه
🗳️╢ الاشعارات
💳╢ التاج
🧾╢ رابط الحذف
🔈╢ اطردني
🤔╢ مين ضافني
🏓╢ الالعاب
🎁╢ الروايات
🎆╢ الابراج
🔍╢ معاني الاسماء
💬╜ الترحيب
═══════『♡』═══════ٴ
⚠️ ❬ بالكتم, بالطرد ❭
═══════『♡』═══════ٴ
🌐╖ الروابط
🔄╢ التوجيه
🍿╢ الفشار
⚜️╢ البوتات
⚠️╜ الممنوعه
═══════『♡』═══════ٴ
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mxx (\\d+)$"))
async def mxx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m2 (\\d+)$"))
async def m2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^mx1 (\\d+)$"))
async def mx1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("➡️ التالي", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 1⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
═══════『♡』═══════ٴ
🐣╖ متوحد «» متوحده
💬╢ تاج للمتوحدين 
📎╜ مسح المتوحدين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💢╖ بقره 
💬╢ تاج للبقرات
📎╜ مسح البقرات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐒╖ غبي
💬╢ تاج للاغبيه
📎╜ مسح الاغبيه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤪╖ حمار
💬╢ تاج للحمير
📎╜ مسح الحمير
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤡╖ فرسه
💬╢ تاج للفرسات
📎╜ مسح الفرسات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤰╖ عره
💬╢ تاج للعرر
📎╜ مسح العرر
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ زوجتي
💬╢ تاج للزوجات
📎╜ مسح المتزوجات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ زواج «» طلاق
💬╢ تاج للمتزوجين 
📎╜ مسح المتزوجين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ رفع بقلبي «» تنزيل من قلبي
💬╢ تاج للي بقلبي
📎╜ مسح من قلبي
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ بيستي 
💬╢ تاج للبيست
📎╜ مسح البيستيه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ

    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mx2 (\\d+)$"))
async def mx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 2⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
═══════『♡』═══════ٴ
🐣╖ وتكه
💬╢ تاج للوتكات 
📎╜ مسح الوتكات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💢╖ رقاصه 
💬╢ تاج للرقاصات
📎╜ مسح الرقاصات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐒╖ مهزء
💬╢ تاج للمهزئين
📎╜ مسح المهزئين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤪╖ حيوان
💬╢ تاج للحيوانات
📎╜ الحيوانات 
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐕╖ فاشل
💬╢ تاج للفشله
📎╜ مسح الفشله
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐰╖ دكري
💬╢ تاج للدكور
📎╜ مسح الدكور
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤡╖ قطتي
💬╢ تاج للقطط
📎╜ مسح القطط
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤰╖ ابني
💬╢ تاج للابناء
📎╜ مسح الابناء
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ بنتي
💬╢ تاج للبنوتات
📎╜ مسح البنوتات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ حبيبي
💬╢ تاج للحبايب 
📎╜ مسح الحبايب
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ زوجي
💬╢ تاج للازواج
📎╜ مسح الازواج
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ زوجتي 
💬╢ تاج للزوجات
📎╜ مسح الزوجات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ خاين
💬╢ تاج للخونه
📎╜ مسح الخونه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ خاينه
💬╢ تاج للخاينين 
📎╜ مسح الخاينين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ عبيط
💬╢ تاج للعبط
📎╜ مسح العبط
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ متخزوق 
💬╢ تاج للمتخزوقين
📎╜ مسح المتخزوقين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·

    """, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m3 (\\d+)$"))
async def m3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
💫 ❬ م3 ❭ اوامر الاعضاء ⇊
═══════『♡』═══════ٴ
🎤╖ غنيلي «» حساب العمر
🖼️╢ صورتي «» نسبه جمالي
📖╢ قرءان
⚙️╢ الاعدادات
🔘╢ نقاطي
⚜️╢ حذف «» بيع ❬ نقاطي ❭
💌╢ رسائلي «» حذف ❬ رسائلي ❭
🔊╢ زخرفه «» اغاني 
🎥╢ افلام «» كارتون
🧭╢ ترجمه + روايات
📼╢ يوتيوب «» العاب
🌡╢ طقس + المنطقة 
🦞╢ فينوم «» الرابط
🥱╢ اسمي «» الرتبه
💞╢ بحبك «» تتجوزيني
⚕️╢ جهاتي «» حذف جهاتي
☣️╢ صلاحياتي «» بينج
🔉╢ قول + الكلمه
⛔️╢ الكلمات الممنوعه
⭐️╢ انا مين «» انا فين
♻️╢ قول + الكلمه
🐕╢ قطه «» كلب 
💔╢ اطردني «» اكتمني
🌐╢ تاك للاونلاين «» تاك للاعضاء
👨‍🏫╢ سورس «» المطور
♋️╢ الرابط «» ايدي
⬆️╢ رتبتي «» كشف
📊╢ رد  انت يا بوت
🤔╢ اي رايك يابوت
😈╢ هينو «» هينها
💋╢ بوسو «» بوسها
🙊╢ بتحب دي «» بتحب ده
🌀╢ اسامة «»  فينوم
⚠️╜ رابط الحذف
═══════『♡』═══════ٴ
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m4 (\\d+)$"))
async def m4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
👮‍♂️╖ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
⚠️╜ الادمن «» المنشئ «» المالك
═══════『♡』═══════ٴ
🥳 « المميز » ⇊
═══════『♡』═══════ٴ
🙈╖ كشف
🔇╢ المحظورين
🔕╢ المكتومين
🍿╜ بس كده 😹💔
═══════『♡』═══════ٴ
🐣 « الادمن » ⇊
═══════『♡』═══════ٴ
🥳╖ رفع مميز «» تنزيل مميز
🙋╢ الترحيب
🤬╢ اضف مغادره «» مسح المغادره
🚫╢ رساله المغادره
🤖╢ كشف البوتات
🥳╢ المميزين «» حذف المميزين
🛡╢ حظر «» الغاء حظر
🗡╢ كتم «» الغاء كتم
🗑╢ حظر لمده + المده
🧺╢ كتم لمده + المده
😠╢ طرد «» تطهير 
📌╢ تثبيت «» تثبيت بدون اشعار
🧷╢ الغاء تثبيت الكل
📚╜ ❬ + ❭ جميع ماسبق
═══════『♡』═══════ٴ
🤵 « المنشئ » ⇊
═══════『♡』═══════ٴ
🐣╖ رفع «» تنزيل ادمن
💌╢ اضف «» حذف  ❬ رد ❭
👨‍🎨╢ الردود «» حذف الردود
🔕╢ ايقاف المنشن
💫╢ تعيين «» مسح  ❬ الايدي ❭
👨‍✈️╢ الادمنيه «» حذف الادمنيه
🍻╢ اضف ترحيب
🎲╢ حذف المحظورين «» المكتومين
🎯╢ منع + الكلمه
🚜╢ الغاء منع + الكلمه
🚨╢ حذف الكلمات الممنوعه
🔍╢ المميزين عام
📚╜ ❬ + ❭ جميع ماسبق
═══════『♡』═══════ٴ
👮‍♂️ « المالك » ⇊
═══════『♡』═══════ٴ
🔼╖ اضف صوره «» وصف (للجروب)
🤵╢ رفع منشئ «» تنزيل منشئ
🔊╢ تاج للاعضاء «» للكل
🔗╢ اضف رابط «» مسح الرابط
🔖╢ اضف «» حذف  ❬ امر ❭
📝╢ الاوامر المضافه
🗑╢ حذف الاوامر المضافه
🔏╢ اضف اسم «» تحديث
🍿╢ المنشئين «» حذف المنشئين
📚╜ ❬ + ❭ جميع ماسبق
═══════『♡』═══════ٴ
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m5 (\\d+)$"))
async def m5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
🎵╖ ❬ م5 ❭ اوامر الموسيقي للقنوات والجروبات ⇊
🤵╜ « المنشئ » ⇊
═══════『♡』═══════ٴ
▶️╖ تشغيل «» ريبلاي علي اغنيه
🎶╢ تشغيل + اسم الاغنيه
📹╢ فيديو + اسم الفديو
🔴╢ تشغيل + لينك بث مباشر
⏹╢ ايقاف
⏯️╢ تخطي
👷‍♂️╢ الحساب المساعد
🔢╜ قائمه التشغيل
═══════『♡』═══════ٴ
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m6 (\\d+)$"))
async def m6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
💎╖ ❬ م6 ❭ اوامر المطورين ⇊
👮‍♂️╜ « المطور » ⇊
═══════『♡』═══════ٴ
🤴╖ رفع «» تنزيل ❬ مالك ❭
🔂╢ تغيير رابط الجروب
🔊╢ اذاعه بالمجموعات
👨‍🏭╢ اذاعه بالتوجيه للمجموعات
🤹‍♀╢ اذاعه موجهه بالتثبيت
☀️╢ اذاعه خاص
💘╢ اذاعه بالتوجيه خاص
🎙️╢ اذاعه بالتثبيت
📶╢ جلب نسخه احتياطيه
🏋‍♂╢ رفع نسخه احتياطيه
🍃╢ الاحصائيات
🚷╢ حذف المالكين
📚╜ ❬ + ❭ جميع ماسبق
═══════『♡』═══════ٴ
💎 « المطور الاساسي » ⇊
═══════『♡』═══════ٴ
📑╖ اضف «» حذف رد عام
🤴╢ رفع «» تنزيل ❬ مميز عام ❭
💎╢ مسح المميزين عام
🗃️╢ الردود العامه
🧨╢ حذف الردود العامه
🛠╢ اذاعه بالتوجيه خاص
🍃╢ اذاعه بالتوجيه للمجموعات
🎯╢ اذاعه بالتثبيت
☀️╢ اذاعه موجهه بالتثبيت
🧲╢ جلب «» رفع ❬نسخه احتياطيه❭
⏳╢ الاحصائيات
🤴╢ رفع «» تنزيل ❬ مطور ❭
🤖╢ المطورين «» حذف المطورين
🔗╢ ضع اسم للبوت
📝╢ تغيير رساله المغادره
🚫╢ حظر «» كتم  ❬ عام ❭
🥺╢ المكتومين  عام 
💔╢ المحظورين عام
♻️╢ الغاء العام
📚╜ ❬ + ❭ جميع ماسبق
═══════『♡』═══════ٴ
    """, reply_markup=keyboard)
    
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
💎╜ ❬ م7 ❭ اوامر الالعاب ⇊
💎 الالعاب الخاصه بالسورس
•━━━━━━━『♡』━━━━━━━•ٴ
⚙️╖ لفتح الالعاب او قفلها ارسل ⇊
🔰╜ قفل الالعاب ࿗ فتح الالعاب
•━━━━━━━『♡』━━━━━━━•ٴ
🎱╖ لعبه XO ࿗ ❬اكس او❭
😎╢ لعبة الصراحه ࿗ ❬صراحه❭
💃╢ لعبة مريم ࿗ ❬مريم❭
🥺╢ لعبة عقاب ࿗ ❬عقاب❭
💥╢ جمالى % ࿗ ❬نسبه جمالي❭
❤️╢ نسبه الحب ࿗ ❬نسبه الحب❭
👺╢ الكذب ࿗ ❬كشف الكذب❭
🐜╢ لعبه النمله الجامده ࿗ ❬نمله❭
🦗╢ الصرصار الجامد ࿗ ❬صرصار❭
🐷╢ الخنزير الجامد ࿗ ❬خنزير❭
🏀╢ كره السله ࿗ ❬كره السله❭
🎯╢ لعبة النشال ࿗ ❬النشال❭
🎲╢ لعبة النرد او الزهر ࿗ ❬النرد❭
💎╢ كت تويت ࿗ ❬تويت❭
👀╢ كت تويت ࿗ ❬تويت بالصور❭
🤹‍♂️╢ اسرع شخص ࿗ ❬الاسرع❭
🏤╢ لعبة المطابقه ࿗  ❬التشابه❭
‌🏜⁩╢ لعبة الذكاء ࿗ ❬المختلف❭
🎰╢ لعبة الارقام ࿗ ❬الرياضيات❭
🌐╢ لعبة ترجمه ࿗ ❬الانجليزي❭
🎎╢ لعبة تصحيح ࿗  ❬الامثله❭
‌♻️⁩╢ لعبة عكس ࿗ الكلمات ❬العكس❭
🤔╢ لعبة التفكير ࿗  ❬الفزوره❭
🎬╜ اللعبه الشهيره ࿗  ❬المعاني❭
•━━━━━━━『♡』━━━━━━━•ٴ
    """, reply_markup=keyboard)