from messages import send_happy_words, send_reminder

def set_push_notification_infos(user_info) -> Dict:
    message = None
    if user_info.is_written:
        message = set_happy_words()
    elif not user_info.is_written:
        message = set_reminder()
    else:
        raise ValueError()
    return {
        "message": message,
        "push_notification_token": user_info.push_notification_token,
    }

def send_push_notification(message, push_notification_token) -> None:
    pass
