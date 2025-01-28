import hashlib
from datetime import datetime
from settings import *
import sys

def hash_cracker(hash_to_crack, hash_type, wordlist_file):
    """
    A simple hash cracker program. Attempts to crack the given hash.

    Args:
        hash_to_crack (str): The hash value to be cracked.
        hash_type (str): The type of hash (e.g., md5, sha1, sha256). Default is md5.
        wordlist_file (str): Path to the .txt file containing password guesses. Default is "wordlist.txt".

    Returns:
        str: The cracked password or "Not Found" message.
    """
    # Check if the provided hash algorithm is supported
    try:
        hash_func = getattr(hashlib, hash_type)
    except AttributeError:
        return f"{hash_type} is not supported. Please choose a valid hash algorithm."

    print_(f"Attempting to crack the {hash_type} hash: {hash_to_crack}")
    start_time = datetime.now()

    try:
        # Open the wordlist file and iterate through each password guess
        with open(wordlist_file, "r") as file:
            for line in file:
                guess = line.strip()  # Remove whitespace from the line
                guess_hash = hash_func(guess.encode()).hexdigest()

                # Compare the hash of the guess to the target hash
                if guess_hash == hash_to_crack:
                    end_time = datetime.now() 
                    total_time = colored(f"{end_time - start_time}", "green", attrs=["bold"])
                    print_(f"Password found: {guess} | {total_time}")
                    return guess

    except FileNotFoundError:
        print_(f"The file {wordlist_file} was not found.", "error")
        return "Not Found"

    print_(f"Password not found.", "error")
    return "Not Found"

# Example usage
if __name__ == "__main__":
    try:
        # Example md5 hash : 35eda9c1dbed8e8db1fe6bbca915753e == bytistan 
        args = sys.argv

        sample_hash = args[1]
        hash_type = args[2] 
        wordlist_file = args[3] 

        result = hash_cracker(sample_hash, hash_type, wordlist_file)
        current_time = get_time() 
        print_(f"Result: {result}")
    except Exception as e:
        print(f"[{text_types.get('warn')}] Wrong arguments hash, hash type, wordlist path")
