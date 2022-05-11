"""
Added: 2022-05-11
Updated: -
"""


def get_seats(s):
    seats = [
        {"num:": 1, "row": 1, "sitting_person": None},
        {"num:": 2, "row": 1, "sitting_person": "thomas"},
        {"num:": 3, "row": 1, "sitting_person": "tutor"},
    ]

    return seats[s]


print(get_seats(slice(0, 3, 2)))
