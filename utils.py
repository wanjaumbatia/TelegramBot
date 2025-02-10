from termcolor import colored


def print_account_info(account_info):
    print(colored("\nMT5 Account Information", "cyan", attrs=["bold", "underline"]))
    
    for key, value in account_info.items():
        if isinstance(value, (int, float)):
            color = "yellow" if value == 0 else "green" if value > 0 else "red"
        else:
            color = "magenta" if isinstance(value, str) else "blue"
        
        print(colored(f"{key}: ", "white", attrs=["bold"]) + colored(value, color))