from peewee import SqliteDatabase, Model, CharField, BlobField, MySQLDatabase
from telegram.ext import ContextTypes
from jdatetime import datetime
import os

db = SqliteDatabase("resumes.db")
# db = MySQLDatabase('miliatio_telegrambot', user='miliatio_telegrambot', password='Kjkszpj123!', host='localhost', port=3306, charset='utf8mb4')

class LongBlobField(BlobField):
    field_type = 'LONGBLOB'

class Resume(Model):
    name = CharField()
    phone = CharField()
    department = CharField()
    specialization = CharField()
    resume = LongBlobField()
    year = CharField()
    month = CharField()
    day = CharField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Resume])


def insert_resume(context: ContextTypes.DEFAULT_TYPE):
    with db:
        Resume.create(
            name=context.user_data["name"],
            phone=context.user_data["phone"],
            department=context.user_data["department"],
            specialization=context.user_data["specialization"],
            resume=context.user_data["resume"],
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
        )


def get_resumes_single_date(context: ContextTypes.DEFAULT_TYPE) -> list:
    resumes = []
    with db:
        if context.user_data["department_or_specialization"] == "department":
            resume_query = Resume.select().where(
                Resume.department == context.user_data["department"],
                Resume.year == context.user_data["year"],
                Resume.month == context.user_data["month"],
                Resume.day == context.user_data["day"],
            )
        else:
            resume_query = Resume.select().where(
                Resume.specialization == context.user_data["specialization"],
                Resume.year == context.user_data["year"],
                Resume.month == context.user_data["month"],
                Resume.day == context.user_data["day"],
            )

        for resume in resume_query:
            resumes.append(resume.__dict__["__data__"])

    return resumes


def insert_resume_with_pdf(context: ContextTypes.DEFAULT_TYPE, pdf_file_path: str):
    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"The file {pdf_file_path} does not exist.")

    with open(pdf_file_path, "rb") as file:
        pdf_content = file.read()

    with db:
        Resume.create(
            name=context.user_data["name"],
            phone=context.user_data["phone"],
            department=context.user_data["department"],
            specialization=context.user_data["specialization"],
            resume=pdf_content,
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day,
        )


def save_pdf_from_blob(resume_id, output_file_path):
    resume = Resume.get(Resume.id == resume_id)

    pdf_content = resume.resume

    with open(output_file_path, "wb") as pdf_file:
        pdf_file.write(pdf_content)

def delete_resume(resume_id):
    with db:
        Resume.delete().where(Resume.id == resume_id).execute()

class DemoContext:
    def __init__(self, user_data):
        self.user_data = user_data

if __name__ == "__main__":
    create_tables()