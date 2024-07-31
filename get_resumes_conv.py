from utils import send_single_date_resumes_to_user, return_to_menu, send_cancel_button
from config import get_resume_password, admin_ids, logger
import jdatetime

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from buttons import (
    inline_back_button,
    SPECIALIZATION_BUTTONS,
    DEPARTMENT_BUTTONS,
)


(
    PASSWORD,
    DEPARTMENT_OR_SPECIALIZATION,
    DEPARTMENT,
    SPECIALIZATION,
    DATE_OR_RANGE,
    YEAR,
    MONTH,
    DAY,
    START_YEAR,
    START_MONTH,
    START_DAY,
    END_YEAR,
    END_MONTH,
    END_DAY,
) = range(14)


def get_reply_markup(
    state: int, context: ContextTypes.DEFAULT_TYPE
) -> InlineKeyboardMarkup:
    year_buttons = [
        [InlineKeyboardButton(f"{i}", callback_data=f"year-{i}")]
        for i in range(1400, 1405)
    ] + [inline_back_button]
    month_buttons = [
        [InlineKeyboardButton(f"{i}", callback_data=f"month-{i}") for i in range(1, 4)],
        [InlineKeyboardButton(f"{i}", callback_data=f"month-{i}") for i in range(4, 7)],
        [
            InlineKeyboardButton(f"{i}", callback_data=f"month-{i}")
            for i in range(7, 10)
        ],
        [
            InlineKeyboardButton(f"{i}", callback_data=f"month-{i}")
            for i in range(10, 13)
        ],
    ] + [inline_back_button]
    day_buttons = [
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(1, 5)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(5, 9)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(9, 13)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(13, 17)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(17, 21)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(21, 25)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(25, 29)],
        [InlineKeyboardButton(f"{i}", callback_data=f"day-{i}") for i in range(29, 32)],
    ] + [inline_back_button]
    if state == DEPARTMENT_OR_SPECIALIZATION:
        buttons = [
            [InlineKeyboardButton("Department 🌿", callback_data="department")],
            [InlineKeyboardButton("Specialization 🛠️", callback_data="specialization")],
        ]
    elif state == DEPARTMENT:
        buttons = DEPARTMENT_BUTTONS + [inline_back_button]
    elif state == SPECIALIZATION:
        buttons = SPECIALIZATION_BUTTONS[context.user_data["department"]] + [
            inline_back_button
        ]
    elif state == DATE_OR_RANGE:
        buttons = [
            [InlineKeyboardButton("Date 📅", callback_data="date")],
            [InlineKeyboardButton("Range ⏳", callback_data="range")],
        ] + [inline_back_button]
    elif state == YEAR or state == START_YEAR or state == END_YEAR:
        buttons = year_buttons
    elif state == MONTH or state == START_MONTH or state == END_MONTH:
        buttons = month_buttons
    elif state == DAY or state == START_DAY or state == END_DAY:
        buttons = day_buttons
    else:
        return None

    markup = InlineKeyboardMarkup(buttons)
    return markup


async def send_step_message(
    state: int, update: Update, context: ContextTypes.DEFAULT_TYPE
):
    messages = {
        PASSWORD: "🔐 Please enter the password:",
        DEPARTMENT_OR_SPECIALIZATION: "📝 Please select one of the options:",
        DEPARTMENT: "📂 Please select one of the departments:",
        SPECIALIZATION: "🔧 Please select one of the specializations:",
        DATE_OR_RANGE: "⏰ Please select one of the options:",
        YEAR: "📅 Please select the year:",
        MONTH: "📅 Please select the month:",
        DAY: "📅 Please select the day:",
        START_YEAR: "📅 Please select the start year:",
        START_MONTH: "📅 Please select the start month:",
        START_DAY: "📅 Please select the start day:",
        END_YEAR: "📅 Please select the end year:",
        END_MONTH: "📅 Please select the end month:",
        END_DAY: "📅 Please select the end day:",
    }

    markup = get_reply_markup(state, context)

    if update.message:
        await context.bot.send_message(
            update.effective_chat.id, messages[state], reply_markup=markup
        )
    else:
        await update.callback_query.edit_message_text(
            messages[state], reply_markup=markup
        )


async def get_resumes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_cancel_button(update)
    await send_step_message(PASSWORD, update, context)
    context.user_data["current_state"] = PASSWORD
    return PASSWORD


async def password_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.delete()
    if update.message.text != get_resume_password:
        await update.message.reply_text("Incorrect password.")
        return PASSWORD

    await update.message.reply_text("Correct password.")
    await send_step_message(DEPARTMENT_OR_SPECIALIZATION, update, context)
    context.user_data["current_state"] = DEPARTMENT_OR_SPECIALIZATION
    return DEPARTMENT_OR_SPECIALIZATION


async def department_or_specialization_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    context.user_data["current_state"] = DEPARTMENT
    context.user_data["department_or_specialization"] = update.callback_query.data
    await update.callback_query.edit_message_text(
        "You have selected: " + update.callback_query.data
    )
    await send_step_message(DEPARTMENT, update, context)
    return DEPARTMENT


async def department_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["department"] = update.callback_query.data.split("_")[1]
    await update.callback_query.edit_message_text(
        "Selected department: " + context.user_data["department"]
    )
    next_step = (
        SPECIALIZATION
        if context.user_data["department_or_specialization"] == "specialization"
        else DATE_OR_RANGE
    )
    context.user_data["current_state"] = next_step
    await send_step_message(next_step, update, context)
    return next_step


async def specialization_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["specialization"] = update.callback_query.data.split("-")[1]
    await update.callback_query.edit_message_text(
        "Selected specialization: " + context.user_data["specialization"]
    )
    context.user_data["current_state"] = DATE_OR_RANGE
    await send_step_message(DATE_OR_RANGE, update, context)
    return DATE_OR_RANGE


async def date_or_range_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["date_or_range"] = update.callback_query.data
    next_step = YEAR if update.callback_query.data == "date" else START_YEAR
    await update.callback_query.edit_message_text(
        "You have selected: " + update.callback_query.data
    )
    context.user_data["current_state"] = next_step
    await send_step_message(next_step, update, context)
    return next_step


async def year_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["year"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = MONTH
    await update.callback_query.edit_message_text(
        "Selected year: " + context.user_data["year"]
    )
    await send_step_message(MONTH, update, context)
    return MONTH


async def month_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["month"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = DAY
    await update.callback_query.edit_message_text(
        "Selected month: " + context.user_data["month"]
    )
    await send_step_message(DAY, update, context)
    return DAY


async def day_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["day"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = None
    await update.callback_query.edit_message_text(
        "Selected date: "
        + context.user_data["year"]
        + "/"
        + context.user_data["month"]
        + "/"
        + context.user_data["day"]
    )

    logger.info(f"Searching for resumes on {context.user_data['year']}/{context.user_data['month']}/{context.user_data['day']}")
    await context.bot.send_message(update.effective_chat.id, "Resume search started.")
    await send_single_date_resumes_to_user(context)

    await context.bot.send_message(update.effective_chat.id, "Resume search completed.")

    return await return_to_menu(context)


async def start_year_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["start_year"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = START_MONTH
    await update.callback_query.edit_message_text(
        "Selected start year: " + context.user_data["start_year"]
    )
    await send_step_message(START_MONTH, update, context)
    return START_MONTH


async def start_month_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["start_month"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = START_DAY
    await update.callback_query.edit_message_text(
        "Selected start month: " + context.user_data["start_month"]
    )
    await send_step_message(START_DAY, update, context)
    return START_DAY


async def start_day_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["start_day"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = END_YEAR
    await update.callback_query.edit_message_text(
        "Selected start day: " + context.user_data["start_day"]
    )
    await send_step_message(END_YEAR, update, context)
    return END_YEAR


async def end_year_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["end_year"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = END_MONTH
    await update.callback_query.edit_message_text(
        "Selected end year: " + context.user_data["end_year"]
    )
    await send_step_message(END_MONTH, update, context)
    return END_MONTH


async def end_month_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["end_month"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = END_DAY
    await update.callback_query.edit_message_text(
        "Selected end month: " + context.user_data["end_month"]
    )
    await send_step_message(END_DAY, update, context)
    return END_DAY


async def end_day_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["end_day"] = update.callback_query.data.split("-")[1]
    context.user_data["current_state"] = None
    await update.callback_query.edit_message_text(
        "Selected range: "
        + context.user_data["start_year"]
        + "/"
        + context.user_data["start_month"]
        + "/"
        + context.user_data["start_day"]
        + " to "
        + context.user_data["end_year"]
        + "/"
        + context.user_data["end_month"]
        + "/"
        + context.user_data["end_day"]
    )

    start_date = jdatetime.date(
        int(context.user_data["start_year"]),
        int(context.user_data["start_month"]),
        int(context.user_data["start_day"]),
    )
    end_date = jdatetime.date(
        int(context.user_data["end_year"]),
        int(context.user_data["end_month"]),
        int(context.user_data["end_day"]),
    )

    if start_date > end_date:
        await update.callback_query.edit_message_text(
            "End date must be greater than start date."
        )
        await send_step_message(START_YEAR, update, context)
        return START_DAY

    current_date = start_date

    logger.info(f"Searching for resumes from {start_date} to {end_date}")    
    await context.bot.send_message(update.effective_chat.id, "Resume search started.")

    while current_date <= end_date:
        context.user_data["year"] = current_date.year
        context.user_data["month"] = current_date.month
        context.user_data["day"] = current_date.day
        await send_single_date_resumes_to_user(context)

        current_date += jdatetime.timedelta(days=1)

    await context.bot.send_message(update.effective_chat.id, "Resume search completed.")

    return await return_to_menu(context)


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Search canceled.")
    return await return_to_menu(context)


def get_previous_state(current_state: int, context: ContextTypes.DEFAULT_TYPE) -> int:
    if current_state == START_YEAR:
        return DATE_OR_RANGE
    elif current_state == DATE_OR_RANGE:
        return (
            DEPARTMENT
            if context.user_data["department_or_specialization"] == "department"
            else SPECIALIZATION
        )
    else:
        return current_state - 1


async def back_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_state = context.user_data["current_state"]
    previous_state = get_previous_state(current_state, context)
    await send_step_message(previous_state, update, context)
    await update.callback_query.answer("Returned to previous step 🔙")
    context.user_data["current_state"] = previous_state
    return previous_state


async def send_resume_results_to_user(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    user_id = update.effective_message.caption.split("\n")[0]

    await context.bot.send_document(
        caption=update.effective_message.caption,
        chat_id=user_id,
        document=update.effective_message.document,
    )


get_resumes_conv = ConversationHandler(
    entry_points=[
        MessageHandler(
            filters.Text("Search Resumes") & filters.User(admin_ids),
            get_resumes_command,
        )
    ],
    states={
        PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, password_handler)],
        DEPARTMENT_OR_SPECIALIZATION: [
            CallbackQueryHandler(
                department_or_specialization_handler,
                pattern="^department$|^specialization$",
            )
        ],
        DEPARTMENT: [
            CallbackQueryHandler(department_handler, pattern="^department_.*$")
        ],
        SPECIALIZATION: [
            CallbackQueryHandler(specialization_handler, pattern="^specialization-.*$")
        ],
        DATE_OR_RANGE: [
            CallbackQueryHandler(date_or_range_handler, pattern="^date$|^range$")
        ],
        YEAR: [CallbackQueryHandler(year_handler, pattern="^year-.*$")],
        MONTH: [CallbackQueryHandler(month_handler, pattern="^month-.*$")],
        DAY: [CallbackQueryHandler(day_handler, pattern="^day-.*$")],
        START_YEAR: [CallbackQueryHandler(start_year_handler, pattern="^year-.*$")],
        START_MONTH: [CallbackQueryHandler(start_month_handler, pattern="^month-.*$")],
        START_DAY: [CallbackQueryHandler(start_day_handler, pattern="^day-.*$")],
        END_YEAR: [CallbackQueryHandler(end_year_handler, pattern="^year-.*$")],
        END_MONTH: [CallbackQueryHandler(end_month_handler, pattern="^month-.*$")],
        END_DAY: [CallbackQueryHandler(end_day_handler, pattern="^day-.*$")],
    },
    fallbacks=[
        CommandHandler("cancel", cancel_handler),
        CallbackQueryHandler(back_handler, pattern="^back$"),
    ],
)
