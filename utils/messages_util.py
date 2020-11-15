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


def set_happy_words() -> str:
    pass


def set_reminder() -> str:
    pass

