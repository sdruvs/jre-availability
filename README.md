# jre-availability
This Python code serves several purposes. It begins by checking whether the Java Runtime Environment (JRE) is available on the system and determines its version using the java_check() function. If JRE is not available, it attempts to silently install it from a specified installer path using the java_install() function. Following that, it generates a timestamp, creates a pandas DataFrame, and extracts the Java version information using regular expressions. Finally, the code exports this collected information, which includes the timestamp, Java version, and availability status, into a CSV file named "java-availability.csv."

# Setup Up the Development Environment
To ensure a consistent development environment across all systems, follow these steps to set up a virtual environment and install dependencies.

### Windows
1. Open **Command Prompt** (`cmd`) or **PowerShell**.  
2. Run the setup script:  
   ```cmd
   setup.bat
   ```
### Linux
1. Open a terminal.  
2. Run the setup script:  
   ```bash
   ./setup.sh

# Donations
If this repository helps you in your development or if you would like to support this development, you can give me a cup of coffee. ☕

You can send me:

- Bitcoin (BTC) 
- Ethereum (ERC-20)
- Polkadot (DOT)
- Cardano (ADA) 

Wallet address: 

```bash
web3sdruvs.crypto
```

Bitcoin address: 
```bash
bc1qjgz6y7sh2rw5fl55432rr6n6vs9hrhhhsn2eft
```