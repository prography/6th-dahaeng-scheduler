from utils.sql_connect_utils import connect
import pandas as pd


def set_push_notification_message(is_written: bool) -> str:
    DEFAULT_MESSAGE  = "[서버알림] 리마인더 문구를 등록하세요!"
    db = connect()

    TYPE = ["r", "h"]
    query = f"SELECT CONTENT FROM CORE_PUSHNOTIFICATIONMESSAGE WHERE TYPE = '{TYPE[is_written]}' ORDER BY RANDOM() LIMIT 1"
    response = pd.read_sql_query(query, db)['content']
    push_message = str(response[0]) if response else DEFAULT_MESSAGE

    return push_message
