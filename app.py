from joke_service import*
from translation_service import*
def choose_language():
    while True:
        user_choose=input("\nChoose a translation language:\n1. Hebrew\n2. Spanish\n3. French\n4. Italian\n")
        if user_choose not in ["1","2","3","4"]:
            print("Invalid language choice")
            continue
        if user_choose=="1":
            return "HE"
        elif user_choose=="2":
            return "ES"
        elif user_choose=="3":
            return "FR"
        elif user_choose=="4":
            return "IT"
def run():
    joke=get_safe_joke()
    if joke:
        data_joke=extract_joke_data(joke)
        langu=choose_language()
        translate=translate_joke(data_joke["joke"],langu)
        analyze=analyze_joke(data_joke["joke"])
        display_result(data_joke["joke"],translate,analyze)

def display_result(joke,translated_joke,analysis):
    print("SAFE PROGRAMMING JOKE\n=====================\n")
    print(f"Original:\n{joke}")
    print(f"Translation:\n[{translated_joke}]")
    print(f"Information:\nCategory: Programming\nWords: {analysis["words"]}\nCharacters: {analysis["characters"]}")
