from web3 import Web3, HTTPProvider
import binascii
import os

INFURA_API_KEY = os.getenv('INFURA_API_KEY')

providers = dict()
providers['ropsten'] = Web3(HTTPProvider(f'https://ropsten.infura.io/v3/{INFURA_API_KEY}'))


'''return string to 32 bytes representation'''
def str_32bytes(st: str) -> str:

    assert len(st) < 32, "too long :("

    ret = Web3.toHex(st.encode())
    ret = ret + '0' * (66-len(ret))
    return ret


'''return sha3 / keccak of int in form of hex and bytes'''
def uint8_sha3(x: int) -> (str, bytes):

    assert (x < 256 and x >= 0), "0 - 255 only"
    ret = Web3.keccak(x).hex()

    return {
        'hex': ret, 
        'bytes': binascii.unhexlify(ret[2:])
    }


'''return storage at slot_no of a smart contract address'''
def get_storage(addr: str, 
                slot_no: int, 
                provider: str = 'ropsten') -> str:
    res = providers['ropsten'].eth.get_storage_at(addr, slot_no)
    return {
        'int': Web3.toInt(res),
        'bytes': res
    } 