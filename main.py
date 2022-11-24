import os
import sys
import time
import json

current_dir = os.getcwd()
startup = True

if os.path.isfile('settings.json'):
    pass
else:
    with open("settings.json", "a+") as f:
        f.write('''{
            "username": "None",
            "ask_very_time": "True"}''')

while True:
    while startup:

        os.system(f'title cmdX - {current_dir}' if os.name == 'nt' else f'PS1="\[\e]0;cmdX - {current_dir}\a\]"; echo -ne "\033]0;cmdX - {current_dir}\007"')
        
        with open('settings.json', 'r') as f:

            """Check settings file for username"""

            data = json.load(f)

            if data['username'] == 'None':
                choice = input("Would you like an username? (y/n): ")

                if choice == 'y':
            
                    username = input("Enter your username: ")
                    data['username'] = username
            
                    with open('settings.json', 'w') as f:
                        json.dump(data, f)

            """Check if the user wants to be asked every time"""

            if data['ask_every_time'] == 'True':
                choice = input("Ask every time? (y/n): ")

                if choice == 'y':
                    pass

                elif choice == 'n':
                    data['ask_every_time'] = 'False'

                    with open('settings.json', 'w') as f:
                        json.dump(data, f)

                elif choice == 'n':
                    pass

        sys.stdout.flush()
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{'-'*13} cmd X {'-'*13}\n'open source, reliable, and free'\n{'-'*33}\n")
        time.sleep(1)
        startup = False


    current_dir = os.getcwd()
    
    if data['username'] == 'None':
        working_dir = current_dir + ">$ "
    else:
        working_dir = data['username'] + ">$ "
    
    command = input(working_dir)


    
    
    if command == "exit":  # Exit the console
        sys.exit()
    
    
    
    if command == "time":  # Current time
        print(time.ctime())
        sys.stdout.flush()

    
    
    if command == "clear":  # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.flush()

    
    
    if command == "direc":  # Current directory
        print(current_dir)
        sys.stdout.flush()
    
    
    
    if command == "cd":  # Change directory
        try:
            os.chdir(command[3:])
            sys.stdout.flush()
            if data["username"] != "None":
                print(f"Current directory: {os.getcwd()}")
                sys.stdout.flush()
            else:
                pass
        except FileNotFoundError:
            print("Directory not found")
            sys.stdout.flush()
        
    
    
    if command == "ls":  # List all files in current directory
        print("  ".join(os.listdir()))
        sys.stdout.flush()
    


    if command.startswith("settings"):  # Change settings
        
        if command.endswith("username"):
            newName = input("Enter new username: ")
            data['username'] = str(newName)
            if data['username'] == '':
                working_dir = current_dir + ">$ "

        elif command.endswith("ask_every_time"):
            choice = input("Ask every time? (True/False): ")
            data['ask_every_time'] = str(choice)
        
        elif command.endswith("dump"):
            current_data = json.dumps(data, indent=4)
            print(current_data)
        
        elif command.endswith("reset"):
            ask = input("Are you sure you want to reset settings? (y/n): ")
            if ask == 'y':
                data["username"] = "None"
                data["ask_every_time"] = "True"
            elif ask == 'n':
                print("Cancelled.")

        else:
            print("--- Settings ---\nusername - Change current username\nask_every_time - Change to ask for a username every time upon launch\ndump - dump current settings")
            sys.stdout.flush()
        

        
    if command.startswith("help"):
        if command.endswith("p"):
            print("time - Current time\nclear - Clear console\ndirec - Current directory\ncd - Change directory\nls - List all files in current directory\nsettings - Change settings\nsay - say/echo what you said\nhelp - Show help\nexit - Exit the console")
            sys.stdout.flush()

        if command.endswith('time'):
            print("usage: time")
            sys.stdout.flush()

        elif command.endswith('clear'):
            print("usage: clear")
            sys.stdout.flush()

        elif command.endswith('direc'):
            print("usage: direc")
            sys.stdout.flush()

        elif command.endswith('cd'):
            print("usage: cd [directory]")
            sys.stdout.flush()

        elif command.endswith('ls'):
            print("usage: ls")
            sys.stdout.flush()

        elif command.endswith('settings'):
            print("usage: settings [setting]")
            sys.stdout.flush()

        elif command.endswith('say'):
            print("usage: say [message]")
            sys.stdout.flush()

        elif command.endswith('cat'):
            print("usage: cat [file]")
            sys.stdout.flush()
            
        elif command.endswith('help'):
            print("usage: help [command]")
            sys.stdout.flush()

        elif command.endswith('exit'):
            print("usage: exit")
            sys.stdout.flush()
            
        else:
            pass

    if command.startswith("say"):
        if command.endswith("say"):
            print("Missing parameter, type 'help say' for more info")
            sys.stdout.flush()
        else:
            if not command.endswith("say"):
                print(command[4:])
                sys.stdout.flush()

    if command.startswith("cat"):
        if command.endswith("cat"):
            print("Missing parameter, type 'help cat' for more info")
            sys.stdout.flush()
        else:
            if not command.endswith("cat"):
                try:
                    with open(command[4:], 'r') as f:
                        print(f.read())
                        sys.stdout.flush()
                except FileNotFoundError:
                    print("File not found")
                    sys.stdout.flush()