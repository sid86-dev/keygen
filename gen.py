import random
import hashlib

def hash(text):
  has = hashlib.sha256(text.encode()).hexdigest()
  return has


# from numba import jit

def gen_easy_32(): 

    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    pswd = ""
    for _ in range(32):
        n = random.choice(letters)
        pswd += n

    return pswd

def gen_easy_16(): 

    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    pswd = ""
    for _ in range(16):
        n = random.choice(letters)
        pswd += n

    return pswd

def gen_strong_32(): 

    letters = "abcdefghijklmnopqrstuvwxyz1234567890!#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
    pswd = ""
    for _ in range(32):
        n = random.choice(letters)
        pswd += n

    return pswd

def gen_strong_16(): 

    letters = "abcdefghijklmnopqrstuvwxyz1234567890!#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
    pswd = ""
    for _ in range(16):
        n = random.choice(letters)
        pswd += n

    return pswd

def gen_strong(): 

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    pswd = ""
    for _ in range(11):
        n = random.choice(letters)
        pswd += n

    return pswd


if __name__=="__main__":
    num = random.random()
    print(hash(str(num)))

''' print(gen_easy_16())
    print(gen_easy_32())
    print(gen_strong())
    print(gen_strong_32())
    print(gen_strong_16())
'''
