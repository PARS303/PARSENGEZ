def request_in_massage (rows):
    i = 0
    massage = ""
    if rows == None:return "Примеры кончились!"
    for row in rows:
        if i != 0:
            massage += f"{row}"
            if (i == 1)or(i == 3) :
                massage += " - "
            if (i == 2) or (i == 4):
                massage += "\n"
        i += 1
    return massage
