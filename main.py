import time
from hashlib import sha256, sha384, sha512, md5, sha1, sha224

# not an accurate implementation. Better for testing how fast a hashing algorithm works
# which basically is helps determine hashrate

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

def calculateHashRate():
    hashList = []
    timeout = time.time() + 1 # length of how long it should print for
    while time.time() < timeout: # calculate for 1 second
        """ change value to get more accurate result """ 
        btc_genesis_block = \
        "GetHash()      = 0x000000000019d6689c085ae165831e934ff763ae46\
        a2a6c172b3f1b60a8ce26f\nhashMerkleRoot = 0x4a5e1e4baab89f3a3251\
        8a88c31bc87f618f76673e2cc77ab2127b7afdeda33b\ntxNew.vin[0].\
        scriptSig     = 486604799 4 0x736B6E616220726F662074756F6C69616\
        220646E6F63657320666F206B6E697262206E6F20726F6C6C65636E616843203\
        93030322F6E614A2F33302073656D695420656854\ntxNew.vout[0].nValue\
        = 5000000000\ntxNew.vout[0].scriptPubKey = 0x5F1DF16B2B704C8A57\
        8D0BBAF74D385CDE12C11EE50455F3C438EF4C3FBCF649B6DE611FEAE06279A\
        60939E028A8D65C10B73071A6F16719274855FEB0FD8A6704 OP_CHECKSIG\
        block.nVersion = 1\nblock.nTime    = 1231006505\nblock.nBits    \
        = 0x1d00ffff\nblock.nNonce   = 2083236893\nCBlock(hash=000000000\
        019d6, ver=1, hashPrevBlock=00000000000000, hashMerkleRoot=4a5e1\
        e, nTime=1231006505, nBits=1d00ffff, nNonce=2083236893, vtx=1)\n\
          CTransaction(hash=4a5e1e, ver=1, vin.size=1, vout.size=1, \
          nLockTime=0)\nCTxIn(COutPoint(000000, -1), coinbase 04ffff0\
          01d0104455468652054696d65732030332f4a616e2f32303039204368616\
          e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c\
          6f757420666f722062616e6b73)\nCTxOut(nValue=50.00000000, script\
          PubKey=0x5F1DF16B2B704C8A578D0B)\nvMerkleTree: 4a5e1e";
        calc = choiceofHash(btc_genesis_block.encode())
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
