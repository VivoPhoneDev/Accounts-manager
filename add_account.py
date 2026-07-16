def account_add():

    game = input("Название игры: ").strip()
    login = input("Логин: ").strip()
    password = input("Пароль: ").strip()
    donate = input("Донат на аккаунте, если нет укажите (No): ").strip()
    
    #если нет доната, но нет смысла спрашивать цену
    if donate == "No":
        data = {
        "game": game,
        "login": login,
        "pass": password,
        "donate": donate,
        "price": 0
        }
    else:
        price = input("Цена на сайте: ").strip()
        data = {
            "game": game,
            "login": login,
            "pass": password,
            "donate": donate,
            "price": price
        }

    return data
    