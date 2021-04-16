def get_format_name(first, last, otch = ''):
    if otch:
        full_name = f"{first.strip().title()} {last.strip().title()} {otch.strip().title()}"
    else:
        full_name = f"{first.strip().title()} {last.strip().title()}"
    return full_name
