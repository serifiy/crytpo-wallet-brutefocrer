# crytpo-wallet-brutefocrer 
# BruteForce Key Finder Tool

## Overview

The **BruteForce Key Finder Tool** is a Python script that allows you to attempt to brute force private keys for cryptocurrency wallets. It leverages multi-threading and configurable parameters to test various private key combinations against a given wallet address. This tool can be used for educational purposes to demonstrate how brute force works in theory and how secure different private keys can be for cryptocurrency wallets.

**Note**: This tool is for **educational and research purposes only**. It should not be used for illegal activities such as trying to access someone else's wallet.

## Features

- Supports multiple cryptocurrencies (Bitcoin, Ethereum, Litecoin, Dogecoin, and more).
- Allows brute-forcing of private keys using a custom character set.
- Multi-threading support for faster brute force attacks.
- Option to either generate private keys automatically or use a list of passwords from a file.
- Colorful and user-friendly output with logs.
- Option to log found private keys to a file.

## How It Works

### 1. **Private Key Length**

The private key length determines how many characters long the private key will be. Longer private keys exponentially increase the number of combinations needed to test, making the brute force attack much more time-consuming. By default, the tool supports keys with lengths between 8 and 32 characters.

### 2. **Number of Threads**

This parameter allows you to specify how many threads (parallel processes) the script will use to try different combinations of private keys at the same time. Increasing the number of threads speeds up the brute force process by allowing multiple attempts to be made simultaneously. However, be mindful of your system's resources—too many threads can cause performance issues.

### 3. **Brute Force Process**

The script works by either reading passwords from a file or generating all possible combinations of private keys of the specified length. Each combination is tested against the target wallet address. If the private key corresponds to the wallet address, the tool will log the private key.

### 4. **Supported Cryptocurrencies**

Currently, the following cryptocurrencies are supported by the tool:

- Bitcoin
- Ethereum
- Litecoin
- Dogecoin
- Ripple
- Cardano
- Polkadot
- Binance Coin
- Solana
- Tron

### 5. **Output**

If the private key is found, the script will log it to the specified output file. It also prints the found private key and related information to the terminal.

### 6. **Logging and Display**

While attempting to find the correct private key, the tool prints helpful logs to the console to show which private keys are being tested, which cryptocurrency is being used, and the current thread processing the attempt. The console output is color-coded for easier readability.

## Requirements

To run the BruteForce Key Finder Tool, you will need to have the following installed on your system:

- Python 3.x
- Required Python libraries:
  - `colorama` (for colored console output)
  - `tkinter` (for file selection dialogs)

You can install the required libraries using `pip`:

```bash
pip install colorama

exmple output
********************************************
*      BruteForce Key Finder Tool          *
********************************************

--- BruteForce Key Finder Menu ---
Enter Wallet Address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
Choose Cryptocurrency Type:
1. Bitcoin
2. Ethereum
...
Enter Private Key Length: 32
Enter Number of Threads: 4
Enter Max Attempts: 1000000
Enter Timeout (in seconds): 0.1
Enter Output File Name: output.txt

Thread 0: Bitcoin Wallet - Testing password: abc12345
Thread 1: Bitcoin Wallet - Testing password: def67890
...
Found private key for Bitcoin: abc12345
