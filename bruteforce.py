from bit import Key
from time import time
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor

with open('wallets.txt', 'r') as file:
  wallets = file.read()

max_p = 115792089237316195423570985008687907852837564279074904382605163141518161494336
sep_p = round(max_p / cpu_count())


# random bruteforce
'''
Will randomly generate addresses
'''
def RBF(r):
  start = time()
  print(f'Instance: {r + 1} - Generating random addresses...')
  for _ in range(1000000):
    pk = Key()
    if pk.address in wallets:
      print(f'Instance: {r + 1} - Found: {pk.address}')
      with open('found.txt', 'a') as result:
        result.write(f'{pk.to_wif()}')
  print(f'Instace: {r + 1} - done after %s' % (time() - start))


# traditional bruteforce (slowest)
'''
Will try every INT from 0 to max possible
'''
def TBF(r):
  sint = sep_p * r
  mint = sep_p * (r + 1)
  start = time()
  print(f'Instance: {r + 1} - Generating addresses...')
  while sint < mint:
    try:
      pk = Key.from_int(sint)
      if pk.address in wallets:
        print(f'Instance: {r + 1} - Found: {pk.address}')
        with open('found.txt', 'a') as result:
          result.write(f'{pk.to_wif()}\n')
    except Exception:
      pass
    sint += 1
  print(f'Instance: {r + 1}  - Done after %s' % (time() - start))


# optimized traditional bruteforce
'''
Will try every INT between 10**75 and max possibility.
This methode is based on the best practice to get the safest address possible.
'''
def OTBF(r):
  sint = (sep_p * r) + 10**75
  mint = (sep_p * (r + 1))
  print(f'Instance: {r + 1} - Generating addresses...')
  while sint < mint:
    try:
      pk = Key.from_int(sint)
      if pk.address in wallets:
        print(f'Instace: {r + 1} - Found: {pk.address}')
        with open('found.txt', 'a') as result:
          result.write(f'{pk.to_wif()}\n')
    except Exception:
      pass
    sint += 1


# set bruteforce mode
print('Select bruteforce mode:\n0 - Exit\n1 - RBF\n2 - TBF\n3 - OTBF')
try:
  option = int(input('> '))
except ValueError:
  option = 0

mode = [None, RBF, TBF, OTBF]

# start bruteforce instances
if mode[option]:
  print(f'Starting bruteforce instances in mode: {mode[option].__name__}')

  with ProcessPoolExecutor() as executor:
    executor.map(mode[option], range(cpu_count()))

print('Stopping...')
