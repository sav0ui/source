# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ✅ • يسمح لك بالبحث عن الموسيقي والفيديو وتشغيلها في المجموعات من خلال المحادثه الصوتيه في تليجرام**

💡 **اكتشف جميع أوامر الروبوت وكيفية عملها من خلال النقر على زر الأوامر »📚**

🔖 **لمعرفة كيفية استخدام هذا الروبوت ، الرجاء النقر فوق الزر »🎧 كيفية الأستخدام !**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 🎞 اضَِٖـفٍُ آلٓبَٰـۄټِٖ إلٓيَ مج ـمۄعَِٰټِٖـڪ 🎞 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("🎧 ڪيَفٍُيَـة آس๋͜ټِٖخدآم هذآ آلٓرۄبَٰـۄټِٖ 🎧", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 آلٓأۄآمــر 📚", callback_data="cbcmds"),
                    InlineKeyboardButton("👨‍💻 لٓلٓأس๋͜‏ټِٖـفٍُس๋͜‏ـآࢪآټِٖ 👩‍💻", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "🎥 ج ـرۄبَٰ آلٓدعَِٰـم 🎥", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قٍُنـآة آلٓس๋͜‏ـۄࢪس๋͜‏  📣", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "♔↯ ᴅᴇᴠ • ʙᴀʀʟᴏ ↯♔", url="https://t.me/bar_lo0o0"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **الدليل الأساسي لأستخدام هذا الروبوت:**

1.) **أولا أضفني إلي مجموعتك.**
2.) **بعد ذلك ، قم بترقيتي كمسؤول ومنح جميع الأذونات باستثناء المسؤول المجهول.**
3.) **بعد ترقيتي ، اكتب /reload في المجموعة لتحديث بيانات المسؤول.**
4.) **أضف @{ASSISTANT_NAME} لمجموعتك أو اكتب /join لدعوه الحساب المساعد.**
5.) **قم بتشغيل محادثة الفيديو أولاً قبل البدء في تشغيل الفيديو / الموسيقى.**
6.) **في بعض الأحيان ، يتم إعادة تحميل الروبوت باستخدام /reload يمكن أن يساعدك الأمر في حل بعض المشكلات.**

📌 **إذا لم ينضم المستخدم bot إلى دردشة الفيديو ، فتأكد من تشغيل دردشة الفيديو بالفعل ، أو اكتب /userbotleave ثم اكتب /join مره اخرى.**

💡 **إذا كانت لديك أسئلة متابعة حول هذا الروبوت ، فيمكنك إخباره من خلال دردشة الدعم الخاصة بي هنا: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اضغط على الزر أدناه لقراءة الشرح ومشاهدة قائمة الأوامر المتاحة! !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻| أوامر الأدمنيه |👷🏻", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻| أوامر أضافيه |🧙🏻", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚| أوامر أساسيه |📚", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
      f"""• 🎥 | قائمة الأوامر الأساسيه | 🎥 • 

» /play (اسم الأغنية / رابط) - تشغيل الموسيقى على دردشة الفيديو
» /vplay (اسم / رابط الفيديو) - تشغيل الفيديو على دردشة الفيديو
» /vstream - تشغيل فيديو مباشر من yt live / m3u8
» /playlist - تظهر لك قائمة التشغيل
» /video (استعلام) - تنزيل الفيديو من youtube
» /song (استعلام) - تنزيل أغنية من youtube
» /lyric (استعلام) - قص الأغنية الغنائية
» /search (استعلام) - ابحث عن رابط فيديو youtube

» /ping - إظهار حالة البوت بينغ
» /uptime - إظهار حالة وقت تشغيل الروبوت
» /alive - عرض معلومات الروبوت على قيد الحياة (في مجموعة)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""• ✅ | قائمة أوامر المسؤليين | ✅ • 

» /pause - إيقاف المحتوي مؤقتًا
» /resume - استئناف المحتوي
» /skip - التبديل إلى الدفق التالي
» /stop - وقف المحتوي
» /vmute - كتم صوت المساعد في الدردشة الصوتية
» /vunmute - قم بإلغاء كتم صوت المساعد في الدردشة الصوتية
» /volume الصوت 1-200 - ضبط حجم الموسيقى (يجب أن يكون برنامج المستخدم هو المسؤول)
» /reload - أعد تحميل الروبوت وقم بتحديث بيانات المسؤول
» /join - دعوة مساعد الروبوت للانضمام إلى المجموعة
» /userbotleave - طلب خروج المساعد من المجموعة

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""• 🎼 | قائمة الأوامر الأضافية | 🎼 •

» /rmw - تنظيف كافة الملفات الخام
» /rmd - تنظيف كافة الملفات التي تم تنزيلها
» /sysinfo - إظهار معلومات النظام
» /update - قم بتحديث الروبوت الخاص بك إلى أحدث إصدار
» /restart - إعادة تشغيل الروبوت الخاص بك
» /leaveall - اطلب userbot للمغادرة من كل المجموعة

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **قائمة التحكم بالمحتوي داخل المحادثه الصوتيه •** {query.message.chat.title}\n\n⏸╎لإيقاف البث [ مؤقتًا ] •\n▶️╎لأستئناف البث مره أخري •\n🔇╎لكتم الحساب المساعد •\n🔊╎لألغاء كتم الحساب المساعد •\n⏹╎لإيقاف تشغيل البث •",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
