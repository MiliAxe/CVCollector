from telegram.ext import Application

from commands import (
    admin_start_handler,
    delete_resume_callback_handler,
    normal_start_handler,
)
from config import bot_token
from get_resumes_conv import get_resumes_conv
from positions_conv import positions_conv
from database import create_tables


def main() -> None:
    create_tables()
    
    application = Application.builder().token(bot_token).build()

    handlers = [
        normal_start_handler,
        admin_start_handler,
        positions_conv,
        get_resumes_conv,
        delete_resume_callback_handler,
    ]

    application.add_handlers(handlers)

    application.run_polling()


if __name__ == "__main__":
    main()
