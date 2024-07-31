from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, ContextTypes, MessageHandler, filters

from config import admin_ids
from database import delete_resume


async def normal_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["Job Opportunities"]]
    reply_keyboard = ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(
        "Dear job seeker,\n"
        "Welcome to the Telegram bot of CVCollector.\n"
        "To submit your resume, select Job Opportunities",
        reply_markup=reply_keyboard,
    )


async def admin_start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["Job Opportunities", "Search Resumes"]]
    reply_keyboard = ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, resize_keyboard=True
    )
    await update.message.reply_text(
        "Dear admin,\n"
        "Welcome to the Telegram bot of CVCollector.\n"
        "Please select your desired option",
        reply_markup=reply_keyboard,
    )


async def delete_resume_inline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resume_id = int(update.callback_query.data.split("-")[-1])
    delete_resume(resume_id)
    await update.callback_query.answer()
    await update.callback_query.edit_message_caption("Resume deleted successfully")


normal_start_handler = MessageHandler(
    filters.Text("/start") & ~filters.User(admin_ids), normal_start_command
)

admin_start_handler = MessageHandler(
    filters.Text("/start") & filters.User(admin_ids), admin_start_command
)

delete_resume_callback_handler = CallbackQueryHandler(
    pattern="delete-resume-*", callback=delete_resume_inline
)
