from utils import greyOutDate
from date_calendar import DateCalender

def test_greyOutDate():
    messages = [
        {
            "number": 1,
            "image": "img/1.jpg",
            "content": "Message 1"
        },
        {
            "number": 2,
            "image": "img/2.jpg",
            "content": "Message 2"
        },
    ]
    expected_messages = [
        {
            "number": 1,
            "image": "img/1.jpg",
            "content": "Message 1",
            "opened": "greyImg"
        },
        {
            "number": 2,
            "image": "img/2.jpg",
            "content": "Message 2"
        },
    ]
    greyed_date = [DateCalender(1)]
    values = greyOutDate(greyed_date, messages)
    assert expected_messages == values

