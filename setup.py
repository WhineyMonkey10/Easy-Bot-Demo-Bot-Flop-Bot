# Created by @WhineyMonkey10
# WhineyMonkey10 on GitHub, WhineyMonkey10#9162 on Discord
# Comments generated by AI (GitHub Copilot)

# Imports

import colorama
import os

# Main Code

print(colorama.Fore.GREEN + "Welcome to setup.py!") # Print "Welcome to setup.py!" in green
print(colorama.Fore.GREEN + "This script will help you set up your bot.") # Print "This script will help you set up your bot." in green
print(colorama.Fore.GREEN + "Press Ctrl+C to cancel at any time.") # Print "Press Ctrl+C to cancel at any time." in green

try:
    print(colorama.Fore.GREEN + "Starting setup.py...") # Print "Starting setup.py..." in green
    print(colorama.Fore.GREEN + "Please enter the following information: ") # Print "Please enter the following information: " in green
    botToken = input(colorama.Fore.GREEN + "Enter your bot token: " + colorama.Fore.YELLOW) # Ask for the bot's token
    botPrefix = input(colorama.Fore.GREEN + "Enter your bot prefix: " + colorama.Fore.YELLOW) # Ask for the bot's prefix

    # Write the bot's token, prefix, and status to .env
    print(colorama.Fore.GREEN + "Writing to .env...") # Print "Writing to .env..." in green

    with open(".env", "w") as f: # Open .env as f
        f.write(f"TOKEN={botToken}\n") # Write the bot's token to .env
        f.write(f"PREFIX={botPrefix}\n") # Write the bot's prefix to .env
        f.flush()
        os.fsync(f.fileno())
        
    print(colorama.Fore.GREEN + "Done!") # Print "Done!" in green
    
    githubPushQ = input(colorama.Fore.GREEN + "Are you going pushing to GitHub? (y/n): " + colorama.Fore.YELLOW) # Ask if the user is pushing to GitHub
    if githubPushQ == "y": # If the user is pushing to GitHub
        print(colorama.Fore.YELLOW + "Remember to keep the credits of the author!") # Print "Remember to keep the credits of the author!" in yellow
        try:
            # Add the .env file to .gitignore
            print(colorama.Fore.GREEN + "Adding .env to .gitignore...") # Print "Adding .env to .gitignore..." in green
            with open(".gitignore", "a") as f: # Open .gitignore as f
                f.write(".env\n") # Write ".env" to .gitignore
                f.flush()
                os.fsync(f.fileno())
        except Exception as e:
            print(colorama.Fore.RED + "Error while adding .env to .gitignore!")
            print(colorama.Fore.RED + f"Error: {e}") # Print the error in red
    
    # Install the required packages
    print(colorama.Fore.GREEN + "Installing required packages...") # Print "Installing required packages..." in green
    
    try:
        os.system("pip install -r requirements.txt") # Install the required packages
        print(colorama.Fore.GREEN + "Done!") # Print "Done!" in green
    except Exception as e:
        print(colorama.Fore.RED + "Error while installing required packages!") # Print "Error while installing required packages!" in red
        print(colorama.Fore.RED + "This is most likely due to you not having pip installed. (The bot will NOT run properley if you do not fix this issue!)") # Print "This is most likely due to you not having pip installed." in red
        print(colorama.Fore.RED + f"Error: {e}") # Print the error in red
            
    
    # Complete setup.py
    print(colorama.Fore.GREEN + "Done!") # Print "Done!" in green
    print(colorama.Fore.GREEN + "setup.py finished!") # Print "setup.py finished!" in green
    print(colorama.Fore.GREEN + "Running the bot...") # Print "Running the bot..." in green
    os.system("python bot.py") # Run bot.py

except KeyboardInterrupt:
    print(colorama.Fore.RED + "setup.py cancelled!") # Print "setup.py cancelled!" in red

except Exception as e:
    print(colorama.Fore.RED + "setup.py failed!") # Print "setup.py failed!" in red
    print(colorama.Fore.RED + f"Error: {e}") # Print the error in red