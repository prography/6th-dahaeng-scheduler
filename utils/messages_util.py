from utils.sql_connect_utils import Database
import pandas as pd


def set_happy_words() -> str:
    happy_words_message = None
    db = Database().connect()

    query = "SELECT HAPPY_CONTENT FROM CORE_HAPPYWORD ORDER BY RANDOM() LIMIT 1"
    try:
        happy_words_message = str(pd.read_sql(query, db)['happy_content'])[0]
    except IndexError:
        happy_words_message = "[서버알림] 행복 문구를 등록하세요!" 
    return happy_words_message


def set_reminder() -> str:
    reminder_message = None
    db = Database().connect()

    query = "SELECT REMINDER_CONTENT FROM CORE_REMINDERWORD ORDER BY RANDOM() LIMIT 1"
    try:
        reminder_message = str(pd.read_sql(query, db)['reminder_content'])[0]
    except IndexError:
        reminder_message = "[서버알림] 리마인더 문구를 등록하세요!"
    return reminder_message


