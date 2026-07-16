from actions import actions_print
from add_account import account_add
from loading import load
from search import searches
import json

act = 0
accounts = []


while act != 4:  
    actions_print()
    try:
        act = int(input("Поле ввода: "))

        if act == 1:
            accounts.append(account_add())
            load()
        
        elif act == 2:
            if not accounts:
                print("Пока нет аккаунтов :(")
            else:
                load()
                print(accounts)
        elif act == 3:
            searches(accounts)

        elif act == 4:
            if not accounts:
                break
            else:
                with open("accounts.json", "w", encoding="utf-8") as f:
                    json.dump(accounts, f, ensure_ascii=False, indent=4)
                break

        else:
            print("Ты че дебил? Такое незя")
        

    except ValueError:
        print("Неверный ввод!")