import subprocess
import msvcrt
import os

app_data = [
    {"category": "Developer Tools", "apps": [
        {"id": "Microsoft.VisualStudioCode", "name": "Visual Studio Code"},
        {"id": "VSCodium.VSCodium", "name": "VSCodium"},
        {"id": "JetBrains.PyCharm.Community", "name": "PyCharm Community"},
        {"id": "SublimeHQ.SublimeText.4", "name": "Sublime Text 4"},
        {"id": "Git.Git", "name": "Git"},
        {"id": "JetBrains.CLion", "name": "CLion"},
        {"id": "GitHub.GitHubDesktop", "name": "GitHub Desktop"},
        {"id": "GitHub.Atom", "name": "Atom"},
        {"id": "Microsoft.VisualStudio.2022.Community", "name": "Visual Studio 2022 Community"},
        {"id": "Google.AndroidStudio", "name": "Android Studio"},
        {"id": "Notepad++.Notepad++", "name": "Notepad++"},
        {"id": "Codeblocks.Codeblocks", "name": "Codeblocks"}
    ]},
    {"category": "Browsers", "apps": [
        {"id": "Google.Chrome", "name": "Google Chrome"},
        {"id": "Microsoft.Edge", "name": "Microsoft Edge"},
        {"id": "Mozilla.Firefox", "name": "Mozilla Firefox"},
        {"id": "Zen-Team.Zen-Browser", "name": "Zen Browser"}
        {"id": "Opera.OperaGX", "name": "Opera GX"},
        {"id": "Opera.Opera", "name": "Opera"},
        {"id": "VivaldiTechnologies.Vivaldi", "name": "Vivaldi"},
        {"id": "Brave.Brave", "name": "Brave"},
    ]},
    {"category": "Gaming", "apps": [
        {"id": "Valve.Steam", "name": "Steam"},
        {"id": "EpicGames.EpicGamesLauncher", "name": "Epic Games Launcher"},
        {"id": "Nvidia.GeForceExperience", "name": "NVIDIA GeForce Experience"},
        {"id": "Ubisoft.Connect", "name": "Ubisoft Connect"},
        {"id": "ElectronicArts.Origin", "name": "Origin"}
    ]},
    {"category": "Media", "apps": [
        {"id": "VideoLAN.VLC", "name": "VLC Media Player"},
        {"id": "Audacity.Audacity", "name": "Audacity"},
        {"id": "Apple.iTunes", "name": "iTunes"},
        {"id": "Spotify.Spotify", "name": "Spotify"},
        {"id": "9WZDNCRFJ3PT", "name": "Microsoft Movies & TV"},
        {"id": "Winamp.Winamp", "name": "Winamp"},
        {"id": "GOMLab.GOMPlayer", "name": "GOM Player"}
    ]},
    {"category": "Graphic Design", "apps": [
        {"id": "XPDM28CQSPXTWQ", "name": "Graphic Design App 1"},
        {"id": "GIMP.GIMP", "name": "GIMP"},
        {"id": "Inkscape.Inkscape", "name": "Inkscape"},
        {"id": "Canva.Canva", "name": "Canva"},
        {"id": "BlenderFoundation.Blender", "name": "Blender"},
        {"id": "Figma.Figma", "name": "Figma"},
        {"id": "dotPDNLLC.paintdotnet", "name": "Paint.NET"}
    ]},
    {"category": "Office", "apps": [
        {"id": "TheDocumentFoundation.LibreOffice", "name": "LibreOffice"},
        {"id": "Kingsoft.WPSOffice", "name": "WPS Office"},
        {"id": "Apache.OpenOffice", "name": "OpenOffice"},
        {"id": "Adobe.Acrobat.Reader.64-bit", "name": "Adobe Acrobat Reader 64-bit"},
        {"id": "evernote.evernote", "name": "Evernote"}
    ]},
    {"category": "File Archivers", "apps": [
        {"id": "7zip.7zip", "name": "7-Zip"},
        {"id": "RARLab.WinRAR", "name": "WinRAR"}
    ]}
]

# List of categories and variables to track selected category and application
categories = [category["category"] for category in app_data]
selected_category = 0
selected_app = 0

# ...

# Function to print the menu
def print_menu(search_query=""):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("PyWinget")
    print("")
    print("To search: CTRL+F")
    print("Navigate within apps with left/right arrows, between categories with up/down arrows.")
    print("------------------")
    for index, category in enumerate(categories):
        prefix = "> " if index == selected_category else "  "
        print(f"{prefix}{category}")

    print("------------------")

    selected_apps = app_data[selected_category]["apps"]

    if search_query:
        found_apps = [app for app in selected_apps if search_query.lower() in app["name"].lower() or search_query.lower() in app["id"].lower()]
        for index, app in enumerate(found_apps):
            prefix = "> " if index == selected_app else "  "
            print(f"{prefix}{app['name']}")
        print("\nPress ESC to exit search")
    else:
        for index, app in enumerate(selected_apps):
            prefix = "> " if index == selected_app else "  "
            print(f"{prefix}{app['name']}")

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
            found_apps = [app for app in app_data[selected_category]["apps"] if search_buffer.lower() in app["name"].lower()]
            if found_apps:
                selected_app = (selected_app - 1) % len(found_apps)
        else:
            selected_app = (selected_app - 1) % len(app_data[selected_category]["apps"])
    elif key == b'M':
        if search_buffer:
            found_apps = [app for app in app_data[selected_category]["apps"] if search_buffer.lower() in app["name"].lower()]
            if found_apps:
                selected_app = (selected_app + 1) % len(found_apps)
        else:
            selected_app = (selected_app + 1) % len(app_data[selected_category]["apps"])
    elif key == b'\r':
        app_to_install = app_data[selected_category]["apps"][selected_app]["id"]
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
