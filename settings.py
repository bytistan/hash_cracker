from termcolor import colored 
from datetime import datetime

text_types = {
    "info": colored("INFO" ,"green"),
    "error": colored("ERROR" ,"red"),
    "warn": colored("WARNING", "yellow")
}

def get_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H.%M.%S")
    colored_text = colored(formatted_time, "cyan")

    return colored_text

def print_(message, tip="info"):
    _text_type = text_types.get(tip)  
    
    if _text_type is None:
        return

    current_time = get_time()
    print(f"[{current_time}] [{_text_type}] {message}.")
