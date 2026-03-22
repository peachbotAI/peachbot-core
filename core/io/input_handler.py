from colorama import Fore, Style

def get_input(mode="medai"):
    if mode == "eco":
        label = "Enter environmental input"
    elif mode == "agri":
        label = "Enter agricultural input"
    elif mode == "bio":
        label = "Enter biological input"
    else:
        label = "Enter clinical input"

    user_input = input(Fore.CYAN + Style.BRIGHT + f"\n{label}: ")
    return {"text": user_input}