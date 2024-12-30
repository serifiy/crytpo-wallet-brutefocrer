import hashlib
import threading
import time
import random
import string
import os
from tkinter import filedialog, Tk
import itertools
from colorama import Fore, Style

class BruteForcer:
    def __init__(self, wallet_address, crypto_type, private_key_length, thread_count, max_attempts, timeout, output_file, use_file, password_file=None):
        self.wallet_address = wallet_address
        self.crypto_type = crypto_type
        self.private_key_length = private_key_length
        self.thread_count = thread_count
        self.max_attempts = max_attempts
        self.timeout = timeout
        self.output_file = output_file
        self.use_file = use_file
        self.password_file = password_file
        self.hash_function = self.get_hash_function()
        self.public_key = "public_key"  # Placeholder for actual public key derivation
        self.alphabet = string.ascii_letters + string.digits + string.punctuation
        self.lock = threading.Lock()  # Lock for printing to prevent jumbled output from threads

    def get_hash_function(self):
        # Assign appropriate hash functions for different cryptocurrencies
        crypto_hash_functions = {
            "Bitcoin": hashlib.sha256,
            "Ethereum": hashlib.sha256,  # Replace with keccak256 for actual Ethereum
            "Litecoin": hashlib.sha256,
            "Dogecoin": hashlib.sha256,
            "Ripple": hashlib.sha256,
            "Cardano": hashlib.sha256,
            "Polkadot": hashlib.sha256,
            "Binance": hashlib.sha256,
            "Solana": hashlib.sha256,
            "Tron": hashlib.sha256,
        }
        return crypto_hash_functions.get(self.crypto_type, hashlib.sha256)

    def brute_force(self):
        threads = []
        for i in range(self.thread_count):
            thread = threading.Thread(target=self.attempt, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    def attempt(self, thread_id):
        attempts = 0
        for private_key in self.generate_private_key(thread_id):
            public_key = self.derive_public_key(private_key)
            address = self.derive_address(public_key)

            # Log the current password being tested, showing the cryptocurrency type and the private key
            with self.lock:
                print(f"{Fore.CYAN}Thread {thread_id}: {Fore.YELLOW}{self.crypto_type} Wallet - {Fore.GREEN}Testing password: {private_key}{Style.RESET_ALL}")

            if address == self.wallet_address:
                with open(self.output_file, "w") as f:
                    f.write(private_key)
                print(f"{Fore.GREEN}Found private key for {self.crypto_type}: {private_key}{Style.RESET_ALL}")
                return

            attempts += 1
            if attempts >= self.max_attempts:
                break
            time.sleep(self.timeout)

    def generate_private_key(self, thread_id):
        if self.use_file:
            # Read the passwords from the file if selected
            with open(self.password_file, 'r') as file:
                for line in file:
                    yield line.strip()
        else:
            # Auto-generate passwords based on specified length using itertools for efficiency
            for length in range(8, self.private_key_length + 1):
                for combo in self.generate_combinations(thread_id, length):
                    yield combo

    def generate_combinations(self, thread_id, length):
        """Generates all possible combinations of the given length using itertools.product for efficiency."""
        start = (thread_id * 1000)  # Control the range of combinations per thread
        end = start + 1000
        count = 0
        for combo in itertools.product(self.alphabet, repeat=length):
            count += 1
            if count > start and count <= end:
                yield ''.join(combo)
            elif count > end:
                break

    def derive_public_key(self, private_key):
        # Replace with actual public key derivation logic
        return private_key

    def derive_address(self, public_key):
        # Replace with cryptocurrency-specific address derivation logic
        # This is a placeholder to mimic the behavior
        return public_key


def display_banner():
    banner = """
    ********************************************
    *      BruteForce Key Finder Tool          *
    ********************************************
    """
    print(Fore.MAGENTA + banner + Style.RESET_ALL)

def display_menu():
    print(Fore.CYAN + "\n--- BruteForce Key Finder Menu ---" + Style.RESET_ALL)
    
    # Step 1: Get wallet address and crypto type from the user
    wallet_address = input(Fore.YELLOW + "Enter Wallet Address: " + Style.RESET_ALL).strip()
    if not wallet_address:
        print(Fore.RED + "Invalid Wallet Address. Please try again." + Style.RESET_ALL)
        exit(1)

    print(Fore.CYAN + "\nChoose Cryptocurrency Type:" + Style.RESET_ALL)
    crypto_types = [
        "Bitcoin", "Ethereum", "Litecoin", "Dogecoin", "Ripple",
        "Cardano", "Polkadot", "Binance", "Solana", "Tron"
    ]
    for i, crypto in enumerate(crypto_types, start=1):
        print(Fore.YELLOW + f"{i}. {crypto}" + Style.RESET_ALL)
    crypto_choice = int(input(Fore.YELLOW + "Enter your choice (1-10): " + Style.RESET_ALL))
    if not (1 <= crypto_choice <= 10):
        print(Fore.RED + "Invalid choice. Exiting..." + Style.RESET_ALL)
        exit(1)

    crypto_type = crypto_types[crypto_choice - 1]

    # Step 2: Ask the user if they want to use a file or auto-generate passwords
    use_file = input(Fore.YELLOW + "\nDo you want to use a password file? (y/n): " + Style.RESET_ALL).strip().lower() == 'y'
    password_file = None
    if use_file:
        print(Fore.CYAN + "\nNow, select a text file containing passwords." + Style.RESET_ALL)
        password_file = ask_open_file("Choose Password File")

    # Get other parameters
    private_key_length = int(input(Fore.YELLOW + "Enter Private Key Length (e.g., 32): " + Style.RESET_ALL))
    thread_count = int(input(Fore.YELLOW + "Enter Number of Threads: " + Style.RESET_ALL))
    max_attempts = int(input(Fore.YELLOW + "Enter Max Attempts: " + Style.RESET_ALL))
    timeout = float(input(Fore.YELLOW + "Enter Timeout (in seconds): " + Style.RESET_ALL))
    output_file = input(Fore.YELLOW + "Enter Output File Name (e.g., output.txt): " + Style.RESET_ALL).strip()

    return wallet_address, crypto_type, private_key_length, thread_count, max_attempts, timeout, output_file, use_file, password_file

def ask_open_file(prompt):
    # Suppress the root Tkinter window
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title=prompt, initialdir="/", filetypes=(("Text Files", "*.txt"),))
    if file_path and os.path.isfile(file_path):
        return file_path
    return None

def display_credits():
    print(Fore.MAGENTA + "\nCredits:" + Style.RESET_ALL)
    print(Fore.GREEN + "BruteForce Key Finder Tool developed by your friendly AI Assistant." + Style.RESET_ALL)
    print(Fore.YELLOW + "For educational purposes only." + Style.RESET_ALL)

if __name__ == "__main__":
    display_banner()
    wallet_address, crypto_type, private_key_length, thread_count, max_attempts, timeout, output_file, use_file, password_file = display_menu()

    brute_forcer = BruteForcer(
        wallet_address=wallet_address,
        crypto_type=crypto_type,
        private_key_length=private_key_length,
        thread_count=thread_count,
        max_attempts=max_attempts,
        timeout=timeout,
        output_file=output_file,
        use_file=use_file,
        password_file=password_file
    )
    brute_forcer.brute_force()
    display_credits()
