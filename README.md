# Subdomain Brute Force Tool

This Python script is a subdomain brute-force tool designed to identify active subdomains of a specific target domain. It utilizes a user-provided wordlist to generate potential subdomains and then performs DNS queries to determine which of these subdomains are active. 

## Usage

1. **Install Dependencies**: Before running the script, make sure you have the `dnspython` library installed. You can install it via pip:
   
   ```
    pip install dnspython
   ```
   
2. **Run the Script**: Execute the script `dnsbrute.py`. You will be prompted to enter the target domain (`example.com`) and the path to the wordlist file containing potential subdomains.

3. **View Results**: The script will display any active subdomains found along with their corresponding IP addresses.

## Example

$ python dnsbrute.py

Enter the target domain (example.com): example.com

Enter the path to the wordlist file: wordlist-example.txt

**Output**
```
subdomain1.example.com -> 192.0.2.1

subdomain2.example.com -> 192.0.2.2
```

## Requirements

- Python 3.x
- dnspython library
