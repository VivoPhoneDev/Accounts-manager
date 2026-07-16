from loading import load

def searches(accounts):
    log = input("Логин: ")
    load()
    for account in accounts:
        if log == account["login"]:
            print(f"Найдено совпадение!\n{account}")
    

