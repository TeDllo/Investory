from enum import Enum

filename_rus = "resources/shares_rus.txt"
filename_for = "resources/shares_for.txt"


class ShareType(Enum):
    RUSSIAN = 0
    FOREIGN = 1


def get_shares(type: ShareType) -> list[str]:
    if type == ShareType.RUSSIAN:
        filename = filename_rus
    else:
        filename = filename_for

    shares_list: list[str] = list()
    with open(filename, "r", encoding="utf-8") as shares:
        for share in shares:
            shares_list.append(share)
    return shares_list
