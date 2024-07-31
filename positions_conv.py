from re import match
import jdatetime
from commands import normal_start_command
from database import insert_resume
from utils import return_to_menu, send_cancel_button
from config import phone_number_regex, logger

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    filters,
)

from buttons import (
    get_back_markup,
    get_department_markup,
    get_position_description,
    get_specialization_markup,
    DEPARTMENT_NAMES,
    SPECIALIZATION_NAMES,
)


DEPARTMENT, SPECIALIZATION, CONFIRMATION, NAME, PHONE, RESUME = range(6)


async def conversation_end(update, context) -> int:
    await normal_start_command(update, context)
    return await return_to_menu(context)


def get_confirmation_markup() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton("Confirm ✅", callback_data="confirm")],
        [InlineKeyboardButton("Back 🔙", callback_data="back")],
    ]

    markup = InlineKeyboardMarkup(buttons)
    return markup


def get_reply_markup(state: int, context: ContextTypes) -> InlineKeyboardMarkup:
    if state == DEPARTMENT:
        return get_department_markup()
    elif state == SPECIALIZATION:
        return get_specialization_markup(context.user_data["department"])
    elif state == CONFIRMATION:
        return get_confirmation_markup()
    else:
        return get_back_markup()


async def send_specialization_description(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    description = get_position_description(context.user_data["specialization"])
    await context.bot.send_message(update.effective_chat.id, description)


async def send_resume_message(
    state: int, update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    messages = {
        DEPARTMENT: "Select your desired department: 🎓",
        SPECIALIZATION: "Select your desired specialization: 🔍",
        CONFIRMATION: "Do you want to send your resume in this specialization? ✉️",
        NAME: "Enter your name: 📝",
        PHONE: "Enter your phone number: 📞",
        RESUME: "Send your resume (PDF file only): 📄",
    }

    markup = get_reply_markup(state, context)
    await context.bot.send_message(
        update.effective_chat.id, messages[state], reply_markup=markup
    )


async def positions_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_cancel_button(update)
    await send_resume_message(DEPARTMENT, update, context)
    context.user_data["current_state"] = DEPARTMENT
    return DEPARTMENT


async def department_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["department"] = update.callback_query.data.split("_")[1]
    context.user_data["current_state"] = SPECIALIZATION
    await update.callback_query.edit_message_text(
        "Selected department: " + DEPARTMENT_NAMES[context.user_data["department"]] + " ✅"
    )
    await update.callback_query.answer()
    await send_resume_message(SPECIALIZATION, update, context)
    return SPECIALIZATION


async def specialization_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["specialization"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = CONFIRMATION
    await update.callback_query.edit_message_text(
        "Selected specialization: "
        + SPECIALIZATION_NAMES[context.user_data["specialization"]]
    )
    await update.callback_query.answer()
    await send_specialization_description(update, context)
    await send_resume_message(CONFIRMATION, update, context)
    return CONFIRMATION


async def confirmation_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer("Now send your resume ✉️")
    await update.callback_query.delete_message()
    context.user_data["current_state"] = NAME
    await send_resume_message(NAME, update, context)
    return NAME


async def name_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    context.user_data["current_state"] = PHONE
    await send_resume_message(PHONE, update, context)
    return PHONE


async def phone_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not match(phone_number_regex, update.message.text):
        await update.message.reply_text("Please enter a valid phone number.")
        return PHONE

    context.user_data["phone"] = update.message.text
    context.user_data["current_state"] = RESUME
    await send_resume_message(RESUME, update, context)
    return RESUME


async def resume_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.document:
        await update.message.reply_text("Please only send PDF files.")
        return RESUME

    if not update.message.document.mime_type == "application/pdf":
        await update.message.reply_text("Please only send PDF files.")
        return RESUME

    if update.message.document.file_size > 5 * 1024 * 1024:
        await update.message.reply_text(
            "The file size exceeds the limit. Maximum file size is 5 MB."
        )
        return RESUME

    context.user_data.pop("current_state")
    context.user_data["year"] = jdatetime.datetime.now().year
    context.user_data["month"] = jdatetime.datetime.now().month
    context.user_data["day"] = jdatetime.datetime.now().day
    file = await update.message.effective_attachment.get_file()
    context.user_data["resume"] = await file.download_as_bytearray()

    insert_resume(context)

    await update.message.reply_text(
        "🎉 Your resume has been successfully submitted. We will contact you soon. 📞"
    )
    logger.info(f"New resume submitted by {context.user_data['name']}, id: {update.effective_user.id}")
    return await return_to_menu(context)


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Resume submission canceled.")
    return await return_to_menu(context)


async def back_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.delete_message()
    current_state = context.user_data["current_state"]
    previous_state = current_state - 1 if current_state != NAME else current_state - 2
    await send_resume_message(previous_state, update, context)
    await update.callback_query.answer("Returned to the previous step 🔙")
    context.user_data["current_state"] = previous_state
    return previous_state


async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please enter a valid input.")
    return context.user_data["current_state"]


positions_conv = ConversationHandler(
    entry_points=[MessageHandler(filters.Text("Job Opportunities"), positions_command)],
    states={
        DEPARTMENT: [
            CallbackQueryHandler(department_handler, pattern="^department_.*$")
        ],
        SPECIALIZATION: [
            CallbackQueryHandler(specialization_handler, pattern="^specialization-.*$")
        ],
        CONFIRMATION: [CallbackQueryHandler(confirmation_handler, pattern="^confirm$")],
        NAME: [MessageHandler(filters.TEXT & ~(filters.COMMAND), name_handler)],
        PHONE: [MessageHandler(filters.TEXT & ~(filters.COMMAND), phone_handler)],
        RESUME: [MessageHandler(filters.ATTACHMENT, resume_handler)],
    },
    fallbacks=[
        CallbackQueryHandler(back_handler, pattern="^back$"),
        CommandHandler("cancel", cancel_handler),
        MessageHandler(filters.ALL, unknown_handler),
    ],
    conversation_timeout=600,
)
