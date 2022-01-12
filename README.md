# bitcoin-bruteforce
Bitcoin public address brute force written in Python
[![CodeFactor](https://www.codefactor.io/repository/github/meesvw/bitcoin-bruteforce/badge)](https://www.codefactor.io/repository/github/meesvw/bitcoin-bruteforce)

## Usage

### Start program
This Python script has multiple functions:
- OTBF (Optimized traditional bruteforce) <- **Does not work as intended yet**
- TBF  (Traditional bruteforce)
- RBF  (Random bruteforce)
- OBF  (Online bruteforce) <- **Not finished nor started**

In this example we will run the TBF attack on the wallets inside of the [wallets.txt](wallets.txt):
```bash
1. $ python bruteforce.py                          # start the python program
2. $ Select bruteforce mode:
3. $ 0 - Exit
4. $ 1 - RBF
5. $ 2 - TBF
6. $ 3 - OTBF
7. $ > 1                                           # choose the function to use
8. $ Starting bruteforce instances in mode: RBF    # feedback that it started bruteforcing
```

After line 8 you will see the instances that started, depending on the CPU cores you picked.

### Found a wallet
When the bruteforce matches an address in the [wallets.txt](wallets.txt) file. It will add or create the found.txt file. The Python program will also print the following:
```bash
$ Instance: 1 - Found: 1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ
```

## Setup

### Debian install
1. Install [Python](https://www.python.org/downloads/)
2. Install git and clone this repo:

```bash
$ sudo apt update -y && sudo apt upgrade -y
$ sudo apt install git -y
$ git clone https://github.com/meesvw/bitcoin-bruteforce.git
```

3. Go into the bitcoin-bruteforce folder and install the requirements:

```bash
$ pip install -r requirements.txt
```

4. Add wallets in the wallets.txt file:
```bash
$ sudo nano wallets.txt
```

5. Run the code:

```bash
$ python3 bruteforce.py
```

## Donations
> NANO: nano_3hsbm1yhsio64gs9u8gi4hqhapydmmn9n6m8g6ijktfukjkp5bisjxm8wh6r
