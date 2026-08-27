def choose_language():
    while True:
        user_choose=input("\nChoose a translation language:\n1. Hebrew\n2. Spanish\n3. French\n4. Italian\n")
        if user_choose not in ["1","2","3","4"]:
            print("Invalid language choice")
            continue
        if user_choose=="1":
            return "he"
        elif user_choose=="2":
            return "es"
        elif user_choose=="3":
            return "fr"
        elif user_choose=="4":
            return "it"
choose_language()