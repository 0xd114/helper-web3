from web3 import Web3
import binascii

def str_32bytes(st: str) -> str:
    assert len(st) < 32, "too long :("

    ret = Web3.toHex(st.encode())
    ret = ret + '0' * (66-len(ret))
    return ret

def uint8_sha3(x: int) -> (str, bytes):
    '''return sha3 / keccak of int in form of bytes and hex'''

    assert (x < 256 and x >= 0), "0 - 255 only"
    ret = Web3.keccak(x).hex()
  
    return (ret, binascii.unhexlify(ret[2:]))

