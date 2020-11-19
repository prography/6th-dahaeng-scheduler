from utils.messages_util import set_push_notification_message

def set_push_notification_infos(user_info) -> Dict:
    message = set_push_notification_message(user_info.is_written)
    return {
        "message": message,
        "push_notification_token": user_info.push_notification_token,
    }

def send_push_notification(message, push_notification_token) -> None:
    pass
