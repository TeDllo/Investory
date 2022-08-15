def get_shares(filename) -> list[str]:
    shares_list: list[str] = list()
    with open(filename, "r") as shares:
        for share in shares:
            shares_list.append(share)
    return shares_list


def get_russian_shares() -> list[str]:
    return get_shares("shares_rus.txt")


def get_foreign_shares() -> list[str]:
    return get_shares("shares_for.txt")
