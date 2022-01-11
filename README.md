# bitcoin-bruteforce
Bitcoin public address brute force written in Python

## Usage
This Python script has multiple functions:
- OTBF (Optimized traditional bruteforce)
- TBF  (Traditional bruteforce)
- RBF  (Random bruteforce)
- OBF  (Online bruteforce) <- **Not finished nor started**

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
