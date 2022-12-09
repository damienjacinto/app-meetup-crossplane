def greyOutDate(greyed_date, messages):
    for message in messages:
        for date in greyed_date:
            if message['number'] == date.date:
                message["opened"] = "greyImg"
    return messages

