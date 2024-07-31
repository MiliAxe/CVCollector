import logging
import dotenv, os

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.INFO)

logger = logging.getLogger(__name__)

phone_number_regex = r"^((98|\+98|0098|0)*(9)[0-9]{9})+$"

dotenv.load_dotenv("config.env")

get_resume_password=os.getenv("RESUME_PASSWORD")
bot_token = os.getenv("BOT_TOKEN")
admin_ids = [int(i) for i in os.getenv("ADMIN_IDS").split(",")]