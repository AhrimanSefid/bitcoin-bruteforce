# bitcoin-bruteforce [![CodeFactor](https://www.codefactor.io/repository/github/meesvw/bitcoin-bruteforce/badge)](https://www.codefactor.io/repository/github/meesvw/bitcoin-bruteforce)
Bitcoin public address brute force written in Python

## Functions
- Divide workload over multiple CPU cores
- Multiple bruteforce functions
- Compare multiple wallets to increase cracking speed

### Up coming features
- Online wallet lookup (OBF)
- Automatic payout system
- Progress bar

## Setup

**THIS IS FOR EDUCATIONAL PURPOSES ONLY, YOU ARE RESPONSIBLE FOR YOUR ACTIONS**

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

4. Add wallets in the [wallets.txt](wallets.txt) file:
```bash
$ sudo nano wallets.txt
```

5. Run the code:

```bash
$ python3 bruteforce.py
```

#### Keep the code running when closing SSH session (Optional):

To keep your code running you can use screen. Install screen with the following command:
```bash
sudo apt install -y screen
```

After that just start the Python program (exit this session by pressing `ctrl` + `a` + `d`):
```bash
sudo screen python bruteforce.py
```

If you want to connect to your last session just use:
```bash
sudo screen -r
```

## Usage

### Add a wallet
When adding a new wallet to the [wallets.txt](wallets.txt) file. Just insert it on top:
```
;new address here;
1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ
1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF
1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC
...
```

Check if the wallet has balance using [Blockchain Explorer](https://www.blockchain.com/explorer). You can use any wallet checker you like.

### Start program
This Python script has multiple functions:
- OTBF (Optimized traditional bruteforce) <- **This is faster than TBF**
- TBF  (Traditional bruteforce) <- **Will try every wallet possible**
- RBF  (Random bruteforce)
- OBF  (Online bruteforce) <- **Not finished nor started**

In this example we will run the TBF attack on the wallets inside of the [wallets.txt](wallets.txt) file:
```
 1. $ python bruteforce.py                                         # start the python program
 2. $ Select bruteforce mode:
 3. $ 0 - Exit
 4. $ 1 - RBF
 5. $ 2 - TBF
 6. $ 3 - OTBF
 7. $ > 1                                                          # choose the function to use
 8. $ How many cores do you want to use (8 available):
 9. $ > 8                                                          # choose how many cores you want to use
10. $ 
11. $ Starting bruteforce instances in mode: RBF with 8 core(s)    # feedback that it started bruteforcing
```

After line 11 you will see the instances that started, depending on the CPU cores you picked.

### Found a wallet
When the bruteforce matches an address in the [wallets.txt](wallets.txt) file. It will add or create the found.txt file. The Python program will also print the following:
```bash
$ Instance: 1 - Found: 1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ
```

## Donations
> NANO: nano_3hsbm1yhsio64gs9u8gi4hqhapydmmn9n6m8g6ijktfukjkp5bisjxm8wh6r
