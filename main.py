import json
import subprocess
import msvcrt
import os

# Load application data from JSON file
with open("apps.json", "r") as apps_file:
    app_data = json.load(apps_file)

# List of categories and variables to track selected category and application
categories = list(app_data.keys())
selected_category = 0
selected_app = 0

# Function to print the menu
def print_menu(search_query=""):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("App Installer With Winget ")
    print("")
    print("To search: CTRL+F")
    print("Navigate with in apps with left/right arrows, between categories with up/down arrows.")
    print("------------------")
    for index, category in enumerate(categories):
        prefix = "> " if index == selected_category else "  "
        print(f"{prefix}{category}")

    print("------------------")

    selected_apps = app_data[categories[selected_category]]

    if search_query:
        found_apps = [app for app in selected_apps if search_query.lower() in app.lower()]
        for index, app in enumerate(found_apps):
            prefix = "> " if index == selected_app else "  "
            print(f"{prefix}{app}")
        print("\nPress ESC to exit search")
    else:
        for index, app in enumerate(selected_apps):
            prefix = "> " if index == selected_app else "  "
            print(f"{prefix}{app}")
                  
search_buffer = ""

while True:
    print_menu(search_buffer)

    key = msvcrt.getch()

    if key == b'q':
        break
    elif key == b'H':
        selected_category = (selected_category - 1) % len(categories)
        selected_app = 0
    elif key == b'P':
        selected_category = (selected_category + 1) % len(categories)
        selected_app = 0
    elif key == b'K':
        if search_buffer:
            found_apps = [app for app in app_data[categories[selected_category]] if search_buffer.lower() in app.lower()]
            if found_apps:
                selected_app = (selected_app - 1) % len(found_apps)
        else:
            selected_app = (selected_app - 1) % len(app_data[categories[selected_category]])
    elif key == b'M':
        if search_buffer:
            found_apps = [app for app in app_data[categories[selected_category]] if search_buffer.lower() in app.lower()]
            if found_apps:
                selected_app = (selected_app + 1) % len(found_apps)
        else:
            selected_app = (selected_app + 1) % len(app_data[categories[selected_category]])
    elif key == b'\r':
        app_to_install = app_data[categories[selected_category]][selected_app]
        subprocess.run(["winget", "install", app_to_install])
        print(f"{app_to_install} installing process finished.")
        input("Press enter to continue...")
    elif key == b'\x06':  # Ctrl+F
        os.system('cls' if os.name == 'nt' else 'clear')
        search_query = input("\nEnter search query: ")
        search_buffer = search_query
        selected_app = 0  # Reset selected_app when starting a new search
    elif key == b'\x1b':  # ESC key
        search_buffer = ""

# ...
