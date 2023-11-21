import keyboard

selected = 0
options = ["Option A", "Option B", "Option C", "Quitter"]

def show_menu():
    print("\n" * 30)
    print("Choose an option:")
    for i, option in enumerate(options):
        print("{1} {0}. {2} {3}".format(i + 1, ">" if selected == i else " ", option, "<" if selected == i else " "))

def up():
    global selected
    if selected > 0:
        selected -= 1
    show_menu()

def down():
    global selected
    if selected < len(options) - 1:
        selected += 1
    show_menu()

def get_selected_choice():
    return options[selected]

def main():
    show_menu()
    keyboard.add_hotkey('up', up)
    keyboard.add_hotkey('down', down)
    keyboard.add_hotkey('enter', get_selected_choice)
    keyboard.wait('enter')

if __name__ == "__main__":
    main()

selected_choice = get_selected_choice()
print(f"You selected option: {selected_choice}")
