import io
from buttons import (
    DEPARTMENT_NAMES,
    SPECIALIZATION_NAMES,
)
from config import admin_ids

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import (
    ContextTypes,
    ConversationHandler
)
from database import get_resumes_single_date


def get_new_caption(resume: dict) -> str:
    new_caption = f"🤵 Name: {resume['name']}\n📞 Phone: {resume['phone']}\n🏢 Department: {DEPARTMENT_NAMES[resume['department']]}\n🔬 Specialization: {SPECIALIZATION_NAMES[resume['specialization']]}\n📅 Submission Date: {resume['year']}/{resume['month']}/{resume['day']}"
    return new_caption


async def send_single_date_resumes_to_user(context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = context._user_id

    resumes = get_resumes_single_date(context)

    for resume in resumes:
        button = [
            InlineKeyboardButton(
                "Delete from Database", callback_data=f"delete-resume-{resume['id']}"
            )
        ]
        document = io.BytesIO(resume["resume"])
        caption = get_new_caption(resume)
        document.name = f"{resume['name']}_resume.pdf"
        await context.bot.send_document(
            user_id,
            document,
            caption=caption,
            reply_markup=InlineKeyboardMarkup([button]),
        )

async def return_to_menu(context: ContextTypes.DEFAULT_TYPE):
    user_id = context._user_id
    
    admin_buttons = [["Job Opportunities", "Search Resumes"]]
    normal_buttons = [["Job Opportunities"]]
    
    if user_id in admin_ids:
        buttons = admin_buttons
    else:
        buttons = normal_buttons
        
    await context.bot.send_message(
        user_id,
        "Returned to the main menu",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True),
    )
    
    return ConversationHandler.END

async def send_cancel_button(update):
    buttons = [["/cancel"]]
    reply_markup = ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(
        "To cancel resume submission, press /cancel", reply_markup=reply_markup
    )

# def get_new_caption(old_caption: str, user_id: str) -> str:
#     user_data = json.loads(old_caption)
#     new_caption = f"{user_id}\n👤 نام: {user_data['name']}\n📞 شماره تماس: {user_data['phone']}\n🏢 دپارتمان: {user_data['department']}\n🔬 تخصص: {user_data['specialization']}\n📅 تاریخ ارسال: {user_data['year']}/{user_data['month']}/{user_data['day']}"
#     return new_caption

# def is_message_date_valid(message_date: str, user_data: dict) -> bool:
#     date = message_date.split(" ")
#     if int(date[-3]) == user_data["year"] and int(date[-2]) == user_data["month"] and int(date[-1]) == user_data["day"]:
#         return True
#     return False

# async def send_resumes_to_bot(user_client: TelegramClient, search_keyword: str, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_id = context._user_id
#     messages = await user_client.get_messages(channel_id, search=search_keyword)

#     for message in messages:
#         user_data = json.loads(message.text)
#         if not is_message_date_valid(search_keyword, user_data):
#             continue
#         message_caption = get_new_caption(message.text, user_id)
#         await user_client.send_message(bot_id, message_caption, file=message.document)
#         await asyncio.sleep(0.5)
