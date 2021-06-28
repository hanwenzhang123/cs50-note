# all possible code from 0000 to 9999
10 * 10 * 10 * 10 = 10,000 possibilities

from string import digits
from itertools import product

for passcode in product(digits, repeat = 4):
  print("".join(passcode))


# all possible code for 4 letter digits
52 * 52 * 52 * 52 = 7,311,616 possibilities

from string import ascii_letters
from itertools import product

for passcode in product(ascii_letters, repeat = 4):
  print("".join(passcode))

  
# all possible code for 4 digits with letter, numbers, punctuation
94 * 94 * 94 * 94

from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters + digits + punctuation, repeat = 4):
  print("".join(passcode))
  
