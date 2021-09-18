import time
from hashlib import sha256, sha384, sha512, md5, sha1, sha224
from os import urandom as random # use os.urandom for speed

choice = input("what algorithm are you using for calculating your hashrate \
per second today?\ninput:\t")

algs = ("sha256", "sha512", "sha224", "sha1", "sha384", "md5")

algorithms = dict.fromkeys(algs, "available")

def choiceofHash(para):
    if choice == "sha256":
        _hash_ = sha256(para).hexdigest()
    elif choice == "sha512":
        _hash_ = sha512(para).hexdigest()
    elif choice == "sha384":
        _hash_ = sha384(para).hexdigest()
    elif choice == "sha1":
        _hash_ = sha1(para).hexdigest()
    elif choice == "md5":
        _hash_ = md5(para).hexdigest()
    elif choice == "sha224":
        _hash_ = sha224(para).hexdigest()
    print(_hash_)

def calculateHashRate():
    hashList = []
    timeout = time.time() + 1 # length of how long it should print for
    while time.time() < timeout: # print for 1 second
        """ change value to get more accurate result """ 
        randomByteToHash = random(1) # measured in bytes
        calc = choiceofHash(randomByteToHash)
        hashList.append(calc)
    print("hashrate per second using {}: {}".format(choice, len(hashList)))

# function call
if choice == "sha224" or choice == "sha256" or choice == "sha384" or choice  \
            == "sha1" or choice == "md5" or choice == "sha512":
    calculateHashRate()
elif choice == "help":
    print("available algorithms are {}".format(algorithms))
else:
    print("invalid algorithm\ntype \"help\" for seeing the available algorithms")

""" my results on a chromebook with 1 pseudo random byte """
# RESULTS FOR MD5: (2266 + 2386 + 2881 + 2911 + 2716) / 5 = 2.632 kilohashes per second
# RESULTS FOR SHA256: (1365 + 1337 + 1526 + 1554 + 1337) / 5 = 1.4238 kilohashes per second
# RESULTS FOR SHA512: (679 + 709 + 586 + 739 + 742) / 5 = 0.691 kilohashes per second
# RESULTS FOR SHA1: (2267 + 2362 + 2267 + 1799 + 2267) / 5 =  kilohashes per second
# RESULTS FOR SHA384: (980 + 785 + 985 + 940 + 975) / 5 =  kilohashes per second
# RESULTS FOR SHA224: (1600 + 1600 + 1768 + 1528 + ) / 5 =  kilohashes per second
